from PIL import Image, ImageDraw
import face_recognition

# Load image into numpy array
image = face_recognition.load_image_file("people.jpg")

# Find all facial features in all the faces
face_landmarks_list = face_recognition.face_landmarks(image)

# Load the image into a PIL object inorder to draw on it
pil_image = Image.fromarray(image)

# Create a PIL drawing object
d = ImageDraw.Draw(pil_image, 'RGBA')

for face_landmarks in face_landmarks_list:

    # Draw line over the eyebrows
    d.line(face_landmarks['left_eyebrow'], fill=(128, 0, 128, 100), width=3)
    d.line(face_landmarks['right_eyebrow'], fill=(128, 0, 128, 100), width=3)

    # Draw over the lips
    d.polygon(face_landmarks['top_lip'], fill=(128, 0, 128, 100))
    d.polygon(face_landmarks['bottom_lip'], fill=(128, 0, 128, 100))

# Show final image
pil_image.show()