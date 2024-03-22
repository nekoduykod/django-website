from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page

from .models import Projects


# def home(request):
#     return render(request, 'home.html')


@cache_page(60 * 15) # 15 хв
def projects_page(request):
    projects_list = Projects.objects.all().order_by('id')
    paginator = Paginator(projects_list, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'projects.html', {'page_obj': page_obj})