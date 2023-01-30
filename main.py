import io
import os
from google.cloud import vision


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'just-ratio-374706-3ccd0dab8f4a.json'
# Imports the Google Cloud client library


# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('resources/wakeupcat.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)