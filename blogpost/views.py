from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import BlogModel
from django.urls import reverse_lazy
# Create your views here.

class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel
class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel
class BlogCreate(CreateView):
    template_name = 'create.html'
    #ユーザーが入力した情報をどのテーブルに保存するかを指定する
    model = BlogModel
    #フォームの中でどの項目を表示させるかを指定
    fields = ('title','content','category')
    #reverse_lazyは逆に流れを変える views.py→urls.py→urlとなる 
    success_url = reverse_lazy('list')
class BlogDelete(DeleteView):
    template_name = 'delete.html'
    #ユーザーが入力した情報をどのテーブルに保存するかを指定する
    model = BlogModel
    #reverse_lazyは逆に流れを変える views.py→urls.py→urlとなる 
    success_url = reverse_lazy('list')
class BlogUpdate(UpdateView):
    template_name = 'update.html'
    #ユーザーが入力した情報をどのテーブルに保存するかを指定する
    model = BlogModel
    #フォームの中でどの項目を表示させるかを指定
    fields = ('title','content','category')
    #reverse_lazyは逆に流れを変える views.py→urls.py→urlとなる 
    success_url = reverse_lazy('list')