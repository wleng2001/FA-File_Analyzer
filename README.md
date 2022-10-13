# File_Analyzer
## Description
 It's program in python, which analyze *.txt file. At the moment it search peaks in file and save them to other file in csv format. If you know polish you find polish version instruction at the bottom of the document.
## Instalation
### Linux device
You can clone it in linux devices: 

#### `git clone https://github.com/wleng2001/File_analyzer.git ./FA`

or download as a zip file on the github webpage.

Next you must check, that you have python download. You can check it by writting the information in terminal: 

#### `python3 --version` to check if you have python

You should get information similary to that:

#### `Python 3.9.7`

If you don't have download python you can do it <a href="https://www.python.org/downloads/">here</a> or you can write the text in terminal:

#### `sudo apt install python3`

### Windows device

On the windows devices you can download zip file from github and unpack it.
Next you must check, that you have python download. You can check it by writting the information in terminal: 

#### `python --version` to check if you have python

You should get information similary to that:

#### `Python 3.9.7`

If you don't have download python you can do it <a href="https://www.python.org/downloads/">here</a>.

## Usage

## PL
## Opis
Jest to prosty program napisany w pythonie do analizy plików *.txt. Na ten moment wyszukuje wartości maksymalnych dla wskazanego pliku i zapisuje je w pliku w formacie csv.
## Instalacja
### Na linuxie
W celu zainstalowania oprogramowania musisz posiadać zainstalowany na urządzeniu interpreter języka python. Aby sprawdzić czy jest zainstalowany wpisz w terminalu:
#### `python3 --version`
Powinieneś otrzymać wynik podobny do tego:
#### `Python 3.9.7`
W innym wypadku wpisz:
#### `sudo apt install python3`
Aby pobrać oprogramowanie wpisz w terminalu:
#### `git clone https://github.com/wleng2001/File_analyzer.git ./FA` (może być konieczne doinstalowanie git)
lub pobierz plik zip i rozpakuj w eksploratorze plików.
### Na windowsie
W celu zainstalowania oprogramowania musisz posiadać zainstalowany na urządzeniu interpreter języka python. Aby sprawdzić czy jest zainstalowany wpisz w cmd (otwiera się poprzez wpisane cmd  i potwierdzenie po naciśnięciu klawisza **win**):
#### `python --version`
Powinieneś otrzymać informację podobną do tej:
#### `Python 3.9.7`
Jeśli nie, oprogramowanie możesz pobrać spod tego <a href="https://www.python.org/downloads/">linku</a>.
Program możesz pobrać poprzez kliknięcie **code** na tej stronie a potem **Download ZIP**. Następnie rozpakuj go przy pomocy eksploratora.

## Użytkowanie
Program uruchamia się klikając w jego ikonę lub w systemie linux poprzez:
#### `sudo python3 [lok]/File_analyzer.py` gdzie lok to ścieżka do programu
Po uruchominu zostaniesz poproszony o wybranie wersji językowej:
####
```
Availible language:
polski - PL
English - EN
Choose language (by code):
```
Wyboru dokonujemy poprzez wpisanie kodu języka (program wyświetla dostępne języki i ich kody).
Po czym program zapyta o separator dziesiętny:
####
```
Wybierz separator dziesiętny (./,):
```
Po wyborze separatora wyświetlą się dostępne funkcje programu i znak zachęty, aby wybrać funkcję:
####
```
help -> wyświetla to okno
1 -> wyznaczanie pików wykresu
c -> utwórz plik
o -> otwórz plik
s -> ustawienia
exit lub 0 -> wyjście
->
```
Wybierjąc opcję *1* program zapyta cię o plik, który chcesz analizować
#### `Podaj nazwę pliku do otwarcia(z rozszerzeniem): ` Wpisując jego nazwę (z rozszerzeniem) pamiętaj, aby znajdował sięw tym samym folderze co program!
W drugiej kolejności zostaniesz poproszony o ilość szukanych wartości maksymalnych:
#### `Podaj ilość szukanych pików (0=nie podaje ile znalazł): `
Jeśli wpiszesz 0 nie pokaże tego podsumowania z tym ile znalazł wartości maksymalnych:
#### `Znaleziono 41 pików a szukano 40 pików`
Następnie program poprosi o nazwę pliku z rozszerzeniem do jakiego ma być zapisany wynik pracy (proponuję rozszerzenie csv co pozwoli na otwarcie pliku w excelu/calc):
#### `Podaj nazwę pliku do utworzenia(z rozszerzeniem):`
Aby zapisać plik należy wyjść z programu poprzez wpisanie *0* lub *exit* po pokazaniu się znaku zachęty *->*. Wówczas program zamknie plik i pokaże twórców:
####
```
->exit

Plik x został zamknięty pomyślnie

Życzymy miłego dnia
Program wykonali:
Kamil Grodzki
```
