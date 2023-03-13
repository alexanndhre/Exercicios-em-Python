##Esse código verifica caracteres alphanuméricos, numéricos, com algarísmos, maiúsculos e minúsculos.##

if __name__ == '__main__':
    s = input()
    
    def alnum(s):
        for caractere in s:
            if caractere.isalnum():
                return True
        return False
        
    def alph(s):
        for caractere in s:
            if caractere.isalpha():
                return True
        return False
    
    def digit(s):
        for caractere in s:
            if caractere.isdigit():
                return True
        return False
    
    def lower(s):
        for caractere in s:
            if caractere.islower():
                return True
        return False
    
    def upper(s):
        for caractere in s:
            if caractere.isupper():
                return True
        return False
    
    print(alnum(s))
    print(alph(s))
    print(digit(s))    
    print(lower(s))
    print(upper(s))