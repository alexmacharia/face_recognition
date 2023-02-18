import face_recognition

# Load the known images
person_1 = face_recognition.load_image("person_1.jpg")
person_2 = face_recognition.load_image("person_2.jpg")
person_3 = face_recognition.load_image("person_3.jpg")

# Get the face encoding of each person
person_1_encoding = face_recognition.face_encodings(person_1)[0]
person_2_encoding = face_recognition.face_encodings(person_2)[0]
person_3_encoding = face_recognition.face_encodings(person_3)[0]

# Create a
