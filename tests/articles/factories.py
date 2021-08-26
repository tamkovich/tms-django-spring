import factory
from faker import Faker
from factory import fuzzy

from articles.models import Article, Category

faker = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = fuzzy.FuzzyText(prefix="test-brand-")

#
# class CarModelFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Article
#
#     brand = fuzzy.FuzzyText(prefix="test-brand-")
#     model = fuzzy.FuzzyText(prefix="test-model-")
#     coach = factory.SubFactory(CoachProfileFactory)
