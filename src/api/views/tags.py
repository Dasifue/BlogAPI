from django.shortcuts import render, redirect
from django.http import JsonResponse
from api.models import Tag, Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import PostListSerializer, TagListSerializer, TagListSerializer, PostDetailsSerializer, TagCreateSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from api.forms import TagCreateForm


class TagListView(ListAPIView):
    serializer_class = TagListSerializer
    queryset = Tag.objects.all()

class TagDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    lookup_field = 'tags__id'
    lookup_url_kwarg = 'tag_id'

class TagCreateView(CreateAPIView):
    serializer_class = TagCreateSerializer

  
def tags_link(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags':tags})


def create_tag(request):
    form = TagCreateForm()
    tags = Tag.objects.all()
    if request.method == 'POST':
        save_form = TagCreateForm(request.POST)
        save_form.save()
        
        return redirect('api:tags_link')
    return render(request, 'tag_create.html', {'form':form, 'tags':tags})


def delete_tag(request, tag_id):
    tag = Tag.objects.filter(id = tag_id).delete()
    return redirect('api:tags_link')





