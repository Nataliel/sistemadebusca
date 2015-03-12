from django import forms
from selectable.forms import AutoCompleteWidget
from apps.core.lookups import BaseLookup, LogLookup

from apps.core.models import Base

__author__ = 'Nataliel Vasconcelos'


class BaseForm(forms.ModelForm):

    class Meta:
        model = Base


class BaseFilter(forms.Form):
    q = forms.CharField(label='Busca Base', widget=AutoCompleteWidget(BaseLookup), required=False,)


class LogFilter(forms.Form):
    q = forms.CharField(label='Busca Log', widget=AutoCompleteWidget(LogLookup), required=False,)