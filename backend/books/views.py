#from django.shortcuts import render
#from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#def index(request):
#    #books = Book.objects.all()
#    books = []
#
#    for book in Book.objects.all():
#        books.append({
#            'title' : book.title,
#            'author' : book.author,
#            'pages' : book.pages,
#        })
#    return JsonResponse(books, safe=False)
