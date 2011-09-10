from django.contrib import admin
from IP_cases.models import *

class NoticeOfAppearenceAdmin(admin.ModelAdmin):
    pass
admin.site.register(notice_of_appearence,NoticeOfAppearenceAdmin)

class ITCcasesAdmin(admin.ModelAdmin):
    pass
admin.site.register(itc_cases,ITCcasesAdmin)

class DistrictCourtsandJudgesAdmin(admin.ModelAdmin):
    pass
admin.site.register(district_courts_and_judges,DistrictCourtsandJudgesAdmin)


