from django.shortcuts import render
from cms.models import Presentation, Application, Api, Documentation, Footer


def index(request):
    model_list = [Presentation, Application, Api, Documentation, Footer]
    data = {}

    for model in model_list:
        try:
            data[model._meta.verbose_name] = model.objects.latest('id')
        except:
            pass

    return render(request, 'cms/index.html', data)
