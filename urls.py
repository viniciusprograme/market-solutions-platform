from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from core.views import index, submit_form

urlpatterns = [
    path('', index, name='index'),
    path('submit/', submit_form, name='submit_form'),
]

urlpatterns += staticfiles_urlpatterns()
