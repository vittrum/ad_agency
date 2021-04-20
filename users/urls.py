from django.urls import path
from . import views


urlpatterns = [
    # TODO: all users, concrete user
    # TODO: all departments, employees in department
    path('', views.index, name='index'),
    path('clients/', views.ClientListView.as_view(), name='clients'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
    path('departments/', views.DepartmentListView.as_view(), name='departments'),
]