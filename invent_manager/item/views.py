from django.shortcuts import render, redirect, reverse
from .models import Item
from .models import Account
# Create your views here.


def list(request):
    items = Item.objects.all()
    cxt = {
        'items':items,
    }
    return render(request, 'item/list.html', cxt)

def register(request):
    accounts = Account.objects.all()
    if request.method == 'GET':
        ctx = {
            'accounts':accounts,
        }
        return render(request, 'item/register.html', ctx)

    title = request.POST['title']
    image = request.FILES['image']
    content = request.POST['content']
    price = request.POST['price']
    amount = request.POST['amount']
    account = request.POST['account']

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
    accounts = Account.objects.all()
    if request.method == "GET":
        cxt = {
            'item':item,
            'accounts':accounts,
        }
        return render(request, "item/update.html", cxt)

    title = request.POST['title']
    image = request.FILES['image']
    content = request.POST['content']
    price = request.POST['price']
    amount = request.POST['amount']
    account = request.POST['account']

    item.title = title
    item.image = image
    item.content = content
    item.price = price
    item.amount = amount
    item.account = account

    item.save()

    url = reverse("item:detail", kwargs={'pk':item.id})
    return redirect(to=url)

def delete(request, pk):
    item = Item.objects.get(id=pk)

    item.delete()

    url = reverse("item:list")
    return redirect(to=url)






def a_list(request):
    accounts = Account.objects.all()

    ctx = {
        'accounts' : accounts,
    }
    return render(request, "account/list.html", ctx)

def a_register(request):
    if request.method == 'GET':
        return render(request, "account/register.html", context={})

    company = request.POST['company']
    number = request.POST['number']
    address = request.POST['address']

    acc = Account.objects.create(company=company, number=number, address=address)

    url = reverse("item:a_detail", kwargs={'pk':acc.id})
    return redirect(to=url)

def a_detail(request, pk):
    account = Account.objects.get(id=pk)

    ctx = {
        'account':account,
    }
    return render(request, "account/detail.html", ctx)

def a_delete(request, pk):
    account = Account.objects.get(id=pk)

    account.delete()

    url = reverse("item:a_list")
    return redirect(to=url)

def a_update(request, pk):
    account = Account.objects.get(id=pk)
    if request.method == "GET":
        ctx = {
            'account':account,
        }
        return render(request, "account/update.html", ctx)

    account.company = request.POST['company']
    account.number = request.POST['number']
    account.address = request.POST['address']

    account.save()

    url = reverse("item:a_detail", kwargs={'pk':account.id})
    return redirect(to=url)










