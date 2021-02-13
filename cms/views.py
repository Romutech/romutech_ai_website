from django.shortcuts import render
from cms.models import Presentation, Application, Api, Documentation, Footer
from django.views.decorators.cache import cache_page

@cache_page(60 * 1440)
def index(request):
    data = {}

    for model in [Presentation, Application, Api, Documentation, Footer]:
        try:
            data[model._meta.verbose_name] = model.objects.latest('id')
        except:
            pass

    return render(request, 'cms/index.html', data)
