from django.shortcuts import render
from django.http import HttpResponse

# View to list all the books
def book_list(request):
    return HttpResponse("This is the list of books.")

# View to display details of one book
def book_details(request, book_id):
    return HttpResponse(f"This is the detail view for book ID: {book_id}")

# View to add a book
def add_book(request):
    return HttpResponse("This is the form to add a new book.")
  


# Create your views here.
