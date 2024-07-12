from django.contrib import admin
from django.urls import path
from game_logs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastre/', views.cadastre, name='cadastre'),
    path('contato/', views.contato, name='contato'),
    path('login/', views.login, name='login'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('play', views.play, name='play'),
]

