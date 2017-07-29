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
from django.forms import ModelForm

from ..models import Part


class PartAdminForm(ModelForm):
    class Meta:
        model = Part
        fields = ['course', 'title', 'description']


class PartTeacherForm(ModelForm):
    class Meta:
        model = Part
        fields = ['title', 'description']


"""The form used when creating a new part is currently the same as the PartTeacherForm."""
class PartAddForm(PartTeacherForm): {}
