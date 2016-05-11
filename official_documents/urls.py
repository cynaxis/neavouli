from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^upload/election/(?P<election>[^/]+)/post/(?P<post_id>[^/]+)/$',
        views.CreateDocumentView.as_view(),
        name='upload_document_view'),
    url(r'^(?P<pk>\d+)/$',
        views.DocumentView.as_view(),
        name='uploaded_document_view'),
]
