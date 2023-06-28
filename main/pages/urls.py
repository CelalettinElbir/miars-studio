from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('projects/', ProjectsListView.as_view(),name = "projects"),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project-detail'),
    path("about-us",about_us,name = "about-us"),
    path("contact-us",ContactUsView.as_view(),name = "contact")
]
