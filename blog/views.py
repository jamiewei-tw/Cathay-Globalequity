from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_list.html', {'post': post})
    
def submit(request):
    A = request.POST['number1']
    B = request.POST['number2']
    C = A + B
    Test = "test"
    W = open(Test, "w")
    W.write(C)
    return render(request, 'blog/post_list.html',{C})
