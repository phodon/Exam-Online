from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('register/',views.register_user, name='register'),
    path('detail/<int:pk>',views.customer_record, name='detail'),
    path('delete/<int:pk>', views.delete_record, name= 'delete'),
    path('add/', views.add_record, name='add'),
    path('update/<int:pk>',views.update_record, name='update'),
]
