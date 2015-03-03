from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sections.views.home_page', name='home_page'),
    url(r'^sections/kamaus-only$', 'sections.views.view_list', name='view_list'),
    url(r'^sections/new$', 'sections.views.new_list', name='new_list'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
