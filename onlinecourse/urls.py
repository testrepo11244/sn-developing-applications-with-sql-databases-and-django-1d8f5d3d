from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    path('<int:submission_id>/submit/', views.submit, name='submit'),
    path('<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]