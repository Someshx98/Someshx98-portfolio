from django.urls import path
from .views import (ProjectsAPI, SkillProgressAPI,SkillLearnAPI,  EducationAPI,
                    LogoAPI, ProfilePictureAPI,
                    WelcomeNoteAPI, MoreListApi, ExperienceApi)
urlpatterns = [
    path('projects/', ProjectsAPI.as_view()),
    path('skillsprogress/', SkillProgressAPI.as_view()),
    path('skillslearned/', SkillLearnAPI.as_view()),
    path('education/', EducationAPI.as_view()),
    path('logo/', LogoAPI.as_view()),
    path('profilepicture/', ProfilePictureAPI.as_view()),
    path('welcomenote/', WelcomeNoteAPI.as_view()),
    path('morelist/', MoreListApi.as_view()),
    path('experience/', ExperienceApi.as_view()),
]