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
"""This module defines the models of the Account application."""
from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    """
    Store every specific information about a platform member.

    This model interfaces with the standard Django User object.
    """

    user = models.OneToOneField(User, verbose_name='default_user', on_delete=models.CASCADE)

    def __str__(self):
        """Define the standard string representation of a user."""
        return '{} {} ({})'.format(self.user.first_name, self.user.last_name, self.user.username)

    class Meta:
        """Meta class definition."""

        permissions = (
            ('view_account', 'Can view the list of registered accounts'),
        )
