#remove unnecesarry space

def rm_space(text):
    n_text=""
    if len(text)>2:
        pr_char=text[0]
        n_text+=pr_char
        for i in range(1,len(text)):
            if pr_text==" " and i==" ":
                pass
            else:
                n_text+=i
                pr_char=i
        return n_text
    return text

#find headers need text processed by rm_space()

def find_header(table, data_sep):
    previous_line=table[0]
    for i in range(1,len(table)):
        j=table[i].split(data_sep)
        try:
            int(j[-1])
        except:
            return j
    return headers, line

def rm_text_line(table):
    new_table=[]
    for i in range(len(table)):
        if table[i]!="" and ord(table[i][0])>=48 and ord(table[i][0])<=57:
            new_table.append(table[i])
    return new_table
