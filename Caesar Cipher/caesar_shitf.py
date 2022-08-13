alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
  words = text.split(" ")
  enc_text = ""
  for i in words:
    enc_word =""
    for l in i:
      if l in alphabet:
        enc_word += alphabet[(alphabet.index(l)+shift+1)%26-1]
      else:
        enc_word += l
    enc_text += enc_word +" "
  print(enc_text)
  
def decrypt(text,shift):
  words = text.split(" ")
  or_text = ""
  for i in words:
    or_word =""
    for l in i:
      if l in alphabet:
        or_word += alphabet[(alphabet.index(l)-shift)] #den einai aparaitito to modulo
      else:
        or_word += l
    or_text += or_word +" "
  print(or_text)


game_over = False
while game_over == False:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == "encrypt":
    encrypt(text,shift)
  else:
    decrypt(text,shift)
  answer = input("Do you want again? \n").lower()
  if answer != "yes":
    game_over = True