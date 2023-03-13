from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),  # Pagina Inicial
    path('recipes/<int:id>/', views.recipe),

]
