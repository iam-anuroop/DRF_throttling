from django.shortcuts import render
from .serializer import Studentserilaiser
from .models import Student
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle




class Student_view(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserilaiser

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
    

    

    
    


        


        




# Create your views here.
