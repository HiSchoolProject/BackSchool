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
"""Define the urls of the dispatcher application."""
import re

from django.apps import apps

from .dispatchers import APIDispatcher

# Get a list of the project applications
# Note that we could make this filter cleaner by moving it in an application dedicated to utils about
# applications management, and also by updating the signature of APIDispatcher.__init__ to handle AppConfig
# See #15
installed_applications = [app.name for app in list(apps.get_app_configs())
                          if re.match(r'^(core|extensions)', app.path) is not None]

app_name = 'dispatcher'

apis = APIDispatcher(installed_applications, [1])

urlpatterns = apis.urls
