from django.urls import path

from super_admin.views import loginCheck

path(r'^login/$', loginCheck, name="login")
