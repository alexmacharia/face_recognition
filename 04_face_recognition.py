import face_recognition

# Load the known images
person_1 = face_recognition.load_image_file("person_1.jpg")
person_2 = face_recognition.load_image_file("person_2.jpg")
person_3 = face_recognition.load_image_file("person_3.jpg")

# Get the face encoding of each person
person_1_encoding = face_recognition.face_encodings(person_1)[0]
person_2_encoding = face_recognition.face_encodings(person_2)[0]
person_3_encoding = face_recognition.face_encodings(person_3)[0]

# Create a list of known face encodings
known_face_encodings = [
    person_1_encoding,
    person_2_encoding,
    person_3_encoding
]

# Load the image we want to check
unknown_image = face_recognition.load_image_file("unknown_8.jpg")

# Get face encodings for the faces in the image
unknown_encodings = face_recognition.face_encodings(unknown_image)

# Loop over each face in the image
for face_encoding in unknown_encodings:

    # Test if unknown face matches any of the three people
    results = face_recognition.compare_faces(known_face_encodings,
                                             face_encoding, tolerance=0.6)
    name = "Unknown"

    if results[0]:
        name = "Person 1"
    elif results[1]:
        name = "Person 2"
    elif results[2]:
        name = "Person 3"

    print(f"Found {name} in the photo!")