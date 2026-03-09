from django.urls import include,path
from rest_framework_nested import routers
from book.views import BookViewset,BookBorrowViewSet,BookReturnViewset

router=routers.DefaultRouter()

router.register('books',BookViewset,basename='books')
router.register('borrow',BookBorrowViewSet,basename='BorrowBook')
router.register('return',BookReturnViewset,basename='Book_return')

urlpatterns = [
    path('', include(router.urls)),

]