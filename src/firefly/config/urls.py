from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


#handler400 = "main.views.bad_request_view"
#handler403 = "main.views.access_denied_view"
#handler404 = "main.views.page_not_found_view"
#handler500 = "main.views.server_error_view"

schema_view = get_schema_view(
    openapi.Info(
        title="Firefly REST API",
        default_version='v1',
        description="API для взаимодействия с веб-сервисом пользователей и оборудования.",
    ),
    public=True,  # False
    permission_classes=(permissions.AllowAny,),
    # permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
    path('', include('main.urls')),
    path('api/v1/', include('api.v1.urls')),

    #path('admin/', admin.site.urls),
]

urlpatterns += [
    #path('swagger/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view().with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view().with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Добавление адреса папки media,
# если включен режим отладки.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
