from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .utils.sms import send_sms

# from .forms import SignUpForm


# Create your views here.
class UserRegisterView(CreateView):
    model = User
    fields = [
        "username",
        "email",
        "password",
    ]
    template_name = "index.html"
    success_url = "/"

    def form_valid(self, form):
        email = form.instance.email
        res = send_sms(email)
        print(res)

        print(form.instance.email)
        return super().form_valid(form)
