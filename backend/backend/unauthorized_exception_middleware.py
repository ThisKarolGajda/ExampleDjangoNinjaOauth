from django.http import JsonResponse

from backend.unauthorized_exception import UnauthorizedException


class UnauthorizedExceptionMiddleware:
    """Middleware to handle UnauthorizedException globally."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except UnauthorizedException as e:
            return JsonResponse({'error': str(e)}, status=401)
