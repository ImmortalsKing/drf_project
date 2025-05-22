from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','bio']

class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'email': {'required': True},
            'username': {'required': True}
        }

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user