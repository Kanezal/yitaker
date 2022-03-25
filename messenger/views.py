from .models import Message
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

'''
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return  dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
'''

def simple(request):
    has_errors = False

    if request.method == 'POST': 
        f = MessageForm(request.POST)
        if f.is_valid():
            new_message = Message(user_sender = request.user,
            text = f.cleaned_data['text']
             )
            new_message.save()

        else:
            has_errors = True
    else:
        f = MessageForm()

    #page = int(request.GET.get('page') if request.GET.get('page') != None else 1)
    #all_messages = Message.objects.order_by('-datetime')[(page - 1) * 10:(page - 1) * 10 + 10]
    ctx = {
        'messages' : new_message,
        'form' : f,
        'has_errors': has_errors
        }

    return render(request, 'new.html', context = ctx)

    