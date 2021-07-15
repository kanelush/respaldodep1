from django.shortcuts import render
from .models import ContactForm
from .forms import ContactModelForm
import time

# Create your views here.
def frontpage(request):
    return render(request, 'frontpage.html')


def contact(request):
    form = ContactModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        time.sleep(2)
        form = ContactModelForm()

    context = {
        'form': form
    }
    
    return render(request, 'contact.html', context)

def hacemos(request):
    return render(request, 'hacemos.html')