from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.views.decorators.http import require_POST


@require_POST
def contact_me(request):
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        name = contact_form.cleaned_data.get('name')
        email = contact_form.cleaned_data.get('email')
        text = contact_form.cleaned_data.get('text')
        subject = 'Email Form User In Personal Website'
        context = {
            'name': name,
            'email': email,
            'text': text
        }
        message = get_template('shared/component/contact/contact_email_form.html').render(context)
        send_mail(subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=[settings.ADMIN_EMAIL])
        return redirect('home_page')
    
    return redirect('home_page')