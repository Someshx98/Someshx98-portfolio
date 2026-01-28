from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (Project, SkillProgress, SkillLearned, Education, Logo, ProfilePicture, WelcomeNote,
                     MoreList, Experience)
from .serializers import (ProjectSerializer, SkillProgressSerializer,
                          SkillLearnedSerializer,
                          LogoSerializer, ProfilePictureSerializer,
                          WelcomeNoteSerializer, MoreListSerializer,
                          ExperienceSerializer, EducationSerializer)

# Create your views here.

class ProjectsAPI(APIView):
    def get(self, request):
        data = Project.objects.all()
        serializer = ProjectSerializer(data, many=True)
        return Response(serializer.data)

class SkillProgressAPI(APIView):
    def get(self, request):
        data = SkillProgress.objects.all()
        serializer = SkillProgressSerializer(data, many=True)
        return Response(serializer.data)

class SkillLearnAPI(APIView):
    def get(self, request):
        data = SkillLearned.objects.all()
        serializer = SkillLearnedSerializer(data, many=True)
        return Response(serializer.data)

class EducationAPI(APIView):
    def get(self, request):
        data = Education.objects.all()
        serializer = EducationSerializer(data, many=True)
        return Response(serializer.data)

class LogoAPI(APIView):
    def get(self, request):
        data = Logo.objects.all()
        serializer = LogoSerializer(data, many=True)
        return Response(serializer.data)

class ProfilePictureAPI(APIView):
    def get(self, request):
        data = ProfilePicture.objects.all()
        serializer = ProfilePictureSerializer(data, many=True)
        return Response(serializer.data)

class WelcomeNoteAPI(APIView):
    def get(self, request):
        data = WelcomeNote.objects.all()
        serializer = WelcomeNoteSerializer(data, many=True)
        return Response(serializer.data)

class MoreListApi(APIView):
    def get(self, request):
        data = MoreList.objects.all()
        serializer = MoreListSerializer(data, many=True)
        return Response(serializer.data)

class ExperienceApi(APIView):
    def get(self, request):
        data = Experience.objects.all()
        serializer = ExperienceSerializer(data, many=True)
        return Response(serializer.data)

def index(request):
    return render(request, 'index.html')

def education(request):
    return render(request, 'education.html')

def experience(request):
    return render(request, 'experience.html')

def skills(request):
    return render(request, 'skills.html')

def more(request):
    return render(request, 'more.html')

def contact_me(request):
    return render(request, 'contactMe.html')