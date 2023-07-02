from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from studentlogin import views as studentlogin_views
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'studentapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^student/', include('studentlogin.urls')),
    url(r'^$', studentlogin_views.index),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
