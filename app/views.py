from django.shortcuts import render

def master_list(request):
    return render(request, 'app/master_list.html', {})
