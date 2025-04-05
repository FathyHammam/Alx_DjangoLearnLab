book.delete()
from bookshelf.models import Book

# Check if the book exists
books = Book.objects.all()
print(books)

Expected Output:
<QuerySet []>  # Empty QuerySet since the book was deleted
