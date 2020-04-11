from rest_framework import serializers
from login.models import Register,Loginuser
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from rest_framework.serializers import ValidationError


# lead serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields='__all__'
        extra_kwargs = {'pass1': {'write_only': True},'passconf': {'write_only': True}}
        
    def create(self, validated_data):
        user = Register(
            email=validated_data['email'],
            name=validated_data['name'],
            userid=validated_data['userid'],
            phone=validated_data['phone'],
            pass1 = make_password(validated_data['pass1']),
            passconf = make_password(validated_data['passconf'])
        )
        #user.set_password(validated_data['password'])
        #print(pass1)
        user.save()
        return user
        

class LoginuserSerializer(serializers.ModelSerializer):
 #   pass1 = serializers.CharField(
  #      write_only=True,
   #     required=True,
    #    #help_text='Leave empty if no change needed',
     #   style={'input_type': 'password', 'placeholder': 'Password'}
   # )
    class Meta:
        model = Register
        fields=[
        'userid',
        'pass1'
        
        ]


    def validate(self,data):
        user_object=Register.objects.all()
        userid=data.get("userid")
        pass1=data.get("pass1")
       # print(userid)
       # print(pass1)
        if not userid:
            raise ValidationError("username is required") 

        user=Register.objects.filter(

            Q(userid=userid)
        ).values()
        if user.exists():
            user_object=user.first()
        else:
            raise ValidationError("username is not valid") 

        if check_password(pass1,user[0]['pass1']):
            #pass2=user[0]['pass1']
            #if pass1!=pass2:
            print(check_password)
            pass
        else:
            raise ValidationError("incorrect password") 
        #data["token"]= "some random token"
        return data
       