from django.contrib import admin
from django.urls import path, include
from .utils import redirect_url
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("app.urls")),
    path('<str:short_code>/', redirect_url, name='redirect'),
     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
