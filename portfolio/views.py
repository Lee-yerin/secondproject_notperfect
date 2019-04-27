from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Person
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Person.objects
    return render (request, 'portfolio/home.html', {'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'portfolio/detail.html',{'post': post_detail})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_data = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id = post.pk)
    else:
        form = PostForm()
        return render(request, 'portfolio/new.html',{'form':form})