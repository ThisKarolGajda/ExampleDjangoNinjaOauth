from django.contrib.auth.models import User
from django.conf import settings
import jwt

from backend.unauthorized_exception import UnauthorizedException
from users.models import CustomUser

async def aauth(request):
    """
    Authenticates the request and returns the user associated with the token.
    Raises an UnauthorizedException if authentication fails.
    """
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        raise UnauthorizedException('Unauthorized')

    token = auth_header.split()[1]

    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_token.get('user_id')
        user = await CustomUser.objects.aget(id=user_id)

        return user

    except jwt.ExpiredSignatureError:
        raise UnauthorizedException('Token has expired')
    except jwt.InvalidTokenError:
        raise UnauthorizedException('Invalid token')
    except CustomUser.DoesNotExist:
        raise UnauthorizedException('User not found')


def auth(request):
    """
    Authenticates the request and returns the user associated with the token.
    Raises an UnauthorizedException if authentication fails.
    """
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        raise UnauthorizedException('Unauthorized')

    token = auth_header.split()[1]

    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_token.get('user_id')
        return CustomUser.objects.get(id=user_id)

    except jwt.ExpiredSignatureError:
        raise UnauthorizedException('Token has expired')
    except jwt.InvalidTokenError:
        raise UnauthorizedException('Invalid token')
    except User.DoesNotExist:
        raise UnauthorizedException('User not found')
