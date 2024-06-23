# animal_image.py
import requests

def get_animal_image_url(animal_type):
    if animal_type == 'duck':
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
    elif animal_type == 'dog':
        url = 'https://random.dog/woof.json'
        res = requests.get(url)
        data = res.json()
        return data['url']
    # Diğer hayvan türlerini buraya ekleyebilirsiniz
    else:
        return None
