import face_recognition
from pathlib import Path
from PIL import Image

# Load image of the person we want to compare
known_image = face_recognition.load_image_file("test_face.jpg")

# Encode the image
known_image_encoding = face_recognition.face_encodings(known_image)[0]

# Variables to keep track of most similar face match
best_face_distance = 1.0
best_face_image = None

# Loop over all images to check for similarity
for image_path in Path("people").glob("*.png"):
    # Load the image
    unknown_image = face_recognition.load_image_file(image_path)

    # Get the face encodings
    face_encodings = face_recognition.face_encodings(unknown_image)

    # Get the distance between known image and all faces in the image
    face_distance = face_recognition.face_distance(face_encodings, known_image_encoding)[0]


    if face_distance < best_face_distance:
        best_face_distance = face_distance
        best_face_image = unknown_image

# Display the best match
pil_image = Image.fromarray(best_face_image)
pil_image.show()