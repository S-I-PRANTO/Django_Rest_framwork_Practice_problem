from django.shortcuts import render
from book.serializers import BooksSerializer,BookBorrow,BookReturn
from book.models import Book,BorrowRecord
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import CreateModelMixin,ListModelMixin
class BookViewset(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BooksSerializer


class BookBorrowViewSet(ModelViewSet):
    serializer_class=BookBorrow

    def get_serializer_context(self):
        member=self.request.user
        return {'member_id':member.id}

    def get_queryset(self):
        member_obj=self.request.user
        borrow_recode=BorrowRecord.objects.filter(member=member_obj)
        return borrow_recode
    

class BookReturnViewset(CreateModelMixin,ListModelMixin,GenericViewSet):
    serializer_class=BookReturn


    def get_serializer_context(self):
        member=self.request.user
        return {'member_id':member.id}

    def get_queryset(self):
        member_obj=self.request.user
        borrow_recode=BorrowRecord.objects.filter(member=member_obj)
        return borrow_recode
