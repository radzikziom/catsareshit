# Cat-or-not-Cat
Projekt zespołowy, Inżynieria programowania 


```commandline
pip install opencv-python
```

## 
- Trzeba pamiętać że jak będziemy wysyłać stringa z ścieżką do pliku to backslashe '\' trzeaba pozamieniać na zwykłe slashe '/' 
Bo inaczej wszystko się wyłoży ``` rawPathToImage = path.replace("\\", "/")```

# Okienko z zaznaczonym kotem
- image -> obrazek wejściowy
- cats -> Wyjściowa lista, po przeanalizowaniu obrazka - lista 4-tuples. 
Tuple zawierają współrzędne (x, y) oraz szerokość i wysokość każdej wykrytej twarzy kota.
```def draw(image, rects):
for (i, (x, y, w, h)) in enumerate(rects):
         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
         cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10),
         cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)d model
```
```
draw(image, cats)
cv2.imshow("Cat Faces", image)      Pokazanie okienka - (tytuł, obrazek)
cv2.waitKey(0)                      Oczekiwanie aż użytkownik sam zamknie nowo otwarte okno 
                                    (czas aktywności okienka-> autoclose)
```
