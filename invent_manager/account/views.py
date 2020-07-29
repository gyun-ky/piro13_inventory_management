from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Account

# Create your views here.

def list(request):
    accounts = Account.objects.all()

    ctx = {
        'accounts' : accounts,
    }
    return render(request, "account/list.html", ctx)

def register(request):
    if request.method == 'GET':
        return render(request, "account/register.html", context={})

    company = request.POST['company']
    number = request.POST['number']
    address = request.POST['address']

    acc = Account.objects.create(company=company, number=number, address=address)
    pk = acc.id

    url = reverse("account:detail", kwargs={'pk':pk})
    return redirect(to=url)

def detail(request, pk):
    account = Account.objects.get(id=pk)

    ctx = {
        'account':account,
    }
    return render(request, "account/detail.html", ctx)

def delete(request, pk):
    account = Account.objects.get(id=pk)

    account.delete()

    url = reverse("account:list")
    return redirect(to=url)

def update(request, pk):
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

    url = reverse("account:detail", kwargs={'pk':account.id})
    return redirect(to=url)



