from __future__ import absolute_import

from django.conf.urls.defaults import *
from . import views as faq_views

urlpatterns = patterns('',
    url(regex = r'^$',
        view  = faq_views.TopicList.as_view(),
        name  = 'faq_topic_list',
    ),
    url(regex = r'^(?P<slug>[\w-]+)/$',
        view  = faq_views.TopicDetail.as_view(),
        name  = 'faq_topic_detail',
    ),
    url(regex = r'^(?P<topic_slug>[\w-]+)/(?P<slug>[\w-]+)/$',
        view  = faq_views.QuestionDetail.as_view(),
        name  = 'faq_question_detail',
    ),
)
