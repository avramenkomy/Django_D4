from django.contrib import admin
from p_library.models import Book, Author, Publisher

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    @staticmethod
    def publishing_house(obj):
        return obj.publisher.pub_name


    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'description', 'publisher', 'year_release', 'author', 'price', 'copy_count')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    @staticmethod
    def books(self):
        return ', '.join([book.title for book in self.book_publisher.all()])

    list_display = ('pub_name', 'books')
