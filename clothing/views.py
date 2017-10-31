from django.views import generic
from models import Brand, Item


class ClothingView(generic.ListView):
    template_name = 'clothing/clothing.html'
    context_object_name = 'all_brands'
    brand = Brand.objects.all()
    queryset = brand

    def get_context_data(self, **kwargs):
        ctx = super(ClothingView, self).get_context_data(**kwargs)
        ctx['items'] = Item.objects.all()
        return ctx


class BrandView(generic.DetailView):
    template_name = 'clothing/brand.html'
    model = Brand

    def get_context_data(self, **kwargs):
        ctx = super(BrandView, self).get_context_data(**kwargs)
        ctx['items'] = Item.objects.all()
        return ctx


class ItemView(generic.DetailView):
    template_name = 'clothing/item.html'
    model = Item



