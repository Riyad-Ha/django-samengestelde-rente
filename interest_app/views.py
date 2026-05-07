from django.shortcuts import render
from .models import Berekening

def home(request):
    context = {}
    if request.method == 'POST':
        try:
            # Inputs (minstens 2 - hier zijn er 3)
            kapitaal = float(request.POST.get('kapitaal'))
            rente = float(request.POST.get('rente'))
            looptijd = float(request.POST.get('looptijd'))

            # Formule samengestelde rente: A = P * (1 + r/100)^t
            eindbedrag = kapitaal * (1 + rente / 100) ** looptijd
            rentewinst = eindbedrag - kapitaal

            # Opslaan in database
            Berekening.objects.create(
                kapitaal=kapitaal,
                rente=rente,
                looptijd=looptijd,
                eindbedrag=eindbedrag,
                rentewinst=rentewinst
            )

            # Outputs (minstens 2 - hier zijn er 2)
            context = {
                'kapitaal': kapitaal,
                'rente': rente,
                'looptijd': looptijd,
                'eindbedrag': round(eindbedrag, 2),
                'rentewinst': round(rentewinst, 2),
            }
        except (ValueError, TypeError):
            context = {'error': "Gelieve geldige getallen in te voeren."}

    return render(request, 'interest_app/home.html', context)