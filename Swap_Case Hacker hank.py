#"swap_case - Hackerhank"
# Essa função converte os caractéres que estão maiúsculos em minúsculos e vice-versa.

def swap_case(s):
    return ''.join(map(lambda c: c.upper() if c.islower() else c.lower(), s))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)