from django.urls import path
from app1.views import *
app_name = 'app1'

urlpatterns = [
    path('dhoni/', dhoni, name = 'dhoni'),
    path('virat/', virat, name = 'virat'),
    path('rohit/', rohit, name = 'rohit')
]