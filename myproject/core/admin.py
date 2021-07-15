from django.contrib import admin
from .models import ContactForm, Services, Blog

# Register your models here.
admin.site.register(ContactForm)
admin.site.register(Services)
admin.site.register(Blog)
