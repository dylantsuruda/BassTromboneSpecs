from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect
from .models import Feedback
import requests

# Create your views here.

def index(request):
    if request.get_host() == "basstrombonespecs.herokuapp.com":
        return HttpResponsePermanentRedirect('https://www.basstrombonespecs.com')
    
    if not settings.DEBUG:  # Code that runs in production
        context = {
            'debug': settings.DEBUG,
            'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY,
        }
    else:  # Code that runs locally in development
        context = {
            'debug': settings.DEBUG,
        }

    if request.method == "POST":
        feedback = request.POST['feedback']
        feedback = feedback.strip()
        if len(feedback) != 0:
            if not settings.DEBUG:  # Code that runs in production
                # Verify reCAPTCHA
                recaptcha_response = request.POST['g-recaptcha-response']
                data = {
                    'secret': settings.RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response,
                }
                r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
                result = r.json()

                if result['success']:
                    Feedback.objects.create(feedback=feedback)
                    messages.success(request,
                        "Thanks for sending feedback! Your feedback is appreciated, and it will be looked over soon.")
                else:
                    messages.error(request,
                        "Your feedback was not submitted because it seems like you're a robot.")
            else:  # Code that runs locally in development
                Feedback.objects.create(feedback=feedback)
                messages.success(request,
                    "Thanks for sending feedback! Your feedback is appreciated, and it will be looked over soon.")

            return redirect('specs:index')
        else:
            messages.error(request, "Your feedback won't be submitted if it's empty.")
            return render(request, 'feedback/index.html', context)
    else:
        return render(request, 'feedback/index.html', context)
