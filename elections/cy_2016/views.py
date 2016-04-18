from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, TemplateView

from candidates.views.mixins import ContributorsMixin

from .forms import DistrictForm
from ..models import Election


class DistrictSelectorView(ContributorsMixin, FormView):
    template_name = 'cy_2016/frontpage.html'
    form_class = DistrictForm

    @method_decorator(cache_control(max_age=(60 * 10)))
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        area_id = form.cleaned_data['district']
        return HttpResponseRedirect(
            reverse('areas-view',
                    kwargs={'type_and_area_ids': 'O06-{}'.format(area_id)}
                    ))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
           'top_users': self.get_leaderboards()[1]['rows'][:8],
           'recent_actions': self.get_recent_changes_queryset()[:5],
           'election_data': Election.objects.current().by_date().last()
           })
        return context
