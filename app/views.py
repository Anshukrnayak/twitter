from django.shortcuts import render,redirect
from .models import PostThread
from django.views.generic.list import ListView
from .forms import TreadForm
from .models import PostThread
from django.views.generic import View


class Home_page(ListView):
 
    template_name='home/home.html'
    model=PostThread


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] =PostThread.objects.all()

        return context

class Post_new_thread(View):

    def get(self,request):

        form=TreadForm()

        return render(request,'home/post.html',{'form':form})
    

    def post(self,request):
        form=TreadForm(data=request.POST)

        if form.is_valid():
            user_field=form.save(commit=False)
            user_field.user=self.request.user
            user_field.save()

            return redirect('home')
        
        return render(request,'home/post.html',{'form':form})











    



