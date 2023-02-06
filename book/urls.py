from django.urls import path
from . import views # 相対パスで指定（bookフォルダを指している）

urlpatterns = [
    path('',views.index_view,name='index'),
    path('book/',views.ListBookView.as_view(),name='list-book'), # CreateBookViewからの遷移先に指定するため、名前を定義する。
    path('book/<int:pk>/detail/',views.DetailBookView.as_view(),name='detail-book'),
    path('book/create/',views.CreateBookView.as_view(),name='create-book'),
    path('book/<int:pk>/delete/',views.DeleteBookView.as_view(),name='delete-book'),
    path('book/<int:pk>/update/',views.UpdateBookView.as_view(),name='update-book'),
    path('book/<int:book_id>/review/',views.CreateReviewView.as_view(),name='review'),
    # path('logout/',views.logout_view,name='logout'),
]

# <int:pk>でsqlite3に格納されているオブジェクト(この場合、登録されている本)を識別する。
#　各viewからの遷移先としてパスを指定するため、操作に応じて名前を定義。（ name= ）