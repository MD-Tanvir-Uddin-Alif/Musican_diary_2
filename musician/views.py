from django.shortcuts import render,redirect
from .forms import AddMusician, SignUP
from .models import Musician

from django.views.generic import CreateView,UpdateView 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import messages
# Create your views here.

def add_musician(request):
    if request.method == 'POST':
        musician_form = AddMusician(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home_page')
    else:
        musician_form = AddMusician()
    return render(request,'musician.html',{'form' : musician_form})

class AdMusicanView(CreateView):
    model = Musician
    form_class = AddMusician
    template_name = 'musician.html'
    success_url = reverse_lazy('home_page')

def edit_musician(request,id):
    musician = Musician.objects.get(pk=id)
    musician_form = AddMusician(instance=musician)
    if request.method == 'POST':
        musician_form = AddMusician(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home_page')

    return render(request,'musician.html',{'form' : musician_form})


class EditMusicanView(UpdateView):
    model = Musician
    form_class = AddMusician
    template_name = 'musician.html'
    success_url = reverse_lazy('home_page')
    pk_url_kwarg = 'id'



def user_signup(request):
    if request.method == 'POST':
        form = SignUP(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('home_page')
    else:
        form = SignUP()
    return render(request,'login_&_logout.html',{'form':form, 'type': 'SignUP', 'type': 'SignUP'})



class UserLoginView(LoginView):
    template_name = 'login_&_logout.html'

    def get_success_url(self):
        return reverse_lazy('home_page')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context