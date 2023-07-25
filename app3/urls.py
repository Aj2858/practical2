from django.urls import path
from app3.views import *

app_name = 'app3'

urlpatterns = [
    path('manish/', manish, name = 'manish'),
    path('dilip/', dilip, name = 'dilip'),
    path('anj/', anj, name = 'anj')

]