from django.shortcuts import render, redirect
from django.http import JsonResponse
from api.models import Tag, Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import PostListSerializer, TagListSerializer, TagListSerializer, PostDetailsSerializer, PostCreateSerializer 
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from api.forms import PostCreateForm
from django.contrib.auth import logout
from authe.models import Author

class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class PostDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailsSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'post_id'


@api_view(['GET', 'POST'])
def post_tag(request, tag_id):
    post = Post.objects.filter(tags__id = tag_id)
    ser = PostListSerializer(post, many = True)
    return Response({'data':ser.data})


@api_view(['GET', 'POST'])
def all_posts(request):
    print(request.user)
    posts = Post.objects.all()
    form = PostListSerializer
    return render(request, 'index.html', {'form':form, 'posts':posts})


def my_posts(request):
    print(request.user)
    posts = Post.objects.filter(author = request.user)
    form = PostListSerializer
    return render(request, 'index.html', {'form':form, 'posts':posts})

class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer
    
def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, 'post_detail.html', {'post':post})

def posts_with_tag(request, tag_id):
    posts = Post.objects.filter(tags__id = tag_id)
    return render(request, 'posts_filter.html', {'posts':posts})

def create_post(request):
    if request.user.is_authenticated:
        form = PostCreateForm()
        if request.method == 'POST':
            save_form = PostCreateForm(request.POST)
            if save_form.is_valid():
                note = save_form.save(commit=False)
                note.author = request.user
                note.save()
                return redirect('api:all_posts')
        return render(request, 'post_create.html', {'form':form})
    return redirect('authe:login')

def delete_post(request, post_id):
    post = Post.objects.filter(id = post_id).delete()
    return redirect('api:all_posts')

