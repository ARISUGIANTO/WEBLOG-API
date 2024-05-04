from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

# Buat router
router = DefaultRouter()
router.register(r'users', views.UserViewSet)

# URLpatterns API
urlpatterns = [
    # Tambahkan router.urls ke urlpatterns
    path('api/', include(router.urls)),
]
