from django.shortcuts import render
from .models import ContactForm, Services, Blog
from .forms import ContactModelForm
import time

# Create your views here.
def frontpage(request):
    service = Services.objects.all()
    context = {
        'service': service
    }

    return render(request, 'frontpage.html', context)

    

def contact(request):
    form = ContactModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        time.sleep(3)
        form = ContactModelForm()

    context = {
        'form': form
    }
    
    return render(request, 'contact.html', context)


def hacemos(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog
        }

    return render(request, 'hacemos.html', context)
