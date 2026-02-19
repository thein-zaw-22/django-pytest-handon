import pytest
from django.test import Client

from apps.blog.factories import PostFactory
from apps.blog.models import Post


@pytest.fixture
def user(django_user_model):
    # Use Django's built-in test user model fixture for auth-related tests.
    return django_user_model.objects.create_user(
        username="learner",
        email="learner@example.com",
        password="strong-test-password",
    )


@pytest.fixture
def authenticated_client(user) -> Client:
    # This fixture demonstrates authenticated client tests with pytest.
    client = Client()
    client.force_login(user)
    return client


@pytest.fixture
def post() -> Post:
    # Factory-based fixture keeps test data expressive and reusable.
    return PostFactory()
