
from django.urls import path
from . import views
#from .views import RegisterView
app_name = "driver"


urlpatterns = [
    path('',views.index,name = "index"),
    path('mail',views.mail,name="mail"),
]