from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from ..models import Product, Advertisement, Lead, Contract, Customer
from ..forms import AuthForm


class RequiredLogin(LoginRequiredMixin):
    login_url = reverse_lazy('login')


class Login(LoginView):
    form_class = AuthForm
    redirect_authenticated_user = True
    template_name = 'registration/login.html'
    next_page = reverse_lazy('index')


class Logout(LogoutView):
    next_page = reverse_lazy('login')


class IndexView(RequiredLogin, View):
    def get(self, request):
        data = {
            "products_count": Product.objects.count(),
            "advertisements_count": Advertisement.objects.count(),
            "leads_count": Lead.objects.count(),
            "customers_count": Customer.objects.count(),
            "contracts_count": Contract.objects.count()
        }
        return render(request, "users/index.html", context=data)
