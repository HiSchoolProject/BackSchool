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
"""HiSchool! URL Configuration."""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token

"""
Redirect every API call the dispatcher application that is responsible for forwarding API queries to the correct
application

Non-api calls are relayed to a displayer application that injects the URL into the client template
"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', obtain_jwt_token),
    url(r'^api/', include('core.dispatcher.urls')),
]
