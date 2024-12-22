from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse ,HttpResponseRedirect

# Create your views here.
def home(request):
    return render (request,"index.html")

# views.py

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to the 'thank_you' page after successful submission
    else:
        form = ContactForm()

    return render(request, 'contact_success.html', {'form': form})

def thank_you_view(request):
    return render(request, 'thank_you.html')

