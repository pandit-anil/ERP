from django.urls import path
from .views import LoginView,RegisterView,ForgetView
from . import views
urlpatterns = [
    path('login',LoginView.as_view(), name="login"),
    path('register',RegisterView.as_view(), name="register"),
    path('forget',ForgetView.as_view(), name="forget"),
    path('logout/', views.Logout, name='logout'),
]
