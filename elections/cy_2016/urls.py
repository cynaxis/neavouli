
from django.conf.urls import url
from django.views.generic import TemplateView

from candidates.views.help import HelpAboutView, HelpApiView
from candidates.views.parties import PartyDetailView
from .views import DistrictSelectorView

urlpatterns = [
    url(r'^$', DistrictSelectorView.as_view(), name='district-selector'),
    url(r'^help/about',
        HelpAboutView.as_view(template_name='cy_2016/about.html'),
        name='help-about'),
    url(r'^help/api',
        HelpApiView.as_view(template_name='cy_2016/api.html'),
        name='help-api'),
    url(r'^help/contact',
        TemplateView.as_view(template_name='cy_2016/contact.html'),
        name='help-contact'),
    url(r'^election/(?P<election>[^/]+)/party/(?P<organization_id>[^/]+)/(?P<ignored_slug>.*)$',
        PartyDetailView.as_view(template_name='cy_2016/party.html'),
        name='party'
        ),
    ]
