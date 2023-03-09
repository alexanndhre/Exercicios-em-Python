def split_and_join(line):
    line_list = line.split(" ")
    line_tracada = "-".join(line_list)
    return line_tracada

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)