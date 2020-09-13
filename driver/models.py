from django.db import models

# Create your models here.


class Organization(models.Model):
    name = models.CharField(verbose_name='Organization',max_length=150, unique=True)

    def __str__(self):
        return self.name

class OrganizationMember(models.Model):
    organization_member = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Organization : %s - User : %s" %(self.organization_member,self.user)

class Folder(models.Model):
    folder_name = models.CharField(verbose_name='Folder Name', max_length=170)
    organization_folder = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.folder_name

class DocumentPackage(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_by = models.ForeignKey(OrganizationMember, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    folder = models.ForeignKey(Folder, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Organization : %s - Folder : %s" %(self.organization, self.folder)

class Document(models.Model):
    package = models.ForeignKey(DocumentPackage, on_delete=models.CASCADE)
    file = models.FileField(blank=False,verbose_name='File')

