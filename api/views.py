from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class MyTokenObtainPairView(TokenObtainPairView):
    # Customize response data if needed
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Add additional data to the response
        response.data['custom_field'] = 'Custom data'
        return response

token_obtain_pair_view = MyTokenObtainPairView.as_view()
token_refresh_view = TokenRefreshView.as_view()

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer

@api_view(['POST'])
def registration_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
    if user.check_password(password):
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
