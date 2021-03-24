from django.urls import path, include
from .views import post_tag, all_posts, PostListView, PostDetailView, TagListView, TagDetailView, PostCreateView, TagCreateView, post_detail, tags_link, posts_with_tag, create_post, create_tag, delete_post, delete_tag, my_posts


app_name = 'api'


urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('tags/', TagListView.as_view()),
    path('tag_details/<int:tag_id>',  TagDetailView.as_view()),
    path('post_details/<int:post_id>', PostDetailView.as_view()),
    path('post_tag/<int:tag_id>', post_tag),
    path('all_posts/', all_posts, name='all_posts'),
    path('post_create/', PostCreateView.as_view()),
    path('tag_create/', TagCreateView.as_view()),
    path('post_detail/<int:post_id>', post_detail, name='post_detail'),
    path('tags_link/', tags_link, name='tags_link'),
    path('posts_filter/<int:tag_id>', posts_with_tag, name = 'posts_with_tag'),
    path('create_post/', create_post, name='create_post'),
    path('create_tag/', create_tag, name='create_tag'),
    path('delete_post/<int:post_id>', delete_post, name='delete_post'),
    path('delete_tag/<int:tag_id>', delete_tag, name='delete_tag'),
    path('my_posts/', my_posts, name = 'my_posts')
]