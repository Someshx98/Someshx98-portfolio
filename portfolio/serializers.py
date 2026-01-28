from rest_framework import serializers
from .models import (Project, SkillProgress, SkillLearned, Education, Logo, ProfilePicture, WelcomeNote,
                     MoreList, Experience)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class SkillProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillProgress
        fields = '__all__'

class SkillLearnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillLearned
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'

class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = '__all__'

class WelcomeNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomeNote
        fields = '__all__'

class MoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoreList
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'