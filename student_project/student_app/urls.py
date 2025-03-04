from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('<int:pk>/update/', views.student_update, name='student_update'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
    path('<int:student_id>/add-subject/', views.add_subject, name='add_subject'),
]
