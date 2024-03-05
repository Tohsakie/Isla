import os
import requests
import json
from PIL import Image
import pytest

def extract_weather_info(city_name='Ales', country_code='fr'):
    if city_name == None or country_code == None:
        raise ValueError('city_name or country_code can not be None')

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&units=metric&APPID=2d3d5aeb234b063ead95987c29dca31a"
    try:
        response = requests.get(url)
        data = response.json()
        weather_main = data['weather'][0]['main']
        weather_description = data['weather'][0]['description']
        weather_icon = data['weather'][0]['icon']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        city_name = data['name']
        return {
            'weather_main': weather_main,
            'weather_description': weather_description,
            'weather_icon': weather_icon,
            'temp_min': temp_min,
            'temp_max': temp_max,
            'city_name': city_name
        }
    except KeyError as e:
        print(f"KeyError: {e} is missing in the provided JSON data.")
        return None
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        return None


def get_weather_image(weather_icon_url, file_name='weather_icon'):
    if not os.path.isdir('images'):
        os.mkdir('images')
    response = requests.get(weather_icon_url)
    with open(f'images/{file_name}.png', 'wb') as f:
        f.write(response.content)


def create_weather_image(weather_icon_url, file_name):
    get_weather_image(weather_icon_url, file_name)

    # Ouvrir l'image téléchargée
    weather_image = Image.open(f'images/{file_name}.png')

    # Créer une nouvelle image avec la taille requise
    final_image = Image.new('RGBA', (weather_image.width * 3, weather_image.height * 3), (255, 255, 255, 0))

    # BAS
    rotated_image = weather_image.rotate(180, expand=True)
    final_image.paste(rotated_image, (weather_image.width, weather_image.height * 2))

    # GAUCHE
    rotated_image = weather_image.rotate(90, expand=True)
    final_image.paste(rotated_image, (0, weather_image.height))

    # DROITE
    rotated_image = weather_image.rotate(270, expand=True)
    final_image.paste(rotated_image, (weather_image.width*2, weather_image.height))

    # HAUT
    final_image.paste(weather_image, (weather_image.width, 0))

    # Enregistrer l'image finale
    final_image.save(f'images/final_{file_name}.png')


def test_extract_weather_info():
    with pytest.raises(ValueError):
        extract_weather_info(None)
        extract_weather_info('Ales', None)

    result = extract_weather_info('Ales')
    assert result['weather_main'] != None
    assert result['weather_description'] != None
    assert result['weather_icon'] != None
    assert result['temp_min'] != None
    assert result['temp_max'] != None
    assert result['city_name'] != None
