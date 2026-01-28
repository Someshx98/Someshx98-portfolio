from django.contrib import admin
from .models import (Project, SkillProgress, SkillLearned, Education, Logo, ProfilePicture, WelcomeNote, MoreList,
                     Experience)

# Register your models here.

admin.site.register(Project)
admin.site.register(SkillProgress)
admin.site.register(SkillLearned)
admin.site.register(Education)
admin.site.register(Logo)
admin.site.register(ProfilePicture)
admin.site.register(WelcomeNote)
admin.site.register(MoreList)
admin.site.register(Experience)