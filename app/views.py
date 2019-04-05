from django.shortcuts import render, redirect
from . models import Master
from . forms import RecordForm

def master_list(request):
    masters = Master.objects.all()
    return render(request, 'app/master_list.html', {'masters': masters})

def create_record(request, pk):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('master_list')
    else:
        form = RecordForm()
    return render(request, 'app/create_record.html', {'form': form})
