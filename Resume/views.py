from django.shortcuts import render, redirect
from Protfillo.models import Portfillo, Category
from Resume.models import Biography, Educational, Skill, Service, Favorite, WorkExperince, SocialMedia
from django.views.generic import TemplateView
from Contact.models import InfoContact
from Contact.forms import ContactForm


class IndexPAge(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['biography'] = Biography.objects.first()
        context['skills'] = Skill.objects.all()
        context['services'] = Service.objects.all()
        context['favorites'] = Favorite.objects.all()
        context['workexperinces'] = WorkExperince.objects.all()
        context['educationals'] = Educational.objects.all()
        context['categories'] = Category.objects.all()
        context['portfillos'] = Portfillo.objects.all()
        context['contact_information'] = InfoContact.objects.first()
        context['contact_form'] = ContactForm()
        context['socialmedia'] = SocialMedia.objects.all()
        return context
    
