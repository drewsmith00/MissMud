from django.conf.urls import url
from . import views


app_name = 'pottery'

urlpatterns = [
    url(r'^$', views.PotteryView.as_view(), ),
    url(r'^(?P<brand>[a-z\-]+)/(?P<slug>[a-z\-]+)/', views.ItemView.as_view(), name='item'),
    url(r'^(?P<slug>[a-z\-]+)/', views.BrandView.as_view(), name='brand'),
]
