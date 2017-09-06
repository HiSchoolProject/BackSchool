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
from django.conf.urls import include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from rest_framework import routers

from .viewSets import AccountViewSet
from .viewSets import GroupViewSet
from .viewSets import UserViewSet

app_name = 'accounts'

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^api/', include(router.urls))
]
