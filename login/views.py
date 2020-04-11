from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Register,Loginuser
from rest_framework import viewsets,permissions
from .serializers import RegisterSerializer,LoginuserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
import json
from rest_framework import serializers
from rest_framework.serializers import ValidationError

#from .models import Register

'''
class RegisterViewSet(viewsets.ModelViewSet):
    queryset=Register.objects.all()
    serializer_class=RegisterSerializer
    #permission_classes = (IsAuthenticated,)  
    

'''
class RegisterAPIView(APIView):
    serializer=RegisterSerializer

    
    def post(self, request):
        data = request.data
        pwd1=request.data.get("pass1")
        pwd2=request.data.get("passconf")

        # Create an article from the above data
        if pwd1!=pwd2:
            raise ValidationError("password do not match")
        if len(pwd1)<8:
            raise ValidationError("password too short ,must be of minimum 8 characters")


        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            register_saved = serializer.save()
        return Response({"success": "created successfully"})
    

# Create your views here.



class UserLoginAPIView(APIView):
    #permission_classes = [AllowAny]
    serializer= LoginuserSerializer
    
    def get(self,request,*args,**kwargs):
        data=request.data
        userid=data.get("userid")
        user_object=Register.objects.filter(userid=userid).values('name','phone','email','pass1')
        
        if user_object:
            #print(user_object[0]['name'])
            d=json.dumps(user_object[0])
            print(d)

        serializer = LoginuserSerializer(data=data)
        if serializer.validate(data):
            #print(user_object[0])
            return Response(d,status=HTTP_200_OK)
        
            
        

