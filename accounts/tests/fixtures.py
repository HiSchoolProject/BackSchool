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
"""
Define common fixtures of the accounts applications, that can be used for retrieving users and performing

common applications on groups.
"""
import logging

from django.contrib.auth.models import User


class UserFixture():
    """
    Allow to retrieve users having a specific status for testing purposes.

    Also provides helpers for user creation and management.
    """

    def __init__(self):
        """
        Ensure that the database we are working on has a registered super user and staff user.

        If not, create them.
        """
        self.superuser = User.objects.get_or_create(username='superuser', password='superuser',
                email='superuser@localhost', is_superuser=True)

        self.staffuser = User.objects.get_or_create(username='staffuser', password='staffuser',
                                  email='staffuser@localhost', is_staff=True)

    def createUser(self, username, email='default@localhost', first_name='default',
                   last_name='default', password='default', is_staff=False, is_superadmin=False):
        """Quickly create and save a user using the given informations."""
        user = User(username=username, password=password, email=email, is_staff=is_staff, is_superadmin=is_superadmin)
        user.save()
        return user
