# FO-Kielbus-Wawrzyniak

## Konfiguracja
### Środowisko
- Python 3.11.8 lub wyższy
- Biblioteka ultralytics
```
pip install ultralytics
````

### Dane
- Utworzyć folder `data` w katalogu projektu
- Foldery z danymi (`train`, `valid` oraz `test`) w formacie YOLO umieścić folderze `data`
- W folderze `data` utworzyć plik `config.yaml`:
```
train: <folder projektu>\train\images
val: <folder projektu>\valid\images
test: <folder projektu>\test\images

nc: 8
names: ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']
```

## Uruchomienie
- Skrypt `train.py` pobierze model oraz rozpocznie jego trenowanie na danych z folderu data/train
- **Skrypt należy uruchamiać z terminala**, będąc w folderze głównym projektu