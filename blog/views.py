from django.shortcuts import render,redirect,get_object_or_404
from . forms import *
from . models import *


def add_blog(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_doctor:

        return render(request, 'error.html', {'message': 'You are not authorized to add a blog.'})

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            print("Add blog successfully")
            return redirect('dashboard')
        else:
            print('Form is invalid')
    else:
        form = BlogPostForm()

    return render(request, 'add_blog.html', {'form': form})


def display_blog(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.is_doctor:
        user_blog=BlogPost.objects.filter(author=request.user)
        return render(request,'blog_doctor.html',{'blogs':user_blog})
    else:
        categories=Category.objects.all()
        categorized_blogs = {category: BlogPost.objects.filter(category=category, status='published') for category in categories}
        return render(request,'blog_patient.html',context={'categorized_blogs':categorized_blogs})

     


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