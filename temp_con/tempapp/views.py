from django.shortcuts import render
from django.http import HttpResponse

def convert_temperature(request):
    if request.method == 'POST':
        temperature = float(request.POST.get('temperature'))
        from_scale = request.POST.get('from_scale')
        to_scale = request.POST.get('to_scale')

        if from_scale == 'C' and to_scale == 'F':
            result = (temperature * 9/5) + 32
        elif from_scale == 'F' and to_scale == 'C':
            result = (temperature - 32) * 5/9
        else:
            # No conversion needed
            result = temperature
        
        return HttpResponse(f'Converted Temperature: {result}')
    
    return render(request, 'temperature_converter.html', {'title': 'Temperature Converter'})
