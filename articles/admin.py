from django.contrib import admin

from articles.models import Article, Author, Category, ContactInfo, Edition


admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(ContactInfo)
admin.site.register(Edition)


# @admin.register(Category)
# @admin.register(Article)
