from django.shortcuts import render
import json
import urllib.request
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        response = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='
            + city + '&appid=3cd9a5ff79f664875bb676fa2669c6f5'
            )

        
        source = response.read()
        
        list_of_data = json.loads(source)

        data = {
            "country_code" : str(list_of_data['sys']['country']),
            "temp" : str(list_of_data['main']['temp']) + 'k',
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity" : str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "Weather_app/index.html", data)