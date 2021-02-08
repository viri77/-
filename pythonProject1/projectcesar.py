eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = input()
k = s.split()
b=[]
print(k)
sh = ''
for i in range(len(k)):
    count =0
    for j in range(len(k[i])):
        if k[i][j].isalpha():
            count+=1
    b.append(count)
print(*b)



for i in range(len(k)):

    for j in range(len(k[i])):

        if k[i][j].isalpha():

            if k[i][j] in eng_upper_alphabet:
                x = eng_upper_alphabet.find(k[i][j])
                st = x + b[i]
                if st > len(eng_upper_alphabet):
                    st -= len(eng_upper_alphabet)
                sh += eng_upper_alphabet[st]
            elif k[i][j] in eng_lower_alphabet:
                x = eng_lower_alphabet.find(k[i][j])
                st = x + b[i]

                if st >=len(eng_lower_alphabet):
                   st -= len(eng_lower_alphabet)

                sh += eng_lower_alphabet[st]

        else:
            sh += k[i][j]
print(sh)
