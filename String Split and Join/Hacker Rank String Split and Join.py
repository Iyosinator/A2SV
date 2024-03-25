
def split_and_join(line):
    split_line = line.split(" ")
    joined_line = "-".join(split_line)
    return joined_line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)