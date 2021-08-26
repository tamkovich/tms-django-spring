import pytest

from articles.models import Category


@pytest.fixture
def category():
    return Category.objects.create(name='test_name')
