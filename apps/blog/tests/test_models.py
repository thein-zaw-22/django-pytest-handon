import pytest

from apps.blog.models import Post


@pytest.mark.django_db
def test_post_creation() -> None:
    post = Post.objects.create(
        title="First post",
        content="This is a realistic content body.",
        is_published=True,
    )

    assert post.pk is not None
    assert post.is_published is True
    assert post.created_at is not None


@pytest.mark.django_db
def test_post_str_representation() -> None:
    post = Post.objects.create(title="Readable title", content="Body text")

    assert str(post) == "Readable title"
