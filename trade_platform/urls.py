from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^$', views.category_list, name='category_list'),
	url(r'^catalog/(?P<category_name>[a-zA-z]+)/$', views.goods_list, name='goods_list'),
	url(r'^catalog/$', views.catalog, name='catalog'),
	url(r'^contacts/$', views.contacts, name='contacts'),
]

if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns() + static(
		settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)