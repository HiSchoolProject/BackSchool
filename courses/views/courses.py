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
"""Defines the views of the application."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from ..forms.courses import CourseAdminForm
from ..forms.courses import CourseTeacherForm
from ..models import Course
from ..permissions import can_edit_course
from ..permissions import can_add_part


class CourseListView(LoginRequiredMixin, generic.ListView):
    """List the available courses."""

    model = Course

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['can_add_course'] = self.request.user.has_perm('courses:add_course')
        return context


class CourseDetailView(LoginRequiredMixin, generic.DetailView):
    """Shows the details of a given course."""

    model = Course

    def get_context_data(self, **kwargs):
        """
        Override the template context.

        Add a boolean to the template context in order to determine if the user is allowed to edit
        the current course.
        """
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['can_edit_course'] = can_edit_course(self.request.user, self.object)
        context['can_add_part'] = can_add_part(self.request.user, self.object)
        return context


class CourseAddView(PermissionRequiredMixin, generic.CreateView):
    """Add a new course."""

    form_class = CourseAdminForm
    permission_required = 'courses.add_course'
    template_name = 'courses/course_form.html'


class CourseEditView(UserPassesTestMixin, generic.UpdateView):
    """Edit a given course."""

    model = Course

    def get_form_class(self):
        """Choose the correct form to display depending on the user permissions."""
        if self.request.user.has_perm('courses.change_course'):
            return CourseAdminForm
        else:
            return CourseTeacherForm

    def test_func(self):
        """We allow edition only for users having the correct right, or the course referent."""
        return can_edit_course(self.request.user, self.get_object())


class CourseDeleteView(PermissionRequiredMixin, generic.DeleteView):
    """Delete a course."""

    model = Course
    permission_required = 'courses.delete_course'
    success_url = reverse_lazy('courses:list_course')
