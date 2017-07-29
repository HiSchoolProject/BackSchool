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
"""Register the models to the administration interface."""
from django.contrib import admin

from .models import Course
from .models import Part
from .models import Sequence
from .models import Session
from .models import Subscription

''' Allow the courses and its parts and sequences to be edited through the admin interface '''
admin.site.register(Course)
admin.site.register(Part)
admin.site.register(Sequence)
admin.site.register(Session)
admin.site.register(Subscription)
