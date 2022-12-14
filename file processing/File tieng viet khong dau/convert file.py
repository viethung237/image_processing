import aes_function
def change(value):

    if len(value) != 8 :
        k = len(value)
        for i in range(8 - k):
            value = '0' + value
    return value

with open('tieng viet co dau.txt','r',encoding = 'UTF-8') as plaintext, open('File chua gia tri chuyen doi.txt','w',encoding = 'UTF-8') as changetext:
    pt = plaintext.read()

    #chuyen ve chuoi bin
    value_lst =[]
    bin_str =''
    for i in pt :
        value_lst.append(bin(ord(i)).replace('0b',''))
    for i in range(len(value_lst)):
        value_lst[i] = change(value_lst[i])
        bin_str += value_lst[i]
    changetext.write(bin_str)

