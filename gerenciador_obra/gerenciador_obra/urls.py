
from django.contrib import admin
from django.urls import path

from historico import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("historico/", views.get_csv),
    path("api/", views.HistoricoView.as_view())
]
