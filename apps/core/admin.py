from django.contrib import admin
from apps.core.models import Base
from apps.core.models import Log


admin.site.register(Base)
admin.site.register(Log)
