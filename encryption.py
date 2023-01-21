word = input("Enter your word:\t")
task = input("What do you want to do? Encode or Decode?\t")
wordLength = len(word)
randomThreeString = "kJo"
randomThreeString2 = "fLw"

if(task.lower() == 'encode'):
    if(wordLength>=3):
        EncodeWordA = randomThreeString + word[1:wordLength] + word[0] + randomThreeString2
        print(f"The encoded string for {word} is {EncodeWordA}")
    else:
        EncodeWordB = word[1] + word[0]
        print(f"The encoded string for {word} is {EncodeWordB}")
elif(task.lower() == 'decode'):
    if(wordLength>=3):
        DecodeA = word[wordLength-4:wordLength-3] + word[3:wordLength - 4]
        print(f"The decoded string for {word} is {DecodeA}")
    else:
        DecodeB = word[1] + word[0]
        print(f"The decoded string for {word} is {DecodeB}")
else:
    raise ValueError("Invalid String | Input either 'encode' or 'decode' ")
