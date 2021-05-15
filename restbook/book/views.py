from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer, BookModelSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics

from rest_framework import authentication
from rest_framework import permissions


# Create your views here.


@csrf_exempt
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


# api/v1/book/1
@csrf_exempt
def book_detail(request, id):
    book = Book.objects.get(id=id)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)

        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)


    elif request.method == "DELETE":
        book.delete()
        return HttpResponse(status=204)


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookModelSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):

    def get_object(self, id):
        return Book.objects.get(id=id)

    def get(self, request, id):
        book = self.get_object(id)
        serializer = BookModelSerializer(book)
        return Response(serializer.data)

    def put(self, request, id):
        book = self.get_object(id)
        serializer = BookModelSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        book = self.get_object(id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookListMixin(mixins.ListModelMixin, generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookDetailMixin(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):

    authentication_classes = [authentication.BasicAuthentication,authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
                                      #IsAdminuser
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
