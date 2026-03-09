from django.db import models
from member.models import Member

class Author(models.Model):
    name=models.CharField(max_length=100)
    biography=models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=150)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='author')
    isbn=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    is_available=models.BooleanField(null=True,blank=True)

    class Meta:
        ordering=['-id']


    def __str__(self):
        return f"Title {self.title} by Author {self.author.name}"

class BorrowRecord(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='books')
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    borrow_date=models.DateTimeField(auto_now_add=True)
    return_date=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f" The book {self.book.title} by Member {self.member.name}"