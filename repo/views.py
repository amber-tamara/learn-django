from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Repository

def repository_list(request):
    repositories = Repository.objects.all()

    paginator = Paginator(repositories, 10)  # Show 10 repositories per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print('ereeeeeeeeeeeeeeeeeeeee')
    print(request)

    return render(request, 'repo/repository_list.html', {'page_obj': page_obj})
