
# importowanie OpenCV
import cv2          # pip install opencv-python

# string ze ścieżką do pliku konfiguracyjnego XML
# jeśli jest w głównym folderze to po prostu nazwa pliku
rawPathToHaar = "haarcascade_frontalcatface.xml"


def Process_image(catImage):
    # Konwersja obrazka na czarno-biały kolor
    grayCat = cv2.cvtColor(catImage, cv2.COLOR_BGR2GRAY)
    # załadowanie pliku konfiguracyjnego XML
    detector = cv2.CascadeClassifier(rawPathToHaar)
    # rozpoznawanie czarnobiałego obrazka
    rects = detector.detectMultiScale(grayCat, scaleFactor=1.3, minNeighbors=10, minSize=(75, 75))
    # zwracamy liste z tuplami (miejsca na obrazku gdzie mają być narysowane kwadraty)
    return rects


def is_cat(cats):
    if len(cats):  # len(cats) != 0
        return cats
    # Przykładowe narysowanie obrazka z kwadratami:
    #     image -> obrazek wyjściowy
    #     cats -> lista 4-tuples. Tuple zawierają współrzędne (x, y) oraz szerokość i wysokość każdej wykrytej twarzy kota.
    #     draw(image, cats)
    #     cv2.imshow("Cat Faces", image)      Pokazanie okienka
    #     cv2.waitKey(0)                      Oczekiwanie aż użytkownik sam zamknie nowo otwarte okno

    # def draw(image, rects):
    #     for (i, (x, y, w, h)) in enumerate(rects):
    #         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #         cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10),
    #                     cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    else:  # len(cats) == 0
        return False


# ścieżka do obrazka ZAPISANEGO na serwerze
path = "path"

"""
zamiana \ ze ścieżki na / obsługiwane przez Pythona
w sumie lepiej jakby zrobić to po stronie serwera przed przekazaniem adresu 
"""
rawPathToImage = path.replace("\\", "/")
# OpenCV wczytuje obrazek
image = cv2.imread(rawPathToImage)
# Rozpoznanie obrazka -> cats przechowuje zwracaną listę tupli
catsList = Process_image(image)
# Sprawdzamy czy zostało coś wpisane do listy i zwracamy wynik do serwera
result = is_cat(catsList)
# result przechowuje wynik analizy zdjęcia
