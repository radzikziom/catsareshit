# importowanie OpenCV
import cv2  # pip install opencv-python

# string ze ścieżką do pliku konfiguracyjnego XML
# jeśli jest w głównym folderze to po prostu nazwa pliku
rawPathToHaar = "haarcascade_frontalcatface.xml"


def Process_image(image):
    # Konwersja obrazka na czarno-biały kolor
    grayCat = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # załadowanie pliku konfiguracyjnego XML
    detector = cv2.CascadeClassifier(rawPathToHaar)
    # rozpoznawanie czarnobiałego obrazka
    rects = detector.detectMultiScale(grayCat, scaleFactor=1.3, minNeighbors=10, minSize=(75, 75))
    # zwracamy liste z tuplami (miejsca na obrazku gdzie mają być narysowane kwadraty)
    return rects


def is_cat(cats):
    if len(cats):  # len(cats) != 0
        output = 'Pomyślnie wykryto koty na zdjęciu. Liczba kotów: {}.'.format(len(cats))
        print(output)
        return True
    else:  # len(cats) == 0
        output = 'Nie wykryto żadnego kota na zdjęciu'
        print(output)
        return False


def draw(catImage, rects):
    for (i, (x, y, w, h)) in enumerate(rects):
        cv2.rectangle(catImage, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(catImage, "Cat #{}".format(i + 1), (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)


def replaceChar(source):
    path = source.replace("\\", "/")
    return path


def main(path):
    #path = "images\cat_1.jpg"
    rawPathToImage = replaceChar(path)
    image = cv2.imread(rawPathToImage)
    cats = Process_image(image)
    result = is_cat(cats)
    return result


# path = "images\cat_"
# for photo in range(1, 11):
#     path = path + str(photo) + ".jpg"
#     main(path)
#     path = "images\cat_"
