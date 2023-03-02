from django.http import HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        template_name = 'app_menu/home.html'
        return render(request, template_name)
