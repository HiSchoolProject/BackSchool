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
from django.shortcuts import get_object_or_404
from django.views import generic

from ..forms.parts import PartAdminForm
from ..forms.parts import PartAddForm
from ..forms.parts import PartTeacherForm
from ..models import Course
from ..models import Part
from ..permissions import can_add_part
from ..permissions import can_edit_part
from ..permissions import can_add_sequence


class PartListView(LoginRequiredMixin, generic.ListView):
    model = Part


class PartDetailView(LoginRequiredMixin, generic.DetailView):
    model = Part

    def get_context_data(self, **kwargs):
        """
        Override the template context.

        Add a boolean to the template context in order to determine if the user is allowed to edit
        the current part.
        Also add a boolean that determines if the current user is allowed to add a new sequence to the part.
        """
        context = super(PartDetailView, self).get_context_data(**kwargs)
        context['can_edit_part'] = can_edit_part(self.request.user, self.object)
        context['can_add_sequence'] = can_add_sequence(self.request.user, self.object)
        return context


class PartAddView(UserPassesTestMixin, generic.CreateView):
    form_class = PartAddForm
    template_name = 'courses/part_form.html'

    def test_func(self):
        return can_add_part(self.request.user, Course.objects.get(pk=self.kwargs['course']))

    def form_valid(self, form):
        """When creating a new part, override the save process in order to attach the part to the current course."""
        part = form.save(commit=False)
        course = get_object_or_404(Course, pk=self.kwargs['course'])
        part.course = course
        part.full_clean()

        return super(PartAddView, self).form_valid(form)


class PartEditView(UserPassesTestMixin, generic.UpdateView):
    model = Part

    def get_form_class(self):
        """Choose the correct form to display depending on the user permissions."""
        if self.request.user.has_perm('courses.change_part'):
            return PartAdminForm
        else:
            return PartTeacherForm

    def test_func(self):
        """We allow edition only for users having the correct right, or the course referent."""
        return can_edit_part(self.request.user, self.get_object())


class PartDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Part
    permission_required = 'courses.delete_part'
