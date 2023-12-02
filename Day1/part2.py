'''
Part 2 of Day 1, Trebuchet?!
https://adventofcode.com/2023/day/1
'''

NUMBERS = {'zero':"0",
           'one':"1",
           'two':"2",
           'three':"3",
           'four':"4",
           'five':"5",
           'six':"6",
           'seven':"7",
           'eight':"8",
           'nine':"9"}

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
        l_num = get_written_number(line, i)
        while not line[i].isdigit() and l_num is None:
            i += 1
            l_num = get_written_number(line, i)
        r_num = get_written_number(line, j)
        while not line[j].isdigit() and r_num is None:
            j -= 1
            r_num = get_written_number(line, j)
        l_num = line[i] if l_num is None else l_num
        r_num = line[j] if r_num is None else r_num
        values.append(int(l_num + r_num))
    return values

def get_written_number(line, i):
    '''
    Tries to get written number starting at index i.
    If no number found, returns None.
    '''
    for k, v in NUMBERS.items():
        if line[i:i+len(k)] == k:
            return v
    return None

def main():
    '''Process the calibration document received.'''
    document = get_calibration_document()
    calibration_values = get_calibration_values(document)
    print(sum(calibration_values))

if __name__ == "__main__":
    main()