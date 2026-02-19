import pytest
from django.urls import reverse

from apps.blog.factories import PostFactory


@pytest.mark.django_db
def test_post_list_includes_total_count_in_response(client) -> None:
    PostFactory.create_batch(3, is_published=True)
    PostFactory(is_published=False)

    response = client.get(reverse("blog:post-list"))
    payload = response.content.decode("utf-8")

    assert response.status_code == 200
    assert "Total posts: 3" in payload
