from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Project, message
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib import messages
from django.urls import reverse
from .models import Main,About
# Create your views here.


def index(request):
    return render(request, 'pages/index.html',context = {"main":Main.objects.first()})


def about_us(request):
    return render(request, 'pages/about_us.html')


class ContactUsView(View):
    template_name = 'pages/contact.html'

    def get(self, request):
        return render(request, 'pages/contact.html', )

    def post(self, request):
        data = request.POST
        if data["name"] and data["email"] and data["phone"] and data["subject"] and data["message"]:
            message.objects.create(name=data["name"], email=data["email"],
                                   phone_number=data["phone"], subject=data["subject"], message=data["message"])
            messages.success(request, "Mesaj Başarıyla Oluşturuldu.")
            return redirect('/contact-us#main')
        else:
            messages.warning(request, "Mesaj Oluşturulamadı.")
            return redirect("contact")


class ProjectsListView(ListView):
    model = Project
    template_name = 'pages/projects.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deneme'] = "merhaba"
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'pages/single_project.html'
    context_object_name = 'project'
