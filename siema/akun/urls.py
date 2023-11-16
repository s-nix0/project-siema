from django.urls import path
from .views import login_user, logout_user, AccountView


urlpatterns = [
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('profil/', AccountView.as_view(), name="profile"),
]
