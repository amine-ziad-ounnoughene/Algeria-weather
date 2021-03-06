
import requests
import folium
def weather(city):
  api_key = "your_API_key"
  base_url =  "http://api.openweathermap.org/data/2.5/weather?" 
  url = base_url + "appid=" + api_key + "&q=" + str(city)
  response = requests.get(url)
  x = dict(response.json())
  if x["cod"] != "404":
    return [dict(x["coord"])['lat'],dict(x["coord"])['lon']
    ,dict(x["weather"][0])['description'],
    dict(x['main'])['temp']-273]
m = folium.Map(location=[35.7058, 4.5419], zoom_start=6)
wilayat = ['in salah', "el meniaa",
 'chlef',
 'laghouat',
 'oum el bouaghi',
 'batna',
 'bejaia',
 'biskra',
  'bechar',
 'blida',
 'bouira',
 'tamanrasset',
 'tebessa',
 'tlemcen',
 'tiaret',
 'tizi ouzou',
 'algiers',
 'djelfa',
 'jijel',
 'setif',
 'saida',
 'skikda',
 'sidi bel abbes',
 'annaba',
 'guelma',
 'constantine',
 'medea',
 'mostaganem',
 "msila",
 'mascara',
 'ouargla',
 'oran',
 'el bayadh',
 'illizi',
 'bordj bou arreridj',
 'boumerdes',
 'el tarf',
 'tindouf',
 'tissemsilt',
 'khenchela',
 'souk ahras',
 'tipaza',
 'mila',
 'ain defla',
 'naama',
 'ain temouchent',
 'ghardaia',
 'relizane']
for i in wilayat:
  des = "<strong>" + str(i[0]).upper() + str(i[1:])+ "</strong><br>temperature: " + str(weather(i)[-1])[:2] +" °C <br>" + str(weather(i)[2])
  folium.Marker(location=[weather(i)[0], weather(i)[1]],popup=des).add_to(m)
