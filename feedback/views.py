from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback

# Create your views here.

def index(request):
    if request.method == "POST":
        feedback = request.POST['feedback']
        feedback = feedback.strip()
        if len(feedback) != 0:
            Feedback.objects.create(feedback=feedback)
            messages.success(request,
                "Thanks for sending feedback! Your feedback is appreciated, and it will be looked over soon.")
            return redirect('specs:index')
        else:
            return render(request, 'feedback/index.html')
    else:
        return render(request, 'feedback/index.html')
