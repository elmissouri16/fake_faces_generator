import os

import requests


#  function to create folder if not exists
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# function to download image using requests


def download_image(url, file_name):
    try:
        rsp = requests.get(url)
        if rsp.status_code == 200:
            with open(file_name, 'wb') as f:

                f.write(rsp.content)
                f.close()
                return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

# get rabdom face image from fakeface api


def get_face():
    url = 'https://fakeface.rest/face/json'
    rsp = requests.get(url)
    if rsp.status_code == 200:
        data = rsp.json()
        return {'file': data['filename'], 'url': data['image_url']}
    else:
        return None


if __name__ == '__main__':

    create_folder('images')

    number_of_images = input(
        'Enter the number of images you want to download : ')
    for i in range(int(number_of_images)):
        face = get_face()
        if face:
            try:
                rsp = download_image(face['url'], 'images/' + face['file'])
                if rsp:
                    print('Downloaded image : ' + face['file'])

            except Exception as e:
                print(e)
                print('Error Skipping')
