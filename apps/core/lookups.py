from selectable.base import ModelLookup
from selectable.registry import registry
from apps.core.models import Base, Log

__author__ = 'Nataliel Vasconcelos'


class BaseLookup(ModelLookup):
    model = Base
    search_fields = ('text__icontains', )


registry.register(BaseLookup)


class LogLookup(ModelLookup):
    model = Log
    search_fields = ('text__icontains', )


registry.register(LogLookup)