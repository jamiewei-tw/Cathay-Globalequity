from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .Data_InputTest import Inputtest


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_list.html', {'post': post})
    
def submit(request):
    
    Test_Result = ""
    
    company = request.POST['G_Company']
    ticker = request.POST['G_Ticker']
    datetime = request.POST['G_Datetime']
    speaker = request.POST['G_Speaker']
    Test_Result, language, description, title = Inputtest(company, ticker, datetime, speaker)
    
    if Test_Result == "Success" or Test_Result == "AHJ":
        return render(request, 'blog/result.html', locals())
        
    elif Test_Result == "AHJ Input Error":
        return render(request, 'blog/InputErrorAHJ.html', locals())
    
    else:
        return render(request, 'blog/InputError.html', locals())
        
    

