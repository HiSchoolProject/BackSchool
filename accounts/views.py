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
"""Those are the views used for accounts management."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.views import generic

from .forms import AccountForm
from .models import Account


class AccountListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'accounts.view_account'
    model = Account


class AccountDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'accounts.view_account'
    model = Account

    def get_context_data(self, **kwargs):
        """Add a boolean to context in order to display the "edit accont" link."""
        context = super(AccountDetailView, self).get_context_data(**kwargs)
        context['can_edit_account'] = self.request.user.has_perm('accounts.change_account')
        return context


class AccountEditView(PermissionRequiredMixin, generic.UpdateView):
    form_class = AccountForm
    model = User
    permission_required = 'accounts.change_account'
    template_name = 'accounts/account_form.html'


class ProfileView(LoginRequiredMixin, generic.DetailView):
    model = Account

    def get_object(self):
        return self.request.user.account
