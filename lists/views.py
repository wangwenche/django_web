from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

# 视图函数的作用：处理用户输入；返回适当的响应
# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_user = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_user})

def new_list(request):
    list_user = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_user)
    return redirect(f'/lists/{list_user.id}/')

def add_item(request, list_id):
    list_user = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_user)
    return redirect(f'/lists/{list_user.id}/')