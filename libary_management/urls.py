from django.contrib import admin
from django.urls import path,include
from debug_toolbar.toolbar import debug_toolbar_urls
from .views import Root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Root),
    path("api-auth/", include("rest_framework.urls")),
    path('api/',include('api.urls'),name='api_root')
] + debug_toolbar_urls()
