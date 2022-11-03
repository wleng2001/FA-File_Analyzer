#program to analyze graphs

#---------------------library import
from time import sleep
from math import *

#---------------------variables

prompt="->"
language="EN"
availible_lng=["PL","EN"]
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
    "create_file":
        {"PL":"Podaj nazwę pliku do utworzenia(z rozszerzeniem): ",
        "EN":"Give file name to create(with file extension):"},
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
    }

#---------------------variables

close_file=True
w_file_name=""
w_file=None
o_file_name=""
o_file=None
o_file_c=""
sep=""
#---------------------function
#input

def check_input(text):
    global sep
    if sep==',':
        text=text.replace(",",".")
    try:
        text=float(text)
        return text
    except:
        return None

def change_output(text, sep):
        text=str(text)
        if sep==",":
            text=text.replace(".",",")
        else:
            text=text.replace(",",".")
        return text
        
#change sep in file

def change_sep_in_file(ask, number, file_name, file, contents):
    if ask==number:
        if sep==",":
            sep_to_change="."
        else:
            sep_to_change=","
        file_name, file, contents=open_file(0,0, file_name, file, contents)
        contents_c=contents.split('\n')
        for i in range(0,len(contents_c)):
            temp_line=""
            for j in range(0,len(contents_c[i])):
                if j>0 and j<len(contents_c[i]):
                    if contents_c[i][j]==sep_to_change and ord(contents_c[i][j-1])>=48 and ord(contents_c[i][j-1])<=57 and ord(contents_c[i][j+1])>=48 and ord(contents_c[i][j+1])<=57:
                        temp_line+=sep
                    else:
                        temp_line+=contents_c[i][j]
                else:
                    temp_line+=contents_c[i][j]
            contents_c[i]=temp_line+'\n'
            copy_file(file_name, file, contents_c)
        
    return file_name, file, contents
    

#math function of program

def rm_text_line(table):
    new_table=[]
    for i in range(len(table)):
        if table[i]!="" and ord(table[i][0])>=48 and ord(table[i][0])<=57:
            new_table.append(table[i])
    return new_table

def search_peaks(table):
    what_counter=10
    peaks=[0]
    peaks[0]=float(table[0])
    peak_n=len(peaks)
    pre_previou_n=0
    previous_n=float(table[0])
    counter=10 #counter from number set as max
    for i in table:
        i=float(i)
        if previous_n>i and previous_n>pre_previous_n:
            if previous_n<peaks[peak_n-1] and counter>0:
                pass
            elif previous_n>peaks[peak_n-1] and counter>0:
                    peaks[peak_n-1]=previous_n
                    counter=what_counter
            else:
                peaks[peak_n-1]=previous_n
                peak_n=len(peaks)
                peaks.append(0)
                counter=what_counter

        if counter>0:
            counter=counter-1
        pre_previous_n=previous_n
        previous_n=i
    return peaks[:-2], peak_n-2
        

def find_peaks(ask, number, o_file_name, o_file, o_file_c, w_file_name, w_file, close_file):
    while True:
        if ask==number:
            while o_file==None:
                o_file_name, o_file, o_file_c=open_file(0,0,o_file_name, o_file, o_file_c)
            o_file_c=o_file_c.split("\n")
            o_file_c=rm_text_line(o_file_c)
            o_file_c_copy=o_file_c
            o_file_c=[]
            for i in o_file_c_copy:
                o_file_c.append(change_output(i,"."))
            peaks_amount=None
            while peaks_amount==None:
                peaks_amount=check_input(input(translation_dict["ask_peaks_amount"][language]))
                if peaks_amount==None:
                    print_tr(language, "error")
                    print_tr(language, "inc_format")
            peaks, peaks_n=search_peaks(o_file_c)
            if peaks_amount!=0:
                print(translation_dict["peaks_amount"][language] %(peaks_n, peaks_amount))
            while w_file==None:
                w_file_name,w_file=create_file(0,0,w_file_name,w_file)
            gen_csv(sep, w_file, peaks)
            close_file=False
            return w_file_name, w_file, close_file
            
        else:
            return w_file_name, w_file, close_file

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
            

#file
def create_file(ask, number, file_name, file):
    global close_file
    if ask==number:
        info=translation_dict["create_file"][language]
        file_name=input(info)
        if file_name=="" or None:
            return file_name, file
        file=open(file_name, 'w')
        close_file=False
        return file_name, file
    return file_name, file

def open_file(ask, number, file_name, file, contents):
    if ask==number:
        info=translation_dict["open_file"][language]
        if contents=="":
            file_name=input(info)
            try:
                file=open(file_name, 'r')
                contents=file.read()
                return file_name, file, contents
            except:
                return file_name, file, contents
    return file_name, file, contents

def gen_csv(*data):
    #firs data to function must be sign of decimal separator!
    cell_sep=""
    sep=data[0]
    w_file=data[1]
    data=data[2:]
    if sep==".":
        cell_sep=","
    else:
        cell_sep=";"
    for i in range(len(data[0])):
        w_file.write(change_output(data[0][i],sep)+cell_sep+'\n')

def copy_file(file_name, file, contents): #contents must by table
    file=open(file_name, 'w')
    for i in contents:
        file.write(i)
    file.close()

#settings
def set_language(ask,number):
    while True:
        if ask==number:
            print_tr(language, "language")
            text=input("Choose language (by code): ").upper()
            if len(text)!=2:
                print_tr(language,"error")
                print_tr(language,"inc_format")
            else:
                for i in availible_lng:
                    if i==text:
                        return text
                print_tr(language,"error")
                print_tr(language,"out_range")
        else: break

def settings(ask, number, lng, sep):
    prompt="s->"
    while True:
        if ask==number:
            print_tr(lng, "settings")
            ask=input(prompt)
            lng=set_language(ask, "l")
            sep=set_sep(ask, "d", sep, lng)
            return lng, sep
        else:
            return lng, sep

def example(ask, number):
    prompt="s->"
    while True:
        if ask==number:
            print_tr(language, "settings")
            ask=input(prompt)
        else: break

def close_app(number,ask, file, file_name):
    if ask==number or ask=="exit":
        if close_file==False:
            file.close()
            print('')
            print(translation_dict["close_file"][language] %file_name)
            sleep(2)

        print_tr(language, "exit")
        sleep(3)
        exit()

#---------------------program
language=set_language(0,0)
sep=set_sep(0,0,sep, language)
print_tr(language,"help")
while True:
    ask=input(prompt)
    w_file_name, w_file, close_file=find_peaks(ask,"1", o_file_name, o_file, o_file_c,  w_file_name, w_file, close_file)
    o_file_name, o_file, o_file_c=change_sep_in_file(ask, "2", o_file_name, o_file, o_file_c)
    w_file_name, w_file=create_file(ask, "c", w_file_name, w_file)
    o_file_name, o_file, o_file_c=open_file(ask,"o", o_file_name, o_file, o_file_c)
    language, sep=settings(ask,"s", language, sep)
    close_app("0",ask, w_file, w_file_name)
    if ask=="help":
        print_tr(language,"help")         
