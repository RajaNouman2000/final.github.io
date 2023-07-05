

from django.urls import path
from . import views

urlpatterns = [
    path('record/', views.record, name='record'),
    path('registrations/', views.registration, name='registration_submit'),
    path('registrations/<int:record_id>/',
         views.delete_registration, name='delete_registration'),
    path('edit-registration/<int:record_id>/',
         views.edit_registration, name='edit_registration'),

]
