import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(email='user@example.com', name='John Doe', mobile_number='1234567890', password='password123')
    assert user.email == 'user@example.com'
    assert user.name == 'John Doe'
    assert user.mobile_number == '1234567890'
    assert user.check_password('password123')
