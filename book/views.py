from django.shortcuts import render , redirect
# from django.contrib.auth import logout
from django.db.models import Avg # レビューの平均点を判定
from django.core.paginator import Paginator
from .consts import ITEM_PER_PAGE
from django.contrib.auth.mixins import LoginRequiredMixin # ログイン状態の判定
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView
from django.urls import reverse , reverse_lazy
from .models import Book , Review

def index_view(request):
    object_list = Book.objects.order_by('-id') # 何に基づいて並べ替えるかを指定。
    ranking_list = Book.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')
    # 以下、ページネーション実装
    paginator = Paginator(ranking_list,ITEM_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.page(page_number)
    #
    return render(request,'book/index.html',{'object_list':object_list,'ranking_list':ranking_list,'page_obj':page_obj},)

# def logout_view(request):
#     logout(request)
#     return redirect('index')


class ListBookView(LoginRequiredMixin,ListView):
    template_name = 'book/book_list.html'
    model = Book
    paginate_by = ITEM_PER_PAGE

class DetailBookView(LoginRequiredMixin,DetailView):
    template_name = 'book/book_detail.html'
    model = Book

class CreateBookView(LoginRequiredMixin,CreateView):
    template_name = 'book/book_create.html'
    model = Book
    fields = ('title','text','category','thumbnail')
    success_url = reverse_lazy('list-book') # 遷移先のURLをここで指定。

    def form_valid(self,form): # formにユーザー情報を追加
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeleteBookView(LoginRequiredMixin,DeleteView):
    template_name = 'book/book_delete.html'
    model = Book
    success_url = reverse_lazy('list-book')

    def get_object(self,queryset=None): # ログインしているユーザーしか編集できない仕組み
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

class UpdateBookView(LoginRequiredMixin,UpdateView):
    template_name = 'book/book_update.html'
    model = Book
    fields = ('title','text','category','thumbnail')
    # success_url = reverse_lazy('list-book')

    def get_object(self,queryset=None): # ログインしているユーザーしか編集できない仕組み
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

    def get_success_url(self): # 更新処理後に遷移させるページを設定
        return reverse('detail-book',kwargs={'pk':self.object.id})

class CreateReviewView(CreateView):
    model = Review
    fields = ('book','title','text','rate')
    template_name = 'book/review_form.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):# Reviewデータ送信後のページ遷移先を指定。
        return reverse('detail-book',kwargs={'pk':self.object.book.id})