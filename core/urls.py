from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

def home(request):
    return JsonResponse({'message': 'API online'})

urlpatterns = [
    path('', home),  # <- agrega esto
    path('admin/', admin.site.urls),
    path('api/blog/', include('apps.blog.urls')),
    path('api/category/', include('apps.category.urls')),


]  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)