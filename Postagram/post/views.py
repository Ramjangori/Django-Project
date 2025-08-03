from django.shortcuts import render
from .models import post
from .forms import postform , UserRegistrationForm
from django.shortcuts import get_object_or_404 , redirect 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.
def post_list(request):
    posts = post.objects.all().order_by('-created_at')  # '-' means descending order
    return render(request, 'index.html', {'posts': posts})
@login_required
def create_post(request):
    if request.method == "POST":
      form = postform(request.POST , request.FILES)
      if form.is_valid():
        post = form.save(commit=False)
        post.User = request.user
        post.save()
        return redirect('post-list')
      
    else:
        form = postform()
        return render(request , 'Post_form.html' , {'form': form} )




# def edit_post(request, post_id):
#     # Get the post or return 404 - corrected line
#     Post = get_object_or_404(post, pk=post_id, User=request.user)
    
#     if request.method == "POST":
#         form = postform(request.POST, request.FILES, instance=Post)
#         if form.is_valid():
#             # No need to set user again since we're editing existing post
#             post = form.save()
#             return redirect('post-list')
#     else:
#         form = postform(instance=Post)
    
#     return render(request, 'Post_form.html', {'form': form})
@login_required
def edit_post(request, post_id):
    # Get the post or return 404 - FIXED the model reference
    User_post = get_object_or_404(post, pk=post_id, User=request.user)
    
    if request.method == "POST":
        form = postform(request.POST, request.FILES, instance=User_post)
        if form.is_valid():
            form.User = request.user
            User_post = form.save()
            return redirect('post-list')  # Make sure this URL name matches your urls.py
    else:
        form = postform(instance=User_post)
    
    return render(request, 'Edit_form.html', {'form': form})

@login_required  
def delete_post(request , post_id):
   User_post = get_object_or_404(post ,pk = post_id , User = request.user)
   if request.method == "POST":
      User_post.delete()
      return redirect('post-list')
   return render(request , 'delete_post.html' , {'post': User_post} )

def register(request):
   if request.method == 'POST':
      form = UserRegistrationForm(request.POST , request.FILES)
      if form.is_valid():
         user = form.save(commit=False)
         user.set_password(form.cleaned_data['password1'])
         user.save()
         login(request , user)
         return redirect('post-list')
   else:
      form = UserRegistrationForm()
      

   return render(request , 'registration/register.html' , {'form': form} )
   
def custom_logout(request):
    logout(request)
    return redirect('post-list')
      