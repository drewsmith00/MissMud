from models import Item, Brand
from django.views import generic


class JewelryView(generic.ListView):
    model = Brand
    template_name = 'jewelry/jewelry.html'
    context_object_name = 'all_brands'


class BrandView(generic.DetailView):
    model = Brand
    template_name = 'jewelry/brand.html'

    def get_context_data(self, **kwargs):
        ctx = super(BrandView, self).get_context_data(**kwargs)
        ctx['items'] = Item.objects.all()
        return ctx


class ItemView(generic.DetailView):
    model = Item
    template_name = 'jewelry/item.html'
