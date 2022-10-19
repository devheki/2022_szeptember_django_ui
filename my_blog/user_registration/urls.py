from .views import register as register_view
from .views import profile_view
from django.urls import path


urlpatterns = [
    path('register/', register_view, name="register"),
    path('profile/', profile_view, name="profile"),
]