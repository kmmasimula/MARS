from django.contrib import admin

from .models import Team,User,MBTI,participatoryentity,bellbin,teamattributes,teamRank,teamQuality,teamHours,teamMBTI,teambellbin

# Register your models here.

admin.site.register(Team)
admin.site.register(User)
admin.site.register(participatoryentity)
admin.site.register(MBTI)
admin.site.register(bellbin)
admin.site.register(teamattributes)
admin.site.register(teamRank)
admin.site.register(teamQuality)
admin.site.register(teamHours)
admin.site.register(teamMBTI)
admin.site.register(teambellbin)
