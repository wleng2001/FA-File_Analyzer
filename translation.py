translation_dict={
    "exit":{
        "PL":"\nŻyczymy miłego dnia\nProgram wykonali:\nKamil Grodzki",
        "EN":"\nWish you a nice day\nProgram is written by:\nKamil Grodzki"},
    "start":
        {"PL":"",
         "EN":""},
    "help":
        {"PL":"\nhelp -> wyświetla to okno\n1 -> wyznaczanie pików wykresu\n2 -> zamień separatory dziesiętne na wybrany\nc -> utwórz plik\no -> otwórz plik\ns -> ustawienia\nexit lub 0 -> wyjście",
         "EN":"\nhelp -> display the screen\n1 -> search graph peaks\n2 -> change decimal separator to choosen\nc -> create file\no -> open file\ns -> settings\nexit or 0 -> exit"},
    "language":
        {"PL":"Dostępne języki: \npolski - PL\nEnglish - EN",
         "EN":"Availible language: \npolski - PL\nEnglish - EN"},
    "sep_ask":
        {"PL":"Wybierz separator dziesiętny (./,): ",
         "EN":"Choose decimal separator (./,): "},
    "gui":
        {"PL":"Czy chcesz uruchomić graficzny interfejs użytkownika? (1->tak/0->nie)",
         "EN":"Do you want enable GUI? (1->yes/0->no)"},
    "create_file":
        {"PL":"Podaj nazwę pliku do utworzenia(z rozszerzeniem): ",
        "EN":"Give file name to create(with file extension): "},
    "open_file":
        {"PL":"Podaj nazwę pliku do otwarcia(z rozszerzeniem): ",
        "EN":"Give file name to open(with file extension):"},
    "close_file":
        {"PL":"Plik %s został zamknięty pomyślnie",
        "EN":"File %s is closed correctly"},
    "settings":
        {"PL":"Ustawienia: \nl -> ustaw język\nd -> ustaw separator dziesiętny",
         "EN":"Settings: \nl-> set language\d -> set decimal separator"},
    "error":{"PL":"BŁĄD","EN":"ERROR"},
    "inc_format":
        {"PL":"Nieprawidłowy format (zbyt długi/krótki tekst lub niedozwolone znaki)",
         "EN":"Wrong text format (too short/long text or not allowe sign)"},
    "out_range":
        {"PL":"Wartość poza zakresem",
         "EN":"Value out of the range"},
    #peaks finder----
    "ask_peaks_amount":
        {"PL":"Podaj ilość szukanych pików (0=nie podaje ile znalazł): ",
         "EN":"Give how many peaks search (0=don't check it): "},
    "peaks_amount":
        {"PL":"Znaleziono %d pików a szukano %d pików",
         "EN":"Program finds %i peaks and it searched %i peaks"},
    #add_line----
    "data_sep":
        {"PL":"Jaki separator oddziela dane w wierszu:",
        "EN":"What separator divide data in line:"},
    "header_look":
        {"PL":"Tak wyglądają nagłówki: ",
         "EN":"Headers look: "},
    "data_jump":
        {"PL":"Jaki ma być skok wartości między wierszami: ",
        "EN":"Jump of value behing lines: "},
    }

#translation
def print_tr(lng, text_name):
    print(translation_dict[text_name][lng])

def comma_dot(data,change_sign):
    if data!='':
        if change_sign==',':
            data=data.replace('.',',')
        if change_sign=='.':
            data=data.replace(',','.')
            data=float(data)
    return data

def set_sep(ask, number, sep, lng):
    if ask==number:
        while True:
            info=translation_dict["sep_ask"][lng]
            ask=input(info)
            if ask!=None and len(ask)==1:
                if ask=="." or ask==",":
                    return ask
                else:
                    print_tr(language,"error")
                    print_tr(language,"inc_format")
            else:
                print_tr(language,"error")
                print_tr(language,"inc_format")
    return sep
            
