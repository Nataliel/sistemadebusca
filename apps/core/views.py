import json
import urllib2
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from apps.core.forms import BaseForm, BaseFilter, LogFilter

from apps.core.models import Base, Log


class LogListView(ListView):
    template_name = 'core/log-listagem.html'
    model = Log
    paginate_by = 500

    def get_context_data(self, **kwargs):
        context = super(LogListView, self).get_context_data(**kwargs)
        context['search'] = LogFilter()
        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        if 'q' in request.GET:
            self.object_list = self.object_list.filter(text__icontains=request.GET.get('q'))

        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)


class BaseListView(ListView):
    template_name = 'core/base-listagem.html'
    model = Base
    paginate_by = 500

    def get_context_data(self, **kwargs):
        context = super(BaseListView, self).get_context_data(**kwargs)
        context['search'] = BaseFilter()
        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        if 'q' in request.GET:
            self.object_list = self.object_list.filter(text__icontains=request.GET.get('q'))

        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)


class BaseCreateView(CreateView):
    model = Base
    form_class = BaseForm
    template_name = 'core/form.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, ('Salvo com sucesso!'))
        return redirect('home')


class BaseDeleteView(DeleteView):
    model = Base
    form_class = BaseForm
    success_url = '/'
    template_name = 'core/deletar-objetos.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.error(self.request, ('Deletado com sucesso!'))
        return HttpResponseRedirect(success_url)


class BaseUpdateView(UpdateView):
    model = Base
    form_class = BaseForm
    template_name = 'core/form.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, ('Alterado com sucesso!'))
        return redirect('home')