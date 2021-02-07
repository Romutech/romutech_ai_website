from django.shortcuts import render
from cms.models import Home, Features, Application, Api, Documentation, Footer

def index(request):
    home            = Home.objects.latest('id')
    features        = Features.objects.latest('id')
    application     = Application.objects.latest('id')
    api             = Api.objects.latest('id')
    documentation   = Documentation.objects.latest('id')
    footer          = Footer.objects.latest('id')

    return render(request, 'cms/index.html', locals())
