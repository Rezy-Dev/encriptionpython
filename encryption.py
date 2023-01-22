word = input("Enter your word:\t")
task = input("What do you want to do? Encode or Decode?\t")
randomThreeString = "kJo"
randomThreeString2 = "fLw"

words = word.split(" ")


if(task.lower() == 'encode'):
    nwords = []
    for i in words:
        if(len(i)>=3):
            EncodeWordA = randomThreeString + i[1:] + i[0] + randomThreeString2
            nwords.append(EncodeWordA)
        else:
            nwords.append(i[::-1])
    print(" ".join(nwords))




elif(task.lower() == 'decode'):
    nwords = []
    for i in words:
        if(len(i)>=3):
            DecodeA = i[3:-3]
            DecodeA = DecodeA[-1] + DecodeA[:-1]
            nwords.append(DecodeA)
        else:
            nwords.append(i[::-1])
    print(" ".join(nwords))


else:
    raise ValueError("Invalid String | Input either 'encode' or 'decode' ")
