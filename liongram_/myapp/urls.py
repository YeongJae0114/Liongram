from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home, name='home'),
    path('new/', views.create, name='create'),
    path('list/',views.list, name='list'),
    path('<int:id>/',views.detail, name='detail'),
    path('<int:id>/edit/', views.update),
    path('<int:id>/delete/', views.delete),
]
