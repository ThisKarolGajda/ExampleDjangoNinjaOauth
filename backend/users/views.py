# views.py
from time import sleep

from django.http import JsonResponse
from ninja import Router

from backend.auth import auth, aauth

router = Router()

@router.get('get/')
def get_user_info(request):
    user = auth(request)

    return JsonResponse({
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'date_of_birth': user.date_of_birth,
    })

@router.get('aget/')
async def get_user_info(request):
    user = await aauth(request)

    return JsonResponse({
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'date_of_birth': user.date_of_birth,
    })