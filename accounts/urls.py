from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logout, name="logout"),
    path('confirm_payement/', views.confirm_payement, name="confirm_payement"),
    path('message_us/', views.message_us, name="message_us"),
]
