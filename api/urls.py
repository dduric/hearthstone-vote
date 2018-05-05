from django.urls import path

from api import views


urlpatterns = [
    path('state_update/', views.state_update, name='state_update'),
]
