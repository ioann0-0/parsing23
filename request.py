import os
import requests
from PIL import Image
from io import BytesIO

output_folder = 'images_requests'
os.makedirs(output_folder, exist_ok=True)

url = 'https://picsum.photos/200'

for i in range(10):
    response = requests.get(f'{url}?random={i}', stream=True)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.save(os.path.join(output_folder, f'image_{i+1}.jpg'))
    else:
        print(f'Не удалось загрузить изображение {i+1}')
