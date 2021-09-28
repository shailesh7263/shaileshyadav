

from django.contrib import admin

from django.urls import path

from .views import index

from .views import send_gmail

jls_extract_var = [

    path('admin/', admin.site.urls),

    path('',index, name="index"),

    path('send_mail/', send_gmail , name="send_mail"),

]
urlpatterns = jls_extract_var

