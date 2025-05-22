from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('swagger-ui'))
        else:
            return redirect('/api-auth/login/')