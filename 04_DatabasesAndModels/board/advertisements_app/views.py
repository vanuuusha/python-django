from django.views.generic import ListView, DetailView
from .models import Advertisement
from .my_scripts import dollars


class AdverisementList(ListView):
    model = Advertisement
    template_name = 'advertisements_app/advertisement_list.html'
    context_object_name = 'advs'
    queryset = Advertisement.objects.all()[:30]


class AdvertisementDetail(DetailView):
    model = Advertisement
    template_name = 'advertisements_app/detail.html'
    context_object_name = 'adv'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views_count += 1  # TODO Обращайтесь к атрибуту self.object без kwargs
        self.object.save()
        # kwargs['object'].views_count = kwargs['object'].views_count + 1
        # kwargs['object'].save()
        context['new'] = dollars.in_dollars(kwargs['object'].price)
        return context

