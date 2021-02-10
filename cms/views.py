from django.shortcuts import render
from cms.models import Presentation, Application, Api, Documentation, Footer

from django.utils.translation import ugettext as _
from django.utils.translation import ungettext


def index(request):
    data = {}

    for model in [Presentation, Application, Api, Documentation, Footer]:
        try:
            data[model._meta.verbose_name] = model.objects.latest('id')
        except:
            pass

    return render(request, 'cms/index.html', data)


def test_i18n(request):
    return render(request, 'cms/langue.html')