from django.shortcuts import render
from cms.models import Presentation, Application, Api, Documentation, Footer


def index(request):
    data = {}

    for model in [Presentation, Application, Api, Documentation, Footer]:
        try:
            data[model._meta.verbose_name] = model.objects.latest('id')
        except:
            pass

    return render(request, 'cms/index.html', data)
