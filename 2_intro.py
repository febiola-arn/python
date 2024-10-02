# perulangan -> Looping

for baris in range (5) :
    for kolom in range (5):
        #jika end nya tidak di tambahkan maka hasil nya akan terurut ke bawah bukan kesamping
        print("*",end="")
    print()    

    

#while itu untuk perulangan yang lebih kecil dari 10
#while iteration -> need condition 

baris2 = 0
tengah = 5
while baris2 < 5 :
    kolom2 = 0 
    if(baris2 % 2 == 0):
        while kolom2 < 5:
            if(kolom2 == int(round(tengah/2))):
               print("*",end="")
            else:
                print(" ",end="")
            kolom2 += 1
    else:
        while kolom2 < 5 :
            print("*",end="")
            kolom2 += 1
    print()
    baris2 += 1

print("Hello World")

    


