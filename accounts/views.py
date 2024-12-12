from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import ProfileEditForm

class HomeView(TemplateView):
   template_name = "account/home.html"

class ProfileEditView(LoginRequiredMixin, UpdateView):
   template_name = "account/edit_profile.html"
   model = CustomUser
   form_class = ProfileEditForm
   success_url = "/accounts/edit_profile/"
   def get_object(self):
       return self.request.user