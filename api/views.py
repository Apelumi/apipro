from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from .models import User

@api_view(['POST', 'GET'])
def user_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST', 'GET'])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    print(email,password,'seyi')
    user = authenticate(request=request, email=email, password=password, backend=None)
    
    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        error_message = 'Invalid credentials'
        if user is None:
            error_message = 'User not found'
        elif not user.is_active:
            error_message = 'User account is disabled'
        elif not user.check_password(password):
            error_message = 'Incorrect password'
    return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def user_logout(request):
    logout(request)
    return Response({'success': 'You have successfully logged out'})
