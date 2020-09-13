from django import forms
from .models import Organization,OrganizationMember,Folder,DocumentPackage,Document

class OrganizationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ['name']

class OrganizationMemberForm(forms.ModelForm):

    class Meta:
        model = OrganizationMember
        fields = ['organization_member','user']

class FolderForm(forms.ModelForm):

    class Meta:
        model = Folder
        fields = ['folder_name','organization_folder']

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.isdigit():
            raise forms.ValidationError('Please do not enter only digit.')

        if '@' in name:
            raise forms.ValidationError('Please do not enter @ sign.')
        return name

class DocumentPackageForm(forms.ModelForm):

    class Meta:
        model = DocumentPackage
        fields = ['organization', 'folder']

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['package','file']

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['package'].widget.attrs['class'] = 'input_field'
