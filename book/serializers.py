from rest_framework import serializers
from book.models import Book,BorrowRecord
from member.models import Member


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','title','author','isbn','category','is_available']


class BookBorrow(serializers.ModelSerializer):
    book_id=serializers.IntegerField()
    class Meta:
        model=BorrowRecord
        fields=['id','book_id','return_date']


    def save(self):
        member_id=self.context['member_id']
        book_id=self.validated_data['book_id']
        return_date=self.validated_data.get('return_data',None)
        member=Member.objects.get(id=member_id)
        book=Book.objects.get(id=book_id)
        
        if not book.is_available:
            raise serializers.ValidationError("Book is already Borrowed !")
        
        borrowBook=BorrowRecord.objects.create(member=member,book=book,**self.validated_data)
        book.is_available=False
        book.save()
        self.instance=borrowBook
        return self.instance



    def book_Validation(self,value):
        if not Book.objects.filter(pd=value).exists():
            raise serializers.ValidationError("This book id {value} id is not exists ! ")
        
        return value


class BookReturn(serializers.ModelSerializer):
    book_id=serializers.IntegerField()
    class Meta:
        model=BorrowRecord
        fields=['id','book_id','return_date']
        read_only_fields = ['return_date']

    def save(self):
        member=self.context['member_id']
        book_id=self.validated_data['book_id']
        
        try :
        
            borrow=BorrowRecord.objects.get(id=book_id,member=member)

        except BorrowRecord.DoesNotExist:
            raise serializers.ValidationError("This book is not exists !")
        

        book=borrow.book
        book.is_available=True
        book.save()
        borrow.delete()

        return {'message':"The Book is return successfully "}