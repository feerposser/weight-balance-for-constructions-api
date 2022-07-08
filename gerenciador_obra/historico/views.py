from django.http import HttpResponse
from django.views import View
import csv

from .models import ModelHistorico
from balanca.models import ModelBalanca


class HistoricoView(View):
    def post(self, request):
        try:
            historico = ModelHistorico.objects.create(
                balanca=ModelBalanca.objects.get(name=request.POST["balanca"]),
                weight=request.POST["peso"]
            )
            return HttpResponse("ok.{}".format(historico.id))
        except Exception as e:
            return HttpResponse("error: {}".format(e.__str__()))


def get_csv(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = "attachment; filename=historico_balancas.csv"

    writer = csv.writer(response)
    writer.writerow(["ID", "NOME BALANÇA", "PESO", "DATA", "HORA"])

    historicos = ModelHistorico.objects.all()

    for historico in historicos:
        writer.writerow([historico.id,
                         historico.balanca.name,
                         historico.weight,
                         historico.get_date(),
                         historico.get_hour()])

    return response
