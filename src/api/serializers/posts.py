from rest_framework import serializers
from api.models import Post, Tag
from .tag import TagListSerializer, TagPostSerializer


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostDetailsSerializer(serializers.ModelSerializer):
    def update(self, instance, data):
        tags = data.pop('tags', [])
        instance = super(PostDetailsSerializer, self).update(instance, data)
        if tags:
            post_tags = instance.tags.all()
            for tag in tags:
                if tag not in post_tags:
                    instance.tags.add(tag)
                    instance.save()
        return instance
    class Meta:
        model = Post
        exclude = ('id',)
        

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('id',)

