from django.http import HttpResponse
from django.conf import settings

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, 'MAINTENANCE_MODE', False) and not request.user.is_staff:
            return HttpResponse("Sayt hozir texnik xizmatda", status=503)
        return self.get_response(request)

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("So‘rov keldi:", request.path)
        response = self.get_response(request)
        print("Javob ketmoqda:", response.status_code)
        return response

class IPLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print("Foydalanuvchi IP manzili:", ip)
        response = self.get_response(request)
        return response