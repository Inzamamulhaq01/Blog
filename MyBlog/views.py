from django.contrib import messages
from django.contrib.auth.models import User
from sre_constants import SUCCESS
from django.contrib.auth import authenticate,login as login_auth,logout
from django.shortcuts import redirect, render,redirect
from django.http import Http404
from .models import Post,about,Comment
from MyBlog.forms import Contactform,CommentForm
from django.core.paginator import Paginator
import logging

# Create your views here.

def index(request):
    # check user login or not 
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        posts = Post.objects.all()
        # Paginator used to Show no of posts/page
        paginator = Paginator(posts,6)
        # recieve the current page number from url using get 
        page_no = request.GET.get('page')
        # based on the page recieved (ex 1) we get the page posts to the index html
        page = paginator.get_page(page_no)
        return render(request,'index.html',{'page':page})




def detail(request,slug):
    # check user login or not 
    if not request.user.is_authenticated:
        return redirect('login')
    # getting post by post id using model class
    
    try:
        post = Post.objects.get(slug=slug)
        other_posts = Post.objects.filter().exclude(pk=post.id)
        comments = Comment.objects.filter(post_id=post.id)
       
    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist!")
        
    
    return render(request,'detail.html',{'post':post , 'other_posts':other_posts,'comments':comments})



def contact(request):
    # check user login or not 
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = Contactform(request.POST)
        
        # values that are filled in the contact form
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
    
        if form.is_valid():    
            
            SUCCESS = 'Your Email Has Sent!'
            messages.success(request, 'Your Email Has Sent!')
            
            return render(request,'contact.html',{'form':form,'SUCCESS':SUCCESS})
        
           
            
        else:
            return render(request,'contact.html',{'form':form,'name':name,'email':email,'message':message})
        
    return render(request,'contact.html')

def aboutus(request):
    # check user login or not 
    if not request.user.is_authenticated:
        return redirect('login')
    
    # about content is object 
    about_content = about.objects.first().content
    # logger = logging.getLogger("test")
    # logger.debug(about_content)
    return render(request,'about.html',{'about_content':about_content})


def login(request):
    context = {"error":""}
    if request.method == 'POST':
        
        
        user = authenticate(username = request.POST['user'],password = request.POST['pass'])
        if user != None:
            login_auth(request,user)
            return redirect('index')
        else:
            context = {"error":"Invalid username or password"}
            return render(request,'login.html',context)
            
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def signup(request):
    context = {
        "error":""
    }
    if request.method == 'POST':
        user = request.POST['username']
        first = request.POST['firstname']
        last = request.POST['lastname']
        mail = request.POST['email']
        pass_word = request.POST['password']
        conformpassword = request.POST['confirm_password']
        
        user_name_check = User.objects.filter(username = request.POST['username'])
        verify_email = User.objects.filter(email = request.POST['email'])
        
        if len(user_name_check) > 0:
            context = {"error":"username already exists",'firstname':first,'lastname':last,'email':mail,'password':pass_word,'confirm_password':conformpassword}
            return render(request,'signup.html',context)
        
        elif len(verify_email) > 0:
            context = {"error":"email already exists",'username':user,'firstname':first,'lastname':last,'password':pass_word,'confirm_password':conformpassword}
            return render(request,'signup.html',context)
        
        
        
        else:
            pass_1 = request.POST['password']
            pass_2 = request.POST['confirm_password']
            if pass_1 == pass_2:
                
                new_user = User(username = request.POST['username'],first_name = request.POST['firstname'],
                                last_name = request.POST['lastname'],email = request.POST['email']
                                )
                new_user.set_password(pass_1)
                new_user.save()  # Save the user to the database
                
            
                
                return redirect('login')
            else:
               
                
                context = {'error':"Password Not Matched",'username':user,'firstname':first,'lastname':last,'email':mail}
                return render(request,'signup.html',context)
    
    return render(request,'signup.html',context)

def commentview(request,slug):
    # check user login or not 
    if not request.user.is_authenticated:
        return redirect('login')
    
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        # values that are filled in the contact form
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        
        if form.is_valid():    
            SUCCESS = 'Your Post Has Sent!'
    
        # Create a new Comment instance with the cleaned data from the form
            new_comment = Comment(
                name=name,
                email=email,
                message=message,
                post=Post.objects.get(slug=slug)  # Assuming you're linking the comment to a specific Post
            )
    
    # Save the new comment to the database
            new_comment.save()
            
            return redirect('detail', slug=slug)

            
            # return reverse
            # return render(request,'comment.html',{'form':form,'SUCCESS':SUCCESS})
        
           
            
        else:
           return render(request,'comment.html',{'form':form,'name':name,'email':email,'message':message})
        
    return render(request,'comment.html')
    
    
    