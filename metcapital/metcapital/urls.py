"""
URL configuration for metcapital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from metapp.views import PostViewSet, create_auth, get_posts, get_post, update_post, delete_post

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', create_auth, name='create_auth'),
    path('api/posts/', get_posts, name='get_posts'),  # Endpoint to get all posts
    path('api/posts/<int:pk>/', get_post, name='get_post'),  # Endpoint to get a single post
    path('api/posts/<int:pk>/update/', update_post, name='update_post'),  # Endpoint to update a post
    path('api/posts/<int:pk>/delete/', delete_post, name='delete_post'),  # Endpoint to delete a post
    # Add other URL patterns here as needed in the future
]



