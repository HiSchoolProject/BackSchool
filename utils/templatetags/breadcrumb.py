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
from django import template

from ..models import Model

register = template.Library()


class BreadcrumbElement:
    def __init__(self, url, text):
        self.url = url
        self.text = text

    def __str__(self):
        return "{} ({})".format(self.text, self.url)


class BreadcrumbElementBuilder:
    def __init__(self, context):
        self.context = context

    def build(self):
        if self.context['object'] is not None:
            breadcrumb = self.build_from_objects(self.context['object'])
        else:
            breadcrumb = []

        return breadcrumb

    def build_from_objects(self, base_object):
        # It would be better to use a stack / queue at some point
        elements = []

        while (isinstance(base_object, Model)):
            elements.append(BreadcrumbElement(base_object.get_absolute_url(), base_object.__str__()))
            parent = base_object.get_parent_relation()
            if parent is None:
                break
            else:
                base_object = parent

        elements.reverse()
        return elements


@register.inclusion_tag('breadcrumb.html', takes_context=True)
def breadcrumb(context):
    """Generate a breadcrumb using the given context."""
    builder = BreadcrumbElementBuilder(context)
    return {'elements': builder.build()}
