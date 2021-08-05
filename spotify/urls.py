from spotify.views import AuthURL
from django.urls import path
from .views import AuthURL


#criar as urls para acessar as diferentes páginas
urlpatterns = [
    path('get-auth-url', AuthURL.as_view()),
]