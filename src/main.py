MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                  'C':'-.-.', 'D':'-..', 'E':'.',
                  'F':'..-.', 'G':'--.', 'H':'....',
                  'I':'..', 'J':'.---', 'K':'-.-',
                  'L':'.-..', 'M':'--', 'N':'-.',
                  'O':'---', 'P':'.--.', 'Q':'--.-',
                  'R':'.-.', 'S':'...', 'T':'-',
                  'U':'..-', 'V':'...-', 'W':'.--',
                  'X':'-..-', 'Y':'-.--', 'Z':'--..',
                  '1':'.----', '2':'..---', '3':'...--',
                  '4':'....-', '5':'.....', '6':'-....',
                  '7':'--...', '8':'---..', '9':'----.',
                  '0':'-----', ', ':'--..--', '.':'.-.-.-',
                  '?':'..--..', '/':'-..-.', '-':'-....-',
                  '(':'-.--.', ')':'-.--.-'}
									

def encrypt(message):
  cipher = ''
  for letter in message:
    if letter != ' ':
      cipher += MORSE_CODE_DICT[letter] + ' '
    else:
      cipher += ' '
  return cipher


def pretty_encrypt(message):
    for item in list(encrypt(message)):
    a = (encrypt(item))
    for characters in a:
        b = list(a)
    for item in b: 
        if b[num] == '-':
        print("dash")
        elif b[num] == '.':
        print("dot")
        else:
        print("0")
        num += 1
    num = 0