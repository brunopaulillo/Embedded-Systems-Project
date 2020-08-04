import face_recognition
import os

def load_images(known_images):
    known_dir = "/diretorio/imagens" # Diretório contendo todas as imagens conhecidas
    directory = os.fsencode(known_dir)

    # These lists will hold the image files and their encodings

    # Carrega todas as imagens conhecidas
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        known_images.append(face_recognition.load_image_file(known_dir + filename))

def load_unknown_image(known_images, known_encodings, unknown_face):
    # Carrega a imagem desconhecida
    unknown_image = face_recognition.load_image_file(unknown_face)
    # Tenta codificar todas as imagens
    try:
        #Se as codificações conhecidas estiverem vazias, codifica todas as imagens conhecidas
        if not known_encodings:
            for image in known_images:
                known_encodings.append(face_recognition.face_encodings(image)[0]) #primeira face
        #Codificações já carregadas
        unknown = face_recognition.face_encodings(unknown_image)[0]
    except IndexError:
            print("Não foi possivel encontrar rostos")
            quit()
    return unknown

def person_recognition(unknown, known_encodings):
    results = face_recognition.compare_faces(known_encodings, unknown)

    # Verifica se há uma correspondência válida
    for match in results:
        if match:
            return True
            quit()
        else:
            return False