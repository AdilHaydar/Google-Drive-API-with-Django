from django.shortcuts import render,redirect,HttpResponse
from .models import OrganizationMember,Organization,Document,DocumentPackage,Folder
from django.contrib import messages
from .forms import OrganizationForm, OrganizationMemberForm, DocumentForm,DocumentPackageForm,FolderForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
# Create your views here.

host = settings.EMAIL_HOST
port = settings.EMAIL_PORT
username = settings.EMAIL_HOST_USER
password = settings.EMAIL_HOST_PASSWORD

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def create_folder(folder_name):
    folder = drive.CreateFile({'title':folder_name, "mimeType": "application/vnd.google-apps.folder"})
    folder.Upload()
    return folder['id']

def check_folder_exists(folder_name):

    list_of_file = drive.ListFile({'q':"'root' in parents and trashed=false"}).GetList()
    for drive_folder in list_of_file:
        if drive_folder['title'] == folder_name:
            return drive_folder['id']
        else:
            folder_id = create_folder(folder_name)
            return folder_id

def index(request):
    organization_form = OrganizationForm(request.POST or None)
    document_form = DocumentForm(request.POST or None)
    document_package_form = DocumentPackageForm(request.POST or None)
    organization_member_form = OrganizationMemberForm(request.POST or None)
    folder_form = FolderForm(request.POST or None)
    forms = {
        'organization_form' : organization_form,
        'document_form' : document_form,
        'document_package_form' : document_package_form,
        'organization_member_form' : organization_member_form,
        'folder_form' : folder_form
    }
    if request.method == "POST":
        if organization_form.is_valid():
            create_organization = organization_form.save(commit=True)

        if document_form.is_valid():
            create_document = document_form.save()

        if document_package_form.is_valid():
            user = OrganizationMember.objects.get(id=request.user.id)
            create_document_package = document_package_form.save(commit=False)
            create_document_package.created_by = user
            create_document_package.save()

        if organization_member_form.is_valid():
            create_organization_member = organization_member_form.save()

        if folder_form.is_valid():
            
            create_folder_form = folder_form.save()
        return redirect('index')
    return render(request,'main_page.html', forms)


def upload_file_inside_folder(title, fid, full_path):
    file = drive.CreateFile({'title':title, "parents":[{"kind":"drive#filelink", "id":fid}]})
    file.SetContentFile(full_path)
    file.Upload()
    return True

def mail(request):
    
    document_form = DocumentForm(request.POST or None, request.FILES)
    if request.method == "POST":
        print("POST REQUEST")
    if document_form.is_valid():
        create_folder = document_form.save(commit=True)
        subject = request.POST.get('subject')
        object = request.POST.get('object')
        to = request.POST.get('to')
        file = create_folder.file

        email = EmailMessage(subject,object,settings.EMAIL_HOST_USER,to.split(','))
        email.content_subtype = 'html'
        email.attach(file.name, file.read(), 'text/plain')
        email.send()

        upload_file_inside_folder(str(file.name),check_folder_exists(create_folder.package.folder.folder_name),file.path)

        return HttpResponse('Mail Send is Successfully')

    return render(request,'mail_send.html', {'document_form':document_form})
