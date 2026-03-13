from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Native views path
    path('admin/', admin.site.urls),
    
    # Thirdparty views path
    path("api-auth/", include("rest_framework.urls")),

    # Local views path
    path('api/', include("api.urls", namespace="api")),
]
