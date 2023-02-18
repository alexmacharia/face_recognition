import PIL.Image
import PIL.ImageDraw
import face_recognition

# Load jpg file into numpy array
image = face_recognition.load_image_file("people.jpg")

# Find all facial features in all the faces in the image
face_landmarks = face_recognition.face_landmarks(image)

num_faces = len(face_landmarks)
print("Found {} faces in this photo".format(num_faces))

# Load image into PIL object inorder to draw on it and display it
pil_image = PIL.Image.fromarray(image)

# Create a PIL drawing object
draw = PIL.ImageDraw.Draw(pil_image)

# Loop over each face
for landmark in face_landmarks:

    # Loop over each facial feature
    for name, points in landmark.items():

        # Print the location of each facial feature in this image
        print("The {} in this face has the following points: {}".format(name, points))

        draw.line(points, fill="red", width=2)

pil_image.show()