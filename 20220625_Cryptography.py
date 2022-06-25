#################################################################################
# Cryptography session.										  Date: 25/06/2022	#
# Credits to the algorithms for Ministery of Education and Technology - Israel.	#
# In this file there are two example questions for AZBY and ALBM ciphers.		#
# Written by Gal Argov Sofer for 9th Grade (KITA TET) exam in Handasaim School. #
#################################################################################

# Ex1
def azby(str):
    abc = "abcdefghijklmnopqrstuvwxyz" # A to Z
    msg = ""
    str = str.lower()
    
    for letter in str:
        if letter == ' ':
            msg += letter
        else:
            p = abc.index(letter)
            msg += abc[-1 * (p + 1)]
    return msg


def main():
    txt = "Handasaim"
    msg = azby(txt)
    print("Encrypted:", msg)
    
    msg1 = azby(msg)
    print("Decrypted:", msg1)


main()


# Ex2
def albm(p_text):
    atom = "abcdefghijklm" # A to M
    ntoz = "nopqrstuvwxyz" # n to Z
    c_text = ""
    for letter in p_text:
        if letter in atom:
            num_letter = atom.find(letter)
            c_letter = ntoz[num_letter]
        elif letter in ntoz:
            num_letter = ntoz.find(letter)
            c_letter = atom[num_letter]
        else:
            c_letter = letter
        c_text += c_letter
    return c_text


def main():
    txt = "Handasaim"
    msg = albm(txt)
    print("Encrypted:", msg)
    
    msg1 = albm(msg)
    print("Decrypted:", msg1)


main()


# EOF