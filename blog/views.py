from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .Data_AllByInput import ProfilefromGFinance

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_list.html', {'post': post})
    
def submit(request):
    ticker = request.POST['G_Ticker']
    datetime = request.POST['G_Datetime']
    speaker = request.POST['G_Speaker']
    dialin = request.POST['G_Dialin']
    passcode = request.POST['G_Passcode']
    baseurl = 'https://www.google.com/finance?q='
    url = baseurl + ticker
    ProfilefromGFinance(ticker, datetime, speaker, dialin, passcode, url)
    return render(request, 'blog/post_list.html')
    
