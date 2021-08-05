from spotify.views import AuthURL
from django.urls import path
from .views import AuthURL, spotify_callback, IsAuthenticated


#criar as urls para acessar as diferentes páginas
urlpatterns = [
    path('get-auth-url', AuthURL.as_view()),
    path('redirect', spotify_callback),
    path('is-authenticated', IsAuthenticated.as_view())
]