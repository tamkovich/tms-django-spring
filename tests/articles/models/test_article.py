import pytest


from articles.models import Article


@pytest.mark.django_db
def test_it_creates_article_if_valid_data():
    Article.objects.create(
        title='test title',
        content='test content',
        author_name='test author',
        rating=10,
    )
    assert Article.objects.count() == 1


@pytest.mark.django_db
def test_it_creates_article_if_category_passed(category):
    Article.objects.create(
        title='test title',
        content='test content',
        author_name='test author',
        rating=10,
        category=category,
    )
    assert Article.objects.count() == 1


@pytest.mark.django_db
def test_it_updates_article_if_new_category_passed(category):
    Article.objects.create(
        title='test title',
        content='test content',
        author_name='test author',
        rating=10,
        category=category,
    )
    article = Article.objects.get()
    article.category = category
    article.save()
    assert Article.objects.filter(category=category).count() == 1
