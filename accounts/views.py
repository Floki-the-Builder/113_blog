from django.shortcuts import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

class SignUpViews(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse("login")