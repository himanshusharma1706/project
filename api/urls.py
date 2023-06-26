from django.urls import path
from .views import token_obtain_pair_view, token_refresh_view

urlpatterns = [
    path('api/token/', token_obtain_pair_view, name='token_obtain_pair'),
    path('api/token/refresh/', token_refresh_view, name='token_refresh'),
    path('api/token/registration/', registration_view(request):, name='registarion'),
]
