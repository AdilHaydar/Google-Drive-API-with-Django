# Google-Drive-API-with-Django

Öncelikle 'python manage.py makemigrations' ve 'python manage.py migrate --run-syncdb' komutlarını çalıştırın.

daha sonra json formatındaki google drive api dosyasını manage.py dosyasının bulunduğu konuma kopyalayınız.

Bir superuser oluşturun ve '/user/login' adresinden giriş yapın.

index sayfasında bir organizasyon oluşturun.
Folder Form başlığı altında organizasyon için bir klasör oluşturun.
Oluşturduğunuz kullanıcıyı Organization Member Form altında bir organizasyona kaydedin.
Document Package Form ile Organizasyon ve klasörü giriş yapmış olduğunuz kullanıcı ile otomatik olarak eşleyin.

'/drive/mail' adresine gidin. Uygun paketi seçip dosyasınızla birlikte maili gönderin. Gönderdiğiniz mail aynı zamanda belirttiğiniz klasör içerisinde google drive da görülecektir.

ENGLISH

First run the commands 'python manage.py makemigrations' and 'python manage.py migrate --run-syncdb'.

Then copy the google drive api file in json format to the location where manage.py file is located.

Create a superuser and login at '/user/login' 


Create an organization on the index page.
Create a folder for the organization under the Folder Form header.
Register the user you created in an organization under Organization Member Form.
With Document Package Form, automatically map the organization and folder to the user you are logged in with.

Go to /drive/mail'. Select the appropriate package and send the mail with your file. The mail you send will also be seen in the google drive in the folder you specified.
