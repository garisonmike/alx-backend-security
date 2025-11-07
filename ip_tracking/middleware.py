import datetime
from django.utils import timezone
from django.http import HttpResponseForbidden
from django.core.cache import cache
from ip_tracking.models import RequestLog, BlockedIP
from ipgeolocation import IpGeolocationAPI

class IPTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.geo_api = IpGeolocationAPI("YOUR_API_KEY_HERE")

    def __call__(self, request):
        ip = self.get_client_ip(request)

        # Block blacklisted IPs
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Access denied")

        # Log IP info
        country, city = self.get_geo_data(ip)
        RequestLog.objects.create(
            ip_address=ip,
            path=request.path,
            timestamp=timezone.now(),
            country=country,
            city=city
        )

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    def get_geo_data(self, ip):
        cache_key = f"geo_{ip}"
        cached = cache.get(cache_key)
        if cached:
            return cached
        try:
            response = self.geo_api.get_geolocation(ip)
            country = response.get("country_name", "")
            city = response.get("city", "")
            cache.set(cache_key, (country, city), 86400)
            return country, city
        except Exception:
            return "", ""
