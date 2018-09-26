# read interger numbers from files

def readNumbers(filename):
    with open(filename, 'r') as fin:
        line = fin.read()
    numbers = [int(n) for n in line.split(',')]
    return numbers

if __name__ == '__main__':
    # Test readNumbers method
    filename = '../test/A1.txt'
    numbers = readNumbers(filename)
    print(numbers)