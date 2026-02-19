from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from apps.blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def render_to_response(self, context, **response_kwargs):
        posts = context["object_list"]
        lines = [f"Total posts: {posts.count()}"]
        lines.extend(post.title for post in posts)
        return HttpResponse("\n".join(lines), **response_kwargs)


class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def render_to_response(self, context, **response_kwargs):
        post = context["object"]
        return HttpResponse(f"{post.title}\n{post.content}", **response_kwargs)
