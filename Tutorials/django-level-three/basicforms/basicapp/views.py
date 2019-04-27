from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    my_form = forms.Form

    if request.method == 'POST':
        my_form = forms.Form(request.POST)

        if my_form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: " + my_form.cleaned_data['name'])
            print("EMAIL: " + my_form.cleaned_data['email'])
            print("TEXT: " + my_form.cleaned_data['text'])

    return render(request,'basicapp/form_page.html',{'form':my_form})
