from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('post_details', views.post_details, name='post_details'),
    path('contact', views.contact, name='contact'),
    path('post_create', views.post_create, name='post_create'),
    path('save_post/', views.save_post, name='save_post'),
    path('save_message/', views.save_message, name='save_message'),
    path('search/', views.search, name='search'),
]





