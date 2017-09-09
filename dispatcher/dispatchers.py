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
"""Declare the platform dispatchers used to transfer requests to their correct modules using the URL."""
from django.conf.urls import url


class Dispatcher():
    """
    Provide a generic definition of a dispatcher.

    A Dispatcher should be used to generate a list of django.urls.url() that corresponds to the state of the server.
    """

    def __init__(self, namespace):
        if namespace is None:
            raise ValueError('A namespace should be specified for the Dispatcher to work.')
        self.namespace = namespace

    def url(self):
        raise NotImplementedError


class ApplicationAPIDispatcher(Dispatcher):
    """
    Define a list of routes that can be used for a given application.

    """

    def __init__(self, namespace, application):
        if application is None:
            raise ValueError('
    def url(self):
        return ''
