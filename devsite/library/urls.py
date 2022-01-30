from django.urls import path
from library import views

urlpatterns = [
    path('', views.library, name='library'),
    path('library_add', views.library_add, name="library_add"),
    path("<int:pk>/", views.library_detail, name="library_detail"),
]
