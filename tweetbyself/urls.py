from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('tweet/', include("tweetbys.urls")),
] + static(settings.MEDIA_URL, decument_root=settings.MEDIA_ROOT)
