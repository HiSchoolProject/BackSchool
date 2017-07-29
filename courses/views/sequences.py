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
from django.shortcuts import get_object_or_404
from django.views import generic

from ..forms.sequences import SequenceAdminForm
from ..forms.sequences import SequenceAddForm
from ..forms.sequences import SequenceTeacherForm
from ..models import Part
from ..models import Sequence
from ..permissions import can_add_sequence
from ..permissions import can_edit_sequence


class SequenceListView(LoginRequiredMixin, generic.ListView):
    model = Sequence


class SequenceDetailView(LoginRequiredMixin, generic.DetailView):
    model = Sequence

    def get_context_data(self, **kwargs):
        context = super(SequenceDetailView, self).get_context_data(**kwargs)
        context['can_edit_sequence'] = can_edit_sequence(self.request.user, self.object)
        return context


class SequenceAddView(UserPassesTestMixin, generic.CreateView):
    form_class = SequenceAddForm
    template_name = 'courses/sequence_form.html'

    def test_func(self):
        return can_add_sequence(self.request.user, Part.objects.get(pk=self.kwargs['part']))

    def form_valid(self, form):
        """When creating a new sequence, override the save process in order to attach the part to the current part."""
        sequence = form.save(commit=False)
        part = get_object_or_404(Part, pk=self.kwargs['part'])
        sequence.part = part
        sequence.full_clean()

        return super(SequenceAddView, self).form_valid(form)


class SequenceEditView(UserPassesTestMixin, generic.UpdateView):
    model = Sequence

    def get_form_class(self):
        """Choose the correct form to display depending on the user permissions."""
        if self.request.user.has_perm('courses.change_sequence'):
            return SequenceAdminForm
        else:
            return SequenceTeacherForm

    def test_func(self):
        """We allow edition only for users having the correct right, or the course referent."""
        return can_edit_sequence(self.request.user, self.get_object())


class SequenceDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Sequence
    permission_required = 'courses.delete_sequence'

    def get_success_url(self):
        return reverse_lazy('courses:detail_part', kwargs={'pk': self.object.part.id})
