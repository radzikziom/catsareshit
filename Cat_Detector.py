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
        output = 'Pomyślnie wykryto koty na zdjęciu.\nLiczba kotów: {}.'.format(len(cats))
        # print(output)  # do testowania lokalnie
        return output
    else:  # len(cats) == 0
        output = 'Nie wykryto żadnego kota na zdjęciu'
        # print(output)  # do testowania lokalnie
        return output


def replaceChar(source):
    path = source.replace("\\", "/")
    return path


# ścieżka do obrazka ZAPISANEGO na serwerze
# path = "path"
def main(path):
    """
    zamiana \ ze ścieżki na / obsługiwane przez Pythona
    w sumie lepiej jakby zrobić to po stronie serwera przed przekazaniem adresu
    """
    rawPathToImage = replaceChar(path)
    # OpenCV wczytuje obrazek
    image = cv2.imread(rawPathToImage)
    # Rozpoznanie obrazka -> cats przechowuje zwracaną listę tupli
    cats = Process_image(image)
    # Sprawdzamy czy zostało coś wpisane do listy i zwracamy wynik do serwera
    result = is_cat(cats)
    # result przechowuje wynik analizy zdjęcia
    return result
