from django.shortcuts import render
from django.views.generic import ListView
from .models import Food, Category


class HomePage(ListView):
    model = Food
    template_name = 'home/HomePage.html'
    context_object_name = 'food'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Food'
        return context
