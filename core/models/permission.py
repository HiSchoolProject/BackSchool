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
"""Define common project permissions."""
import types


class ModelPermission:
    """Uses a dict to describe an extended set of permissions about a given model."""

    FALSE = 0
    TRUE = 1
    INHERIT = 2

    ADD = 'add'
    CHANGE = 'change'
    DELETE = 'delete'

    default_permissions = {
            'model': {
                'add': ModelPermission.TRUE,
                'change': ModelPermission.TRUE,
                'delete': ModelPermission.TRUE}}

    permissions = {}

    def _evaluate_permission(self, permission, user, obj=None):
        if isinstance(permission, PermissionValue):
            return permission
        elif isinstance(permission, types.LambdaType):
            arguments = (user if obj is None else (user, obj))
            return permission(arguments)
        else:
            raise AttributeError('[{}] property in [{}] is not a boolean or a lambda expression'
                    .format(permission, self.permissions))

    def _get_permission(self, permission, user, obj=None):
        if user is None:
            return False

        if obj is None:
            return (self._evaluate_permission(self.permissions[PermissionScope.MODEL][permission])
                    is PermissionValue.ALLOW)
        else:
            #XXX
            return (self._evaluate_permission(self.permissions[PermissionScope.OBJECT][permission])
                    is PermissionValue.ALLOW)

    def can_view(self, user, obj=None):
        pass

    def can_change(self, user, obj=None, field=None):
        pass

    def can_add(self, user, obj=None):
        pass

    def can_delete(self, user, obj=None):
        pass

    def get_editable_fields(self, user, obj):
        pass

class PermissionValue(enum):
    ALLOW = 1
    DENY = 0
    INHERIT = 2

class PermissionType(enum):
    VIEW = 'view'
    ADD = 'add'
    CHANGE = 'change'
    DELETE = 'delete'

class PermissionScope(enum)
    MODEL = 'model'
    OBJECT = 'object'
    FIELD = 'field'
