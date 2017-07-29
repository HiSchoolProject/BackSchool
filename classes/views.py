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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .models import Group


class GroupListView(LoginRequiredMixin, generic.ListView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        context['can_add_group'] = self.request.user.has_perm('classes.add_group')
        return context


class GroupDetailView(LoginRequiredMixin, generic.DetailView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        context['can_edit_group'] = self.request.user.has_perm('classes.change_group')
        return context


class GroupAddView(PermissionRequiredMixin, generic.CreateView):
    model = Group
    permission_required = 'classes.add_group'
    fields = ['title']


class GroupEditView(PermissionRequiredMixin, generic.UpdateView):
    model = Group
    permission_required = 'classes.change_group'
    fields = ['title']


class GroupDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Group
    permission_required = 'classes.delete_group'

    def get_success_url(self):
        return reverse_lazy('classes:list_group')
