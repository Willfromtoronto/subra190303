from django.urls import path
from . import views

# URL mapping for the greet web application
urlpatterns = [
 path('', views.greet, name='greet')
]