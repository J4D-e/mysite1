import requests
def rickymorty (request):
   # URL de la API
   api
   _url = 'https://rickandmortyapi.com/api/character/2'
   # Realizar solicitud a la API
   response = requests.get (api_url)
   data = []
   if response. status_code == 200:
      data = response. json ()
      print (data)
  return render(request, 'polls/testapirick.html', {'data': data})
