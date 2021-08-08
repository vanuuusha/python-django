from django.core.exceptions import PermissionDenied


class FilerIpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        bad_ip = []
        ip = request.META.get("REMOTE_ADDR")
        if ip in bad_ip:
            raise PermissionDenied

        response = self.get_response(request)
        return response

