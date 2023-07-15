from django.urls import path
from . import views
from django.urls import include
urlpatterns = [
    # path('books/',views.books)
    path('books',views.BookList.as_view()),
    path('books/<int:pk>',views.Book.as_view()),
    path('__debug__/', include('debug_toolbar.urls')),
]
