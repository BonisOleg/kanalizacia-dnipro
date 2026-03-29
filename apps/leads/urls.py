from django.urls import path
from . import views

urlpatterns = [
    path("contact/", views.contact, name="contact"),
    path("contact/submit/", views.contact_submit, name="contact_submit"),
    path("quiz/", views.quiz_start, name="quiz_start"),
    path("quiz/step/<int:step>/", views.quiz_step, name="quiz_step"),
]
