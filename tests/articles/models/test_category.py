import pytest

from articles.models import Category


@pytest.mark.django_db
def test_it_creates_if_valid_data():
    Category.objects.create(name='bla bla')
    assert Category.objects.count() == 1
