from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import *


admin.site.register(Career, ImportExportModelAdmin)
admin.site.register(Matter, ImportExportModelAdmin)
admin.site.register(Classroom, ImportExportModelAdmin)
admin.site.register(Course, ImportExportModelAdmin)
admin.site.register(Branch, ImportExportModelAdmin)
