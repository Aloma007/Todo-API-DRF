from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer

class RegisterView(APIView):
    def post(self, request):
        # 1. Pass the incoming JSON data to our translator
        serializer = UserRegistrationSerializer(data=request.data)
        
        # 2. Check if the data is valid (email is unique, password provided, etc.)
        if serializer.is_valid():
            # 3. Save the new user to the database
            user = serializer.save()
            
            # 4. Generate the JWT "wristband" for this specific user
            refresh = RefreshToken.for_user(user)
            
            # 5. Return the exact JSON structure your project guide requested
            return Response({
                'token': str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
            
        # If data is invalid, return the error details and a 400 Bad Request status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        # 1. Extract the email and password from the user's request
        email = request.data.get('email')
        password = request.data.get('password')
        
        # 2. Check if a user with this exact email and password exists
        user = authenticate(email=email, password=password)
        
        # 3. If the user is found and password is correct, generate the token
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'token': str(refresh.access_token),
                'refresh': str(refresh)
            }, status=status.HTTP_200_OK)
            
        # 4. If credentials fail, return a 401 Unauthorized error
        return Response(
            {'message': 'Invalid email or password'}, 
            status=status.HTTP_401_UNAUTHORIZED
        )

