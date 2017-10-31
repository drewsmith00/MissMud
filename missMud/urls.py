from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from profiles import views as profiles_views
from contact import views as contact_views
from checkout import views as checkout_views
from views import home, about

from clothing import views as clothing_views
from jewelry import views as jewelry_views
from pottery import views as pottery_views
from events import views as events_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^profile/$', profiles_views.profileView, name='profile'),
    url(r'^checkout/$', checkout_views.checkout, name='checkout'),
    url(r'^contact/$', contact_views.contact, name='contact'),

    url(r'^account/', include('allauth.urls')),
    url(r'^jewelry/', include('jewelry.urls', namespace='jewelry')),
    url(r'^pottery/', include('pottery.urls', namespace='pottery')),
    url(r'^clothing/', include('clothing.urls', namespace='clothing')),
    url(r'^events/', include('events.urls', namespace='events')),

    url(r'^clothing/', clothing_views.ClothingView.as_view(), name='clothing'),
    url(r'^events/', events_views.IndexView.as_view(), name='events'),
    url(r'^pottery/', pottery_views.PotteryView.as_view(), name='pottery'),
    url(r'^jewelry/', jewelry_views.JewelryView.as_view(), name='jewelry'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
