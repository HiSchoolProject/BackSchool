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
from django.db import models


class Model(models.Model):

    add_date = models.DateTimeField('Date added', auto_now_add=True)

    last_modified = models.DateTimeField('Last update', auto_now=True)

    def get_parent_relation(self):
        """
        Create a hierarchy between the model elements.

        If None is returned, the current element is considered as a root element and should be bound to the home
        page of the platform.
        """
        return None

    class Meta:
        abstract = True
