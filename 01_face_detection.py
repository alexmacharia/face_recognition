import PIL.Image
import PIL.ImageDraw
import face_recognition

# Load jpg file into numpy array
image = face_recognition.load_image_file("people.jpg")

# Find all faces in image
face_locations = face_recognition.face_locations(image)

num_faces = len(face_locations)
print("Found {} faces in this photo".format(num_faces))
