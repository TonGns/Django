from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<emp_id>', views.delete, name='delete'),
    path('update/<emp_id>', views.update, name='update'),
    path('update/updaterecord/<emp_id>', views.updaterecord, name='updaterecord'),
]

