import aes_function

with open('tieng viet co dau.txt','r',encoding = 'UTF-8') as plaintext, open('File chua gia tri chuyen doi.txt','w',encoding = 'UTF-8') as changetext:
    pt = plaintext.read()
    value_lst =[]
    str_len =[]
    bin_str =''
    for i in pt :
        value_lst.append((bin(ord(i)).replace('0b','')))
    changetext.write(' '.join(str(i) for i in  value_lst))

with open('File chua gia tri chuyen doi.txt','r',encoding='UTF-8') as changetext, open('File chua gia tri tra ve.txt','w',encoding='UTF-8') as originaltext:
    ct = changetext.read()
    a_lst =''
    i_lst =[]
    for i in range(len(ct)) :
        if ct[i] == ' ':
            i_lst.append(str(i))
        else:
            i_lst.append('0')
    print(i_lst)
    temp = 0
    for i in range(len(ct)):
        if(i_lst[i] != '0') :
            a_lst += chr(int(aes_function.bintodec(int(ct[temp:i]))))
            temp = int(i_lst[i]) + 1
    a_lst += chr(int(aes_function.bintodec(int(ct[temp:]))))
    originaltext.write(a_lst)



