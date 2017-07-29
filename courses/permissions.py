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
"""Define the custom permissions tests related to the current application."""


def can_edit_course(user, course):
    """Define if the given user has the permission to edit a course."""
    return (user.has_perm('courses.change_course') or course.referent == user)


def can_add_part(user, course):
    """Define if the given user has the permission to add a new part inside of the given course."""
    return (user.has_perm('courses.add_part') or course.referent == user)


def can_edit_part(user, part):
    return (user.has_perm('courses.change_part') or part.course.referent == user)


def can_add_sequence(user, part):
    return (user.has_perm('courses.add_sequence') or part.course.referent == user)


def can_edit_sequence(user, sequence):
    return (user.has_perm('courses.change_sequence') or sequence.part.course.referent == user)

