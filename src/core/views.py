from keyword import kwlist

from django.shortcuts import get_object_or_404,render,redirect,aget_list_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Profile,Post,Comment,Follow
from .forms import ProfileForm,PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

""" All the functionalities of Profile management. """

class ProfileCreateView(LoginRequiredMixin, generic.CreateView):
   template_name = 'home/register-profile.html'
   model = Profile
   form_class = ProfileForm
   
   def form_valid(self, form):
      form.instance.user=self.request.user
      return super().form_valid(form)

   def get_success_url(self):
      return reverse_lazy('profile')


class ProfileView(LoginRequiredMixin,generic.View):
   def get(self,request):

      profile=get_object_or_404(Profile,user=self.request.user)
      posts=Post.objects.filter(user=request.user)

      context={
         'profile':profile,
         'posts':posts
      }
      return render(request,'home/profile.html',context)


class ProfileUpdateView(LoginRequiredMixin,generic.View):
   def get(self, request):
      instance = Profile.objects.get(user=request.user)
      form = ProfileForm(instance=instance)
      return render(request, 'home/profile-update.html', {'form': form})

   def post(self, request):
      instance = get_object_or_404(Profile, user=request.user)
      form = ProfileForm(instance=instance)  # Error occurs here or in get
      if form.is_valid():
         form.save()
         return redirect('home')
      return render(request, 'home/profile-update.html', {'form': form})



class ProfileDeleteView(LoginRequiredMixin,generic.DeleteView):
   form_class = ProfileForm
   model = Profile
   template_name = 'home/profile-delete'

"""
 User post management 
"""

class PostCreateView(LoginRequiredMixin,generic.View):

   def post(self,request):
      form=PostForm(request.POST,request.FILES)
      if form.is_valid():
         post=form.save(commit=False)
         post.user=self.request.user
         post.save()
         return redirect('home')
      print(form.errors)

      return render(request,'home/post.html',{'form':form})

   def get(self,request):
      form=PostForm()
      return render(request,'home/post.html',{'form':form})

class PostListView(LoginRequiredMixin,generic.ListView):
   template_name = 'home/index.html'
   model = Post
   context_object_name = 'posts'

   def get_queryset(self):
      return Post.objects.select_related('user').order_by('-created_at')


   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['profile'] = Profile.objects.get(user=self.request.user)
      context['form'] = PostForm()
      return context


class PostDetailView(LoginRequiredMixin, generic.View):

   def get(self, request, *args, **kwargs):
      post = get_object_or_404(Post, id=kwargs['pk'])
      form = CommentForm()
      return render(request, 'home/post-detail.html', {'post': post, 'form': form})

   def post(self, request, *args, **kwargs):
      post = get_object_or_404(Post, id=kwargs['pk'])
      form = CommentForm(request.POST)

      if form.is_valid():
         comment = form.save(commit=False)
         comment.user = request.user
         comment.post = post
         comment.save()
         return redirect('post_detail', pk=post.pk)  # Better UX than redirecting to home

      return render(request, 'home/post-detail.html', {'form': form, 'post': post})


class PostUpdateView(LoginRequiredMixin,generic.UpdateView):
   template_name = 'home/post-update.html'
   model = Post
   form_class = PostForm

   success_url = reverse_lazy('home')

class PostDeleteView(LoginRequiredMixin,generic.DeleteView):
   template_name = 'home/post-delete.html'
   model = Post
   success_url = reverse_lazy('home')


"""
   Liking and commenting functionalities :   
"""

@login_required
def liking_post(request,*args,**kwargs):
   user=request.user
   post=get_object_or_404(Post,id=kwargs['pk'])

   if user in post.likes.all():
      post.likes.remove(user)
   else:
      post.likes.add(user)

   return redirect('home')