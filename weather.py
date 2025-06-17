import requests
import shutil
import json

class LlamadosInternet:

    def mi_primer_request(self):
        url='https://www.google.com/search?q=frenchies+lilac&sca_esv=e833def03aa227c2&udm=2&biw=1280&bih=889&ei=CuYwaMD-A_G_kPIP9KmvsA0&ved=0ahUKEwjAq_yQwrqNAxXxH0QIHfTUC9YQ4dUDCBE&uact=5&oq=frenchies+lilac&gs_lp=EgNpbWciD2ZyZW5jaGllcyBsaWxhYzIHEAAYgAQYEzIIEAAYExgIGB4yCBAAGBMYCBgeMggQABgTGAgYHjIIEAAYExgIGB4yCBAAGBMYCBgeMggQABgTGAgYHjIIEAAYExgIGB4yCBAAGBMYCBgeMggQABgTGAgYHkilH1CXAVjcGXACeACQAQCYAW6gAd4FqgEDMC43uAEDyAEA-AEBmAIJoAKxBsICBhAAGAcYHsICEBAAGIAEGLEDGEMYgwEYigXCAgUQABiABMICChAAGIAEGEMYigXCAgkQABiABBgTGArCAgoQABgTGAgYChgewgIEEAAYHsICBhAAGAgYHpgDAIgGAZIHAzIuN6AH-ymyBwMwLje4B6IG&sclient=img#vhid=0q7BKFsjsGf5wM&vssid=mosaic'
        r=requests.get(url)
        print(r)
        print(r.content)
        print(r.status_code)

    def descargar_img(self, url, file_name):
        res=requests.get(url,stream=True)
        if res.status_code == 200:
            with open(file_name,'wb')as f:
                shutil.copyfileobj(res.raw,f)
            print('imagen descargada correctamente')
        else:
            print('No se encontro la imagen')

    def get_weather(self,city,api_key):
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        params = {"q": city, "appid": api_key, "units": "metric"}

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()

            weather_data = response.json()

            if weather_data["cod"] == 200:
                print(f"Weather ins {weather_data['name']}:")
                print(f"  Description: {weather_data['weather'][0]['description']}")
                print(f"  Temperature: {weather_data['main']['temp']}°C")
                print(f"  Humidity: {weather_data['main']['humidity']}%")
                print(f"  Viento: {weather_data['wind']['speed']}m/s")
            else:
                    print(f"Error: {weather_data['message']}")

        except:
            print('error')

url = 'https://premierpups.com/azure/premierphotos/pups/lilac-french-bulldog-full-guide-where-to-find-one-premierpups-637852751042797908.png'
res = LlamadosInternet()
res.descargar_img(url,'imagen.jpg')
city = "zapopan"
api_key = "69ec8ca2037d63a120d31c59efd0f604"
res.get_weather(city,api_key)

