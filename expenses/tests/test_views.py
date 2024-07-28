import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_create_user():
    client = APIClient()
    url = reverse('create_user')
    data = {
        'email': 'user@example.com',
        'name': 'John Doe',
        'mobile_number': '1234567890',
        'password': 'password123'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data['email'] == 'user@example.com'
    assert response.data['name'] == 'John Doe'

@pytest.mark.django_db
def test_token_obtain_pair():
    client = APIClient()
    user_data = {
        'email': 'user@example.com',
        'name': 'John Doe',
        'mobile_number': '1234567890',
        'password': 'password123'
    }
    user = client.post(reverse('create_user'), user_data, format='json')
    url = reverse('token_obtain_pair')
    data = {
        'email': 'user@example.com',
        'password': 'password123'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data
