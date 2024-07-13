from django.shortcuts import render,redirect,get_object_or_404
from . forms import *
from . models import *


# def add_blog(request):
#     if request.user.is_authenticated:
#              if request.user.is_doctor:
#                   if request.method =='POST':
#                       form=BlogPostForm(request.POST,request.FILES)
#                       if form.is_valid():
#                              blog = form.save(commit=False)
#                              blog.author = request.user
#                              blog.save()
#                              print("Add blog sucessfully")
#                              return render(request,'dashboard_doctor.html')
#                   else:
#                      print('not working')
#                      form=BlogPostForm()
#     else:
#          return redirect('login')
#     return render(request,'add_blog.html',{'form':form})
def add_blog(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_doctor:
        # Handle case where user is not a doctor, maybe show an error or redirect
        return render(request, 'error.html', {'message': 'You are not authorized to add a blog.'})

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            print("Add blog successfully")
            return redirect('dashboard')  # Assuming 'dashboard_doctor' is the name of the URL
        else:
            print('Form is invalid')
    else:
        form = BlogPostForm()

    return render(request, 'add_blog.html', {'form': form})

def doctor_display_blog(request):
     blog=BlogPost.objects.all()
     return render(request,'display_blog.html',context={'blogs':blog})
     


def update_blog(request,id):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_doctor:
        # Handle case where user is not a doctor, maybe show an error or redirect
        return render(request, 'error.html', {'message': 'You are not authorized to add a blog.'})
    
    blog = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            print("Updated")
            return redirect('display_blog') 
    else:
        form = BlogPostForm(instance=blog)
    return render(request, 'update_blog.html', {'form': form, 'blog': blog})

def delete_blog(request,id):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_doctor:
        # Handle case where user is not a doctor, maybe show an error or redirect
        return render(request, 'error.html', {'message': 'You are not authorized to delete a blog.'})
    blog=get_object_or_404(BlogPost,id=id)
    blog.delete()
    return redirect('dashboard')