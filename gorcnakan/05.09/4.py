time = int(input())
vaxt = input()
qani_jamic = int(input())
paho = time + qani_jamic
while (paho != 0):
    if(vaxt == 'am'):
        if(time + qani_jamic > 12):
            vaxt = 'pm'
            print(time +qani_jamic - 12, vaxt)
        elif(time + qani_jamic < 12):
            print(time + qani_jamic, vaxt)
    elif(vaxt == 'pm'):
        if(time + qani_jamic > 12):
            vaxt = 'am'
            print(time +qani_jamic - 12, vaxt)
        elif(time + qani_jamic < 12):
            print(time + qani_jamic, vaxt)
    paho -= 1        
       
   