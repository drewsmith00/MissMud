from django.conf.urls import url
from . import views


app_name = 'jewelry'

urlpatterns = [
    url(r'^$', views.JewelryView.as_view(), ),
    url(r'^(?P<brand>[a-z\-]+)/(?P<slug>[a-z\-]+)/$', views.ItemView.as_view(), name='item'),
    url(r'^(?P<slug>[a-z\-]+)/$', views.BrandView.as_view(), name='brand'),
]
