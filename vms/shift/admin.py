# Django
from django.contrib import admin

# local Django
from shift.models import Report, Shift, VolunteerShift


class ShiftAdmin(admin.ModelAdmin):
    pass


admin.site.register(Shift, ShiftAdmin)


class VolunteerShiftAdmin(admin.ModelAdmin):
    pass


admin.site.register(VolunteerShift, VolunteerShiftAdmin)


class ReportAdmin(admin.ModelAdmin):
    pass


admin.site.register(Report, ReportAdmin)

