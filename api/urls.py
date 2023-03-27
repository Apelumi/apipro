from django.urls import path
from api.views import user_signup, user_login, user_logout

urlpatterns = [
    path('signup/', user_signup),
    path('login/', user_login),
    path('logout/', user_logout),
]
