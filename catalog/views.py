from django.shortcuts import render


def catalog(requests):
    return render(requests, 'home.html')