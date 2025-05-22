from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import APIView
from rest_framework.request import Request
from rest_framework import status
from rest_framework import mixins, generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema

from .serializers import UserSerializer, RegisterUserSerializer
from users.models import User

# This is the api view for users list
class UsersListApiView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

# this is the api view for authenticated user details
class UserDetailApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get(self, request:Request):
        return self.retrieve(request)

    def put(self, request:Request):
        return self.update(request)


# this is the api view for user registration
class RegisterApiView(APIView):
    @extend_schema(
        request=RegisterUserSerializer,
        responses={201: RegisterUserSerializer},
        description= 'This Api view is used to register a new user.'
    )
    def post(self, request: Request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)