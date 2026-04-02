from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Education, ContactMessage


def index(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    education = Education.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message_text = request.POST.get('message', '').strip()

        if name and email and message_text:
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message_text,
            )
            messages.success(request, 'Your message has been sent. Thank you!')
        else:
            messages.error(request, 'Please fill in all fields before submitting.')

        return redirect('index')

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'education': education,
    }
    return render(request, 'portfolio/index.html', context)
