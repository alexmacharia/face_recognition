import PIL.Image
import PIL.ImageDraw
import face_recognition

# Load jpg file into numpy array
image = face_recognition.load_image_file("people.jpg")

# Find all faces in image
face_locations = face_recognition.face_locations(image)

num_faces = len(face_locations)
print("Found {} faces in this photo".format(num_faces))

# Load image into PIL for drawing and displaying it
pil_image = PIL.Image.fromarray(image)

for location in face_locations:
    # Print co-ordinates of each image
    top, right, bottom, left = location
    print("Top: {}, Right: {}, Bottom: {}, Left: {}".format(top, right, bottom, left))

    # Draw box around face
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle([left, top, right, bottom], outline="red")

# Display the image
pil_image.show()
