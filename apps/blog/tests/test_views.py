import pytest
from django.urls import reverse

from apps.blog.factories import PostFactory


@pytest.mark.django_db
def test_post_list_view_returns_200(client) -> None:
    PostFactory(is_published=True)

    response = client.get(reverse("blog:post-list"))

    assert response.status_code == 200


@pytest.mark.django_db
def test_post_detail_view_returns_200(client) -> None:
    post = PostFactory(is_published=True)

    response = client.get(reverse("blog:post-detail", kwargs={"pk": post.pk}))

    assert response.status_code == 200


@pytest.mark.django_db
def test_post_detail_view_returns_404_for_missing_post(client) -> None:
    response = client.get(reverse("blog:post-detail", kwargs={"pk": 999999}))

    assert response.status_code == 404
