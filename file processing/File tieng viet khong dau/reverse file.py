import  aes_function
with open('File chua gia tri chuyen doi.txt','r',encoding = 'UTF-8') as changetext, open('File chua gia tri tra ve.txt','w',encoding = 'UTF-8') as originaltext:
    ct = changetext.read()
    temp = ''
    eight_b_lst =[]
    for i in ct:
        temp += i
    for i in range(0,len(temp),8):
        eight_b_lst.append((aes_function.bintodec(int(temp[i:i+8]))))
    text =''
    for i in eight_b_lst:
        text += chr(int(i))
    originaltext.write(text)
