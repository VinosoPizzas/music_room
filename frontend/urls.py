from django.urls import path
from .views import index

app_name = 'frontend'

#criar as urls para acessar as diferentes páginas
urlpatterns = [
    path('', index, name=''),
    path('join', index),
    path('create', index),
    path('room/<str:roomCode>', index), # o /<str:roomCode> é tipo um placeholder e vai ser o código da sala
]