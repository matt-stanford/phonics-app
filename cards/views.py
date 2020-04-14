from django.shortcuts import render
from .models import Card

def index(request):
    return render(request, 'index.html', {})


def card(request):
    if request.method == 'POST':
        guess = request.POST['guess']
        return render(request, 'card.html', {'guess': guess})
    else:
        card = Card.objects.order_by('?').first()
        return render(request, 'card.html', {'card': card})
    
