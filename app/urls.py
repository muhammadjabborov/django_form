from django.urls import path

from app.views import form_page, thanks_page

urlpatterns = [
    path('', form_page, name='form'),
    path('thanks/', thanks_page, name='thanks')
]
