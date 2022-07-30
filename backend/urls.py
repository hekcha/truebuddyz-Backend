from config import Config
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path(Config.ADMIN_URL, admin.site.urls),
    path('core/', include('core.urls')),
    path('quiz/', include('quiz.urls')),
    path('rf/', include('rf.urls')),
    path('youlooklike/', include('youlooklike.urls')),
    path('howwelluknow/', include('howwelluknow.urls')),
    path('twooptions/', include('twooptionsque.urls')),
    path('auth/', obtain_auth_token),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
