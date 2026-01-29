from rest_framework import serializers
from .models import (Project, SkillProgress, SkillLearned, Education, Logo, ProfilePicture, WelcomeNote,
                     MoreList, Experience)


class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None


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
    sketch = serializers.SerializerMethodField()
    original = serializers.SerializerMethodField()

    class Meta:
        model = ProfilePicture
        fields = '__all__'

    def get_sketch(self, obj):
        if obj.sketch:
            return obj.sketch.url
        return None

    def get_original(self, obj):
        if obj.original:
            return obj.original.url
        return None


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