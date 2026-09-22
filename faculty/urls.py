from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.programs, name='programs'),
    path('programs/<int:id>/', views.program_detail, name='program_details'),
    path('departments/', views.departments, name='departments'),
    path('departments/<int:id>/', views.department_detail, name='department_details'),
]
