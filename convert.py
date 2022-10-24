def emoji(message):
    words=message.split(' ')
    emojis = {
        ":)":"😊😊😊",
        ":(" :"😒😒😒😒😒"
    }
    output=""
    for i in words:
        output+= emojis.get(i,i)+' '
    return output


message=input(">")
print(emoji(message))
   
