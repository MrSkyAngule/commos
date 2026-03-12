import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_home_view(client):
    url = reverse('dashboard')
    response = client.get(url)
    assert response.status_code == 200
    # Проверяем то, что реально есть на странице
    assert "Ваши сообщения" in response.content.decode()
