from django.urls import path
# from book_api_app.views import book_list, book_create, book
from book_api_app.views import BookCreate, BookList, BookDetail

urlpatterns = [
    # path('', book_create),
    path('', BookCreate.as_view()),
    # path('list/', book_list),
    path('list/', BookList.as_view()),
    # path('<int:pk>', book)
    path('<int:pk>', BookDetail.as_view())
]
