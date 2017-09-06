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
"""This module contains the models definition of the Courses application."""
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from utils.models import Model


class Course(Model):
    """
    Store the available courses on the platform.

    A course is defined by a user (the referent of the course), a title and a description.
    It can also contain multiple parts that can then be subdivised into multiple sequences.
    """

    referent = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField('Title', max_length=255, help_text='The course title should not exceed 255 characters.')

    description = models.TextField('Description', blank=True)

    def get_absolute_url(self):
        """Define the URL that should be returned when a course is saved."""
        return reverse('courses:detail_course', kwargs={'pk': self.pk})

    def can_edit(self, user):
        """Define if the given user has the permission to edit the current course."""
        return (user.has_perm('courses.change_course') or self.referent == user)

    def can_add_part(self, user):
        """Define if the given user has the permission to add a new part inside of the given course."""
        return (user.has_perm('courses.add_part') or self.referent == user)

    def __str__(self):
        """Define the standard string representation of a course."""
        return '{} ({} {})'.format(self.title, self.referent.first_name, self.referent.last_name)


class Part(Model):
    """Define a part of a course."""

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    title = models.CharField('Title', max_length=255)

    description = models.TextField('Description', blank=True)

    """
    Define the position of the part in the course parts.

    Currently, no specific validation is done on the field, but if needed, a custom validator could be implemented
    in order to check for position uniqueness in the parts of a specific course.
    """
    position = models.IntegerField('Position', blank=True, default=0)

    def get_absolute_url(self):
        return reverse('courses:detail_part', kwargs={'pk': self.pk})

    def get_parent_relation(self):
        return self.course

    def can_edit(self, user):
        """Define if the given user has the permission to edit the current part."""
        return (user.has_perm('courses.change_part') or self.course.referent == user)

    def can_add_sequence(self, user):
        """Define if the given user has the permission to add a new sequence to the current part."""
        return (user.has_perm('courses.add_sequence') or self.course.referent == user)

    def __str__(self):
        """Define the standard string representation of a course part."""
        return '#{}: {} ({})'.format(self.position, self.title, self.course.title)


class Sequence(Model):
    """Define a sequence of a part."""

    part = models.ForeignKey(Part, on_delete=models.CASCADE)

    title = models.CharField('Title', max_length=255)

    description = models.TextField('Description', blank=True)

    """As in the Part model, we use an integer to indicate the position of the sequence in the part."""
    position = models.IntegerField('Position', blank=True, default=0)

    def get_absolute_url(self):
        return reverse('courses:detail_sequence', kwargs={'pk': self.pk})

    def get_parent_relation(self):
        return self.part

    def can_edit_sequence(self, user):
        """Define if the given user has the permission to edit the current sequence."""
        return (user.has_perm('courses.change_sequence') or self.part.course.referent == user)

    def __str__(self):
        """Define the standard string representation of a sequence."""
        return '#{}: {} ({} / #{}: {})'.format(self.position, self.title, self.part.course.title, self.part.position,
                                               self.part.title)


class Session(Model):
    """A session of a course is a new iteration of this course."""

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    start_date = models.DateField('Start date')

    def __str__(self):
        """Define the standard string representation of a session."""
        return '{} ({})'.format(self.course.title, self.start_date)


class Subscription(Model):
    """Represents the membership of a user and a course."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        """Define the standard string representation of a membership."""
        return '{} {} / {}'.format(self.user.first_name, self.user.last_name, self.session.course.title)
