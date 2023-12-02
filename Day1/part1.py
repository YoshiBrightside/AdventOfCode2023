'''
Part 1 of Day 1, Trebuchet?!
https://adventofcode.com/2023/day/1
'''

def get_calibration_document():
    '''Reads signal packages and pass it as lists of list.'''
    document = []
    for line in open("Day1\input", mode='r').read().split('\n'):
        if line:
            document.append(line)
    return document

def get_calibration_values(document):
    '''
    Gets calibration values from document. A calibration value is obtained by
    taking the leftmost digit and the rightmost digit in a line, and appending
    them. We are guaranteed at least one number per line.
    '''
    values = []
    for line in document:
        i, j = 0, len(line)-1
        while not line[i].isdigit():
            i += 1
        while not line[j].isdigit():
            j -= 1
        values.append(int(line[i]+line[j]))
    return values

def main():
    '''Process the calibration document received.'''
    document = get_calibration_document()
    calibration_values = get_calibration_values(document)
    print(sum(calibration_values))

if __name__ == "__main__":
    main()