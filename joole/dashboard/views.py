from django.shortcuts import render, redirect
from django.views.generic import View
import json
from django.core.serializers.json import DjangoJSONEncoder
from .forms import ClientForm
from .models import Conso_eur, Conso_watt


class ClientFormView(View):
    def get(self, request):
        return render(request, 'dashboard/accueil.html')

    def post(self, request):
        form = ClientForm(request.POST)

        if form.is_valid():
            client_id = form.cleaned_data['client']
            return redirect('dashboard:results', client_id=client_id)

# calcule la consommation moyenne sur plusieurs mois
def moy(list_mois, conso):
    v = 0;
    i = 0;
    
    for m in list_mois:
        v += conso[m]
        i = i+1;

    if i != 0:
        return v/i
    else:
        return 0

def results(request, client_id):
    conso_euro = []
    conso_watt = []
    annual_costs = {}
    json_conso_watt=""
    is_elec_heating = False
    dysfunction_detected = False

    if (client_id != 'login.html'):
        conso_euro = Conso_eur.objects.filter(client_id = client_id)
        for c in conso_euro: 
            annual_costs[c.year] = c.janvier +  c.fevrier + c.mars + c.avril + c.mai + c.juin + c.aout + c.septembre + c.octobre + c.novembre + c.decembre

        conso_watt = Conso_watt.objects.filter(client_id = client_id).values()
        json_conso_watt = json.dumps(list(conso_watt), cls=DjangoJSONEncoder)

        # si la consommation en hiver dépasse largement celle d'été
        if (moy(['janvier','fevrier','decembre'],conso_watt[0]) > 2*moy(['juin','juillet','aout'],conso_watt[0])):
            is_elec_heating =True 

        # si la différence entre les deux années dépasse le seuil fixé (10%)
        if (abs(annual_costs[2017] - annual_costs[2016])/annual_costs[2016] > 0.1):
            dysfunction_detected = True

    context = {
        "conso_euro": conso_euro,
        "json_conso_watt": json_conso_watt,
        "annual_costs": annual_costs,
        "is_elec_heating": is_elec_heating,
        "dysfunction_detected": dysfunction_detected
    }
    return render(request, 'dashboard/results.html', context)
