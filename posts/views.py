from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth import get_user_model
from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models,forms
from django.contrib import messages

User=get_user_model()
# Create your views here.
class PostList(SelectRelatedMixin,generic.ListView):
    model = models.Post
    select_related = ('user','group')

class UserPosts(generic.ListView):
    model=models.Post
    template_name = 'posts/user_post_list.html'


    def get_queryset(self):
        try:
            self.post_user=User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.Doesnotexist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['post_user']=self.post_user
        return context


class PostDetail(generic.DetailView,SelectRelatedMixin):
    model=models.Post
    select_related = ('post','group')

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(user__username_iexact=self.kwargs.get('username'))


class CreatePost(generic.CreateView,LoginRequiredMixin,SelectRelatedMixin):
    model = models.Post
    fields = ('message', 'group' )

    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(generic.DeleteView,SelectRelatedMixin,LoginRequiredMixin):
    model=models.Post
    select_related = ('user','post')
    success_url = reverse_lazy('posts:all')


    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)


    def delete(self, *args, **kwargs):
        messages.success(self.request,'Post deleted')
        return super().delete(*args,**kwargs)