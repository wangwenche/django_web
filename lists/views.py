from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# 视图函数的作用：处理用户输入；返回适当的响应
# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})