import time
from django.core.exceptions import PermissionDenied

list_ip = {}
stop_time = 10
count_requests = 3


class RequestBlocker:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        list_ip[ip] = [list_ip.get(ip, (0, 0))[0] + 1, list_ip.get(ip, (0, time.time()))[1]]
        if time.time() - list_ip[ip][1] > stop_time:
            list_ip.pop(ip)
        elif list_ip[ip][0] >= count_requests:
            list_ip[ip][1] += 15
            raise PermissionDenied

        response = self.get_response(request)
        return response
