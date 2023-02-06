from django.utils import timezone
from django.db import models
from .consts import MAX_RATE
# from django.urls import reverse

# SQLの「create table」文は使わずにDjangoのコマンドで作成できる
# class SampleModel(models.Model):
#     title = models.CharField(max_length=100)
#     number = models.IntegerField()

class TestDate(models.Model):
    test_date = models.DateField('日付')

    def __str__(self):
        return timezone.localtime(self.test_date)


CATEGORY = (('Business','ビジネス'),('Life','生活'),('Other','その他'))

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True) # 画像を扱うフィールド
    category = models.CharField(max_length= 100,choices= CATEGORY)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self): # 「__str__」は、文字列表現を返す特殊メソッド。
        return self.title #　ここでタイトルを返す

    # def get_absolute_url(self):
    #     return reverse('list-book')
    # get_absolute_urlを使用する際は、viewsのサクセスURLは使わないのでコメントアウトしておく


RATE_CHOICES = [(x,str(x)) for x in range(0,MAX_RATE+1)]

class Review(models.Model):
    book = models.ForeignKey(Book,on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    text = models.TextField()
    rate = models.IntegerField(choices = RATE_CHOICES)
    user = models.ForeignKey('auth.User',on_delete = models.CASCADE)

    def __str__(self):
        return self.title