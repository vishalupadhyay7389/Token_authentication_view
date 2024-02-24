from django.urls import path
from api.views import StudentDetailView , StudentListView , StudentRetriView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('student/', StudentDetailView.as_view(),name='students'),
    path('stud/', StudentListView.as_view(),name='student'),
    path('stud/<int:pk>/', StudentRetriView.as_view(),name='student'),
    path('auth/login/',obtain_auth_token ,name='create-token'),
    
]