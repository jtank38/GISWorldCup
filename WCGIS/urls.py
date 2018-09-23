from django.conf.urls import url,include
from django.contrib import admin
from .import views
from WC import views as WCviews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',WCviews.WCTeam_render,name='home'),
    url(r'^Routing/$',WCviews.Routing_render,name='routings'),
    url(r'^Query/$',WCviews.Query_render,name='queries'),
    url(r'^WC/',include('WC.urls')),
     url(r'^Routing/',include('WC.urls')),
     url(r'^Query/',include('WC.urls')),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)