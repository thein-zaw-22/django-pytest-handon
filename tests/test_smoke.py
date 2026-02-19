import pytest
from django.conf import settings
from django.urls import reverse


def test_project_settings_are_loaded() -> None:
    """Smoke test to ensure Django settings are loaded correctly."""
    assert settings.SECRET_KEY


@pytest.mark.django_db
def test_admin_login_page_loads(client):
    """Smoke test to ensure the admin login page is accessible."""
    url = reverse("admin:login")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_main_page_loads(client):
    """Smoke test to ensure the main post list page is accessible."""
    url = reverse("blog:post-list")
    response = client.get(url)
    assert response.status_code == 200
