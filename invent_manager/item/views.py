from django.shortcuts import render, redirect, reverse
from .models import Item
# Create your views here.

def list(request):
    items = Item.objects.all()
    cxt = {
        'items':items,
    }
    return render(request, 'item/list.html', cxt)

def register(request):
    if request.method == 'GET':
        return render(request, 'item/register.html', context={})

    title = request.POST['title']
    image = request.FILES['image']
    content = request.POST['content']
    price = request.POST['price']
    amount = request.POST['amount']
    # account = request.POST['account']

    item = Item.objects.create(title=title, image=image, content=content, price=price, amount=amount)
    pk = item.id

    url = reverse("item:detail", kwargs={'pk':pk})
    return redirect(to=url)

def detail(request, pk):
    item = Item.objects.get(id=pk)

    cxt={
        'item':item,
    }

    return render(request, "item/detail.html", cxt)

def update(request, pk):
    item = Item.objects.get(id=pk)

    if request.method == "GET":
        cxt = {
            'item':item,
        }
        return render(request, "item/update.html", cxt)

    title = request.POST['title']
    image = request.FILES['image']
    content = request.POST['content']
    price = request.POST['price']
    amount = request.POST['amount']

    item.title = title
    item.image = image
    item.content = content
    item.price = price
    item.amount = amount

    item.save()

    url = reverse("item:detail", kwargs={'pk':item.id})
    return redirect(to=url)

def delete(request, pk):
    item = Item.objects.get(id=pk)

    item.delete()

    url = reverse("item:list")
    return redirect(to=url)










