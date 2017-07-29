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
"""Define the urls of the Accounts application."""
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import AccountDetailView
from .views import AccountEditView
from .views import AccountListView

from .views import ProfileView

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^$', AccountListView.as_view(), name='list_account'),
    url(r'^(?P<pk>[0-9]+)/$', AccountDetailView.as_view(), name='detail_account'),
    url(r'^edit/(?P<pk>[0-9]+)/$', AccountEditView.as_view(), name='edit_account'),

    url(r'^profile/$', ProfileView.as_view(), name='profile')
]
