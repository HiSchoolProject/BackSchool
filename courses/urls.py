# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 The HiSchool! Project
#
# This file is part of HiSchool!.
#
# HiSchool! is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HiSchool! is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with HiSchool!.  If not, see <http://www.gnu.org/licenses/>.
"""Define the urls of the Course application."""
from django.conf.urls import url

from .views.courses import CourseListView
from .views.courses import CourseDetailView
from .views.courses import CourseAddView
from .views.courses import CourseEditView
from .views.courses import CourseDeleteView

from .views.parts import PartDetailView
from .views.parts import PartAddView
from .views.parts import PartEditView
from .views.parts import PartDeleteView

from .views.sequences import SequenceDetailView
from .views.sequences import SequenceAddView
from .views.sequences import SequenceEditView
from .views.sequences import SequenceDeleteView


app_name = 'courses'

urlpatterns = [
    url(r'^$', CourseListView.as_view(), name='list_course'),
    url(r'^(?P<pk>[0-9]+)/$', CourseDetailView.as_view(), name='detail_course'),
    url(r'^add/$', CourseAddView.as_view(), name='add_course'),
    url(r'^edit/(?P<pk>[0-9]+)/$', CourseEditView.as_view(), name='edit_course'),
    url(r'^delete/(?P<pk>[0-9]+)/$', CourseDeleteView.as_view(), name='delete_course'),

    url(r'^part/(?P<pk>[0-9]+)/$', PartDetailView.as_view(), name='detail_part'),
    url(r'^part/add/(?P<course>[0-9]+)/$', PartAddView.as_view(), name='add_part'),
    url(r'^part/edit/(?P<pk>[0-9]+)/$', PartEditView.as_view(), name='edit_part'),
    url(r'^part/delete/(?P<pk>[0-9]+)/$', PartDeleteView.as_view(), name='delete_part'),

    url(r'^sequence/(?P<pk>[0-9]+)/$', SequenceDetailView.as_view(), name='detail_sequence'),
    url(r'^sequence/add/(?P<part>[0-9]+)/$', SequenceAddView.as_view(), name='add_sequence'),
    url(r'^sequence/edit/(?P<pk>[0-9]+)/$', SequenceEditView.as_view(), name='edit_sequence'),
    url(r'^sequence/delete/(?P<pk>[0-9]+)/$', SequenceDeleteView.as_view(), name='delete_sequence')
]
