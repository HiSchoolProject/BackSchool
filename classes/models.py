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
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Group(models.Model):
    """
    Store a group of students in a class.

    Note that this model is unrelated to django.contrib.auth.models.Group
    """

    title = models.CharField('Title', max_length=255)

    students = models.ManyToManyField(User)

    def get_absolute_url(self):
        """Define the URL that should be returned when a group is saved."""
        return reverse('classes:detail_group', kwargs={'pk': self.pk})

    def __str__(self):
        """Define the standard string representation of a group."""
        return '{} ({})'.format(self.title, self.students)
