from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixin import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from groups.models import Group,GroupMember
from django.contrib import messages
# Create your views here.

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroup(generic.ListView):
    model = Group

class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs = {"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug = self.kwargs.get("slug"))

        try:
            GroupMember.obejcts.create(user = self.request.user, group = group)
        except IntegrityError:
            messages.warning(self.request, "Warning! Already a member!")
        else:
            message.success(self.request, "Yay! You are now a member!")

        return super().get(request, *args, **kwargs)

class LeaveGroup():
    pass
