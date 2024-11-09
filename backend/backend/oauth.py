# views.py
from authlib.integrations.django_oauth2 import requests
from django.http import JsonResponse
from authlib.integrations.django_client import OAuth
from django.conf import settings
from ninja import Router
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import CustomUser

router = Router()

oauth = OAuth()
oauth.register(
    name='google',
    client_id=settings.OAUTH_GOOGLE_CLIENT_ID,
    client_secret=settings.OAUTH_GOOGLE_CLIENT_SECRET,
    client_kwargs={'scope': 'openid profile email'},
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration'
)

def generate_jwt(user):
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)
    return {
        'access_token': access_token,
        'refresh_token': refresh_token
    }

@router.get('/google-login/')
def google_login(request):
    redirect_uri = request.build_absolute_uri('/api/v1/auth/google-callback/')
    return oauth.google.authorize_redirect(request, redirect_uri)

@router.get('/google-callback/')
def google_callback(request):
    try:
        token = oauth.google.authorize_access_token(request)
        user_info = token.get('userinfo')
        if not user_info:
            raise ValueError('No user info found in the token')

        if user_info.get('iss') != "https://accounts.google.com":
            raise ValueError('Invalid issuer in ID token')

        user, _ = CustomUser.objects.get_or_create(
            email=user_info['email'],
            defaults={
                'first_name': user_info.get('given_name', ''),
                'last_name': user_info.get('family_name', '')
            }
        )

        jwt_token = generate_jwt(user)
        return JsonResponse({'token': jwt_token})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@router.get('/refresh-token/')
def refresh_jwt_token(request):
    try:
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return JsonResponse({'error': 'Authorization header is missing'}, status=400)

        parts = auth_header.split()
        if parts[0].lower() != 'bearer' or len(parts) == 1:
            return JsonResponse({'error': 'Authorization header must be Bearer token'}, status=400)

        refresh_token = parts[1]
        refresh = RefreshToken(refresh_token)
        new_access_token = str(refresh.access_token)
        new_refresh_token = str(refresh)
        return JsonResponse({'access_token': new_access_token, 'refresh_token': new_refresh_token})

    except TokenError:
        return JsonResponse({'error': 'Invalid refresh token or token expired'}, status=400)