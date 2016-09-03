from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings  
from django.conf.urls.static import static
from app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sport_list/' , 'app.views.sport_list'),
    # url(r'^athlete_list/' , 'app.views.athlete_list'),
    url(r'^athlete_list/(?P<pk>\d+)', 'app.views.athlete_list'),
    url(r'^athlete_detail/(?P<pk>\d+)/', 'app.views.athlete_detail'),
    url(r'^about_view/$', 'app.views.about_view'),
    url(r'^events_view/$', 'app.views.events_view'),
    # url(r'^home_view/$', 'app.views.home_view'),
    url(r'^contact/$', 'app.views.contact'),
    # url(r'^base/$', 'app.views.base'),
    url(r'^signup/$', 'app.views.signup'),
    url(r'^login_view/$', 'app.views.login_view'),
    url(r'^logout_view/$', 'app.views.logout_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
