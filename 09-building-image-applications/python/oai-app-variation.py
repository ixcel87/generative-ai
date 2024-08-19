from openai import OpenAI
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

openai = OpenAI()

image_dir = os.path.join(os.curdir, 'images')

# Initialize the image path (note the filetype should be png)
image_path = os.path.join(image_dir, 'generated-image2.png')

print(f'This is the image_path => {image_path}\n')

# ---creating variation below---
try:
    print("LOG creating variation")
    response = openai.images.create_variation(
        # image=open("./images/generated-image2.png", "rb"),
        image=open(image_path, "rb"),
        n=1,
        size="1024x1024"
    )

    image_path = os.path.join(image_dir, 'generated_variation2.png')

    image_url = response.data[0].url

    print("LOG downloading image")
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()
except openai.error.InvalidRequestError as err:
    print(err)