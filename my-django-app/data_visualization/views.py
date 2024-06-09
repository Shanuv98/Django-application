from django.shortcuts import render, redirect
from .models import DataPoint
from .forms import DataPointForm

def chart_view(request):
    data_points = DataPoint.objects.all()
    dates = [data.date.strftime('%Y-%m-%d') for data in data_points]
    values = [data.value for data in data_points]
    return render(request, 'data_visualization/chart.html', {
        'dates': dates,
        'values': values
    })

def add_data_point(request):
    if request.method == 'POST':
        form = DataPointForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chart_view')
    else:
        form = DataPointForm()
    return render(request, 'data_visualization/add_data_point.html', {'form': form})
