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
from django.conf.urls import url

from .views import GroupListView
from .views import GroupDetailView
from .views import GroupAddView
from .views import GroupEditView
from .views import GroupDeleteView


app_name = 'classes'

urlpatterns = [
    url(r'^group/$', GroupListView.as_view(), name='list_group'),
    url(r'^group/(?P<pk>[0-9]+)/$', GroupDetailView.as_view(), name='detail_group'),
    url(r'^group/add/$', GroupAddView.as_view(), name='add_group'),
    url(r'^group/edit/(?P<pk>[0-9]+)/$', GroupEditView.as_view(), name='edit_group'),
    url(r'^group/delete/(?P<pk>[0-9]+)/$', GroupDeleteView.as_view(), name='delete_group'),
]
