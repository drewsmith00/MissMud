from django.views import generic
from models import Brand, Item


class PotteryView(generic.ListView):
    template_name = 'pottery/pottery.html'
    context_object_name = 'all_brands'
    queryset = Brand.objects.all()


class BrandView(generic.DetailView):
    template_name = 'pottery/brand.html'
    model = Brand

    def get_context_data(self, **kwargs):
        ctx = super(BrandView, self).get_context_data(**kwargs)
        ctx['items'] = Item.objects.all()
        return ctx


class ItemView(generic.DetailView):
    template_name = 'pottery/item.html'
    model = Item




