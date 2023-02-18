import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("person.jpg")

# Generate face encodings
face_encodings = face_recognition.face_encodings(image)

if len(face_encodings) == 0:
    print("No faces were found")

else:
    first_face_encoding = face_encodings[0]

    print(first_face_encoding)
