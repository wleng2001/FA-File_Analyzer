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
#### `python3 --veresion`
Powinieneś otrzymać wynik podobny do tego:
#### `Python 3.9.7`
W innym wypadku wpisz:
#### `sudo apt install python3`
Aby pobrać oprogramowanie wpisz w terminalu:
#### `git clone https://github.com/wleng2001/File_analyzer.git ./FA` (może być konieczne doinstalowanie git)
lub pobierz plik zip i rozpakuj w eksploratorze plików.
### Na windowsie
W celu zainstalowania oprogramowania musisz posiadać zainstalowany na urządzeniu interpreter języka python. Aby sprawdzić czy jest zainstalowany wpiszw cmd (otwiera się poprzez wpisane cmd  i potwierdzeniepo naciśnięciu klawisza **win**):
#### `python --version`
Powinieneś otrzymać informację podobną do tej:
#### `Python 3.9.7`
Jeśli nie oprogramowanie możesz pobrać spod tego <a href="https://www.python.org/downloads/">linku</a>.
Program możesz pobrać poprzez kliknięcie **code** na tej stronie a następnie **Download ZIP**. Następnie rozpakuj go przy pomocy eksploratora.

## Użytkowanie
Program uruchamia się poprzez kliknięcie w jego ikonę lub w systemie linux:
#### `sudo python3 [lok]` gdzie lok to ścieżka do programu
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
Po wyborze separatora wyświetlą się dostępne funkcje porgramu i znak zachęty, aby wybrać funkcję:
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
