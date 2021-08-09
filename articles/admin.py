from django.contrib import admin

from articles.models import Article, Category, Author, ContactInfo


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(ContactInfo)
