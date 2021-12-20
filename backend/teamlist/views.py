from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView , UpdateView , ListView , DeleteView
from .forms import MemberForm
from .models import TeamMember
 
# Create your views here.

class CreateUserView(CreateView):
    form_class = MemberForm
    success_url = reverse_lazy('list')
    template_name = 'createuser.html'
    

class EditUserView(UpdateView):
    model = TeamMember
    form_class = MemberForm
    success_url = reverse_lazy('list')
    template_name = 'edituser.html'

class ListUserView(ListView):
    model = TeamMember
    template_name = 'listusers.html'

class DeleteUserView(DeleteView):
    model = TeamMember
    success_url = reverse_lazy('list')
    template_name = 'deleteuser.html'
    
