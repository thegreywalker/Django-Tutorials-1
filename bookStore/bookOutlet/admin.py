from django.contrib import admin
from .models import Address, Book, Author, Country


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating", "isBestSelling")
    list_display = ("title", "author")


class BookCountries(admin.ModelAdmin):
    list_display = ("name", "code")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country, BookCountries)