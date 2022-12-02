configured=False
language=""
sep=""
GUI=False

#end config section
#check configure

def change(var_n, new_value):
    if type(new_value)==str:
        new_value='"'+new_value+'"'
    file_t=[]
    file=open('config.py', 'r')
    file_t=file.read().split('\n')
    for i in range(0,len(file_t)):
        if file_t[i]!="end config section":
            if var_n in file_t[i]:
                file_t[i]=var_n+'='+str(new_value)
        else:
            break
    file=open('config.py', 'w')
    for i in file_t:
        file.write(i+'\n')
    file.close()





























