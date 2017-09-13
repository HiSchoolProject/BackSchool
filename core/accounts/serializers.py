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
"""Serializers for the accounts application models."""
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Account


class UserSerializer(serializers.ModelSerializer):
    """API endpoint for users management."""

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'groups', 'is_staff')


class GroupSerializer(serializers.ModelSerializer):
    """API endpoint for groups management."""

    class Meta:
        model = Group
        fields = ('pk', 'name')


class AccountSerializer(serializers.ModelSerializer):
    """API endpoint for account management."""

    user = UserSerializer()

    class Meta:
        model = Account
        fields = ('pk', 'user')
