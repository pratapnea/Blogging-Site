from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse


# Create your views here.
def home(request):
	# return HttpResponse('<h1>Blog Home</h1>')
	context = {
		# Post.objects.all() fetch all data from table Post
		'posts': Post.objects.all(),
	}
	return render(request, 'blog/home.html', context)


def about(request):
	# return HttpResponse('<h1>Blog About</h1>')
	return render(request, 'blog/about.html', {'title': 'About'})
