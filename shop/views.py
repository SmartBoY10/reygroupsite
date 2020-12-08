from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages

from .models import *

def index(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['name'],  
                form.cleaned_data['email'], 
                'qurol.django99@gmail.com', 
                ['qurol.abdujalilov99@gmail.com'], 
                fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = ContactForm()

    about_us = About.objects.all()
    categories = Category.objects.all()
    honey = Product.objects.filter(category=1)
    mountain = Product.objects.filter(category=2)
    another = Product.objects.filter(category=4)
    shops = Shops.objects.all()
    context = {
        'honey': honey,
        'mountain': mountain,
        'another': another,
        'about_us': about_us,
        'categories': categories,
        'shops': shops,
        "form": form,
    }
    return render(request, template_name='shop/index.html', context=context)


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             mail = send_mail(
#                 form.cleaned_data['name'], 
#                 form.cleaned_data['email'],
#                 form.cleaned_data['number'],
#                 form.cleaned_data['content'], 
#                 'qurol.django@gmail.com', 
#                 ['qurol.abdujalilov99@gmail.com'], 
#                 fail_silently=False
#                 )
#             if mail:
#                 messages.success(request, 'Письмо отправлено')
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Ошибка отправки')
#         else:
#             messages.error(request, 'Ошибка валидации')
#     else:
#         form = ContactForm()
#     return render(request, 'shop/index.html', {"form": form})


# def get_category(request, category_id):
#     products = Product.objects.filter(category_id=category_id)
#     categories = Category.objects.all()
#     current_category = Category.objects.get(pk=category_id)
#     context = {
#         'products': products,
#         'categories': categories,
#         'current_category': current_category,
#     }
#     return render(request, template_name='shop/by_category.html', context=context)




    

#def about(request):
    #about_us = About.objects.all()
    #context = {
    #    'about_us': about_us
    #}
    #return render(request, template_name='shop/index.html', context=context)

