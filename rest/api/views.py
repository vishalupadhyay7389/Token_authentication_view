from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .models import School , Student ,Email , StudentSeralizer
from rest_framework import status
from django.http import Http404
from rest_framework.response import responses
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated , BasePermission
from rest_framework.authtoken.models import Token

# Create your views here.
users = User.objects.all()
for user in users:
    token = Token.objects.get_or_create(user=user)
    print(token)


class WriteByAdminonlyPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'GET':
            return True
        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True
        return False
    

class StudentListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated , WriteByAdminonlyPermission]
    queryset = Student.objects.all()
    serializer_class = StudentSeralizer
    
class StudentDetailView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeralizer
    
class StudentRetriView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeralizer
    

    
