from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display fields in the list view
    list_filter = ('publication_year', 'author')  # Add filters for easier navigation
    search_fields = ('title', 'author')  # Enable search by title and author
