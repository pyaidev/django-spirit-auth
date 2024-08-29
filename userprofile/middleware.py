from django.shortcuts import redirect
from django.urls import reverse

class SiteUserAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            # Avoid redirect loop by checking the current path
            if request.path not in [reverse('login'), reverse('logout')]:
                return redirect(reverse('login'))
        return self.get_response(request)
