from django.shortcuts import render,get_object_or_404
from django.db.models import Q  # New
from django.views import generic
from .models import Post

class PostList(generic.ListView):

    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3



class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    paginate_by = 1

def about(request):

	latests=Post.objects.all().order_by('-created_on')[:2]
	context = {
		'latests':latests
	}
	return render(request,'about.html', context)

def contact(request):

	latests=Post.objects.all().order_by('-created_on')[:2]
	context = {
		'latests':latests
	}
	return render(request,'contact.html', context)
