from django.views.generic import ListView
from .models import post



class HomePagesview(ListView):
    model = post
    template_name = 'home.html'