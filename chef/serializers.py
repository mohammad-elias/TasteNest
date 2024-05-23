from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name','mobile','password','confirm_password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def save(self):
        email = self.validated_data['email']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        mobile = self.validated_data['mobile']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists!"})
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched!"})
        
        user = User.objects.create_user(email=email,first_name=first_name,last_name=last_name,mobile=mobile)
        user.set_password(password)
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','first_name','last_name','mobile','image','address','total_recipe','total_event')
        read_only_fields = ('email', 'total_recipe', 'total_event')


