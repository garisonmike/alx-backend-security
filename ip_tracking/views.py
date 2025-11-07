from django.http import HttpResponse
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='10/m', method='GET', block=True)
@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def sensitive_view(request):
    return HttpResponse("Sensitive operation executed successfully.")
