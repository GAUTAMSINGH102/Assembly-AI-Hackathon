import requests

def generate_image_func(promptarr):
    imagearr = []
    for prompt in promptarr:

        url = "https://lexica.art/api/v1/search?q={}".format(prompt)

        response = requests.request("GET", url)
        data = response.json()
        imageURL = data['images'][0]['src']

        imagearr.append(imageURL)
    
    return imagearr