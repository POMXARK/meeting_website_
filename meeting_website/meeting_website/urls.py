from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from .views import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='members/index.html')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/', include('members.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
