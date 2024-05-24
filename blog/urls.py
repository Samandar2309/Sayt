from django.urls import path
from .views import index, detail, Contact

urlpatterns = [
    path('', index, name='index'),
    path('home/<int:pk>/', detail, name='detail'),
    path('contact/', Contact, name='contact'),

]
