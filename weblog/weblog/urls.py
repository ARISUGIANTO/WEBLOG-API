from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

# Buat router
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewset)
router.register(r'comments', views.CommentViewSet)
router.register(r'categories', views.CategoryViewSet)

# URLpatterns API
urlpatterns = [
    # Tambahkan router.urls ke urlpatterns
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
