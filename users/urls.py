from django.urls import path

from users import views

urlpatterns = [
path('sukumar/', views.sukumar_function, name='sukumar_view')
]