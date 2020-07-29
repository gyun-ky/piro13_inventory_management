from django.shortcuts import render, redirect, reverse
from .models import Item
# Create your views here.

def list(request):
    items = Item.objects.all()
    cxt = {
        'items':items
    }
    return render(request, 'item/list.html', cxt)

def register(request):
    if request.method == 'GET':
        return render(request, 'item/register.html', context={})

    title = request.POST['title']
    image = request.POST['image']
    content = request.POST['content']
    price = request.POST['price']
    amount = request.POST['amount']
    # account = request.POST['account']

    item = Item.objects.create(title=title, image=image, content=content, price=price, amount=amount)
    pk = item.id

    url = reverse("item:detail", kwargs={'pk':pk})
    return redirect(url)

def detail(request, pk):
    item = Item.objects.get(id=pk)

    cxt={
        'item':item
    }

    return render(request, "item/datail.html", cxt)










