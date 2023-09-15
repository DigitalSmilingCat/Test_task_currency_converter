from django.urls import path
from .views import get_with_parameters
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='rates')),
    path('rates', get_with_parameters),
]
