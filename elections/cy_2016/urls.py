from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DistrictSelectorView.as_view(), name='district-selector'),
    url(r'^help/about$', views.HelpAboutView.as_view(), name='help-about')]
