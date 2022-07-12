from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

from django.contrib.auth import get_user_model
User = get_user_model()

from braces.views import SelectRelatedMixin

from . import models
from . import forms
# Create your views here.

class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ("user", "group")

class UserPosts(generic.ListView):
    model = models.Post
    template_name = "posts/user_post_list.html"
