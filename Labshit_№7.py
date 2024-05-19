from time import *


def encode_LZ77(FileIn, FileOut):
    #   Note of time
    start_time = time()

    #   Connecting files for extraction and saving
    input_file = open(FileIn, 'r', encoding='utf-8').read()
    encoded_file = open(FileOut, 'w', encoding='utf-8')

    #   Value of the search and check window
    max_search = 100
    max_look_ahead = 10

    #   Initialize the output, the current position
    output = []
    current = 0

    #   Loop until the end of the text
    while current < len(input_file):
        #   Set the search and look ahead windows
        search = input_file[max(0, current - max_search) : current]
        look_ahead = input_file[current : current + max_look_ahead]

        #   Initialize the best match
        best_match = (0, 0, look_ahead[0])

        #   Loop through the search window
        for i in range(len(search) - 1, -1, -1):
            #   Compare each character with the look ahead window
            match = 0
            while match < len(look_ahead) and search[i + match] == look_ahead[match]:
                match += 1

            #   Update the best match if necessary
            if match > best_match[1]:
                best_match = (len(search) - i, match, look_ahead[match] if match < len(look_ahead) else '')

            #   Break the loop if the match is maximal
            if match == len(look_ahead):
                break

        #   Store the best match in the output
        output.append(best_match)

        #   Update the current position
        current += best_match[1] + 1
    
    #   Writing encodings and characters to file
    for code in output:
        encoded_file.write(str(code)+'\n')
    
    encoded_file.close()

    #   Time ca;culation
    end_time = time()
    elapsed_time = end_time - start_time

    #   Printing the output
    for code in output:
        print(code)
    print(f'Original file size: {len(input_file)}\nEncoded file size: {len(output)}\nTime spent: {round(elapsed_time, 9)} sec')

def decode_LZ77(FileIn, FileOut):

    coded_file = open(FileIn, 'r', encoding='utf-8').readlines()
    decoded_file = open(FileOut, 'w', encoding='utf-8')

    encodedNumbers, encodedSizes, encodedLetters = [], [], []

    for i in range(len(coded_file)):
        encodedNumbers.append(eval(coded_file[i].replace('\n', ''))[0])
        encodedSizes.append(eval(coded_file[i].replace('\n', ''))[1])
        encodedLetters.append(eval(coded_file[i].replace('\n', ''))[2])

    i = 0
    decodedString = []
    while i < len(encodedNumbers):
        if (encodedNumbers[i] == 0):
            decodedString.append(encodedLetters[i])
        else:
            currentSize = len(decodedString)
            for j in range(0, encodedSizes[i]):
                decodedString.append(decodedString[currentSize-encodedNumbers[i]+j])
            decodedString.append(encodedLetters[i])
        i = i+1

    for letter in decodedString:
        decoded_file.write('%s' % letter)

    decoded_file.close()

#   ----------------------------------------------------------------------------

def encode_LZ78(FileIn, FileOut):
    #   Note of time
    start_time = time()

    #   Connecting files for extraction and saving
    input_file = open(FileIn, 'r', encoding='utf-8')
    encoded_file = open(FileOut, 'w', encoding='utf-8')
    
    #   Initialize the output
    output = []

    text_from_file = input_file.read()
    dict_of_codes = {text_from_file[0]: '1'}
    encoded_file.write('0' + text_from_file[0])
    output.append((0, text_from_file[0]))
    text_from_file = text_from_file[1:]
    
    combination = ''
    code = 2
    
    #   Loop until the end of the text
    for char in text_from_file:
        combination += char
        if combination not in dict_of_codes:
            dict_of_codes[combination] = str(code)
            #   Store the combination in endcoding file
            if len(combination) == 1:
                encoded_file.write('0' + combination)
                output.append((0, combination))
            else:
                encoded_file.write(dict_of_codes[combination[0:-1]] + combination[-1])
                output.append((dict_of_codes[combination[0:-1]], combination[-1]))
            code += 1
            combination = ''
    
    input_file.close()
    encoded_file.close()

    #   Time ca;culation
    end_time = time()
    elapsed_time = end_time - start_time
    
    #   Printing the output
    for codes in output:
        print(codes)
    print(f'Original file size: {len(text_from_file)}\nEncoded file size: {len(output)}\nTime spent: {round(elapsed_time, 9)} sec')

def decode_LZ78(FileIn, FileOut):
    coded_file = open(FileIn, 'r', encoding='utf-8')
    decoded_file = open(FileOut, 'w', encoding='utf-8')
    text_from_file = coded_file.read()
    dict_of_codes = {'0': '', '1': text_from_file[1]}
    decoded_file.write(dict_of_codes['1'])
    text_from_file = text_from_file[2:]
    combination = ''
    code = 2
    for char in text_from_file:
        if char in '1234567890':
            combination += char
        else:
            dict_of_codes[str(code)] = dict_of_codes[combination] + char
            decoded_file.write(dict_of_codes[combination] + char)
            combination = ''
            code += 1
    coded_file.close()
    decoded_file.close()

#   ----------------------------------------------------------------------------

def encode_LZW(FileIn, FileOut):
    #   Note of time
    start_time = time()

    #   Connecting files for extraction and saving
    input_file = open(FileIn, 'r', encoding='utf-8').read()
    encoded_file = open(FileOut, 'w', encoding='utf-8')

    #   Build the dictionary.
    dict_size = 2048
    dictionary = dict((chr(i), i) for i in range(dict_size))

    #   Initialize the output
    output = []

    w = ""
    result = []

    #   Loop until the end of the text
    for c in input_file:
        wc = w + c
        #   Store the combination in endcoding file
        if wc in dictionary:
            w = wc
            if dictionary[w] not in output:
                output.append((dictionary[w], w))
        else:
            #   print dictionary[w], '---', type(dictionary[w])
            result.append(dictionary[w])
            #   Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
            if dictionary[w] not in output:
                output.append((dictionary[w], w))

    #   Output the code for w.
    if w:
        result.append(dictionary[w])

    #   Writing encodings and characters to file
    for code in result:
        encoded_file.write('%s ' % str(code))

    encoded_file.close()

    #   Time ca;culation
    end_time = time()
    elapsed_time = end_time - start_time

    #   Printing the output
    for codes in output:
        print(codes)
    print(f'Original file size: {len(input_file)}\nEncoded file size: {len(output)}\nTime spent: {round(elapsed_time, 9)} sec')


def decode_LZW(FileIn, FileOut):
    """Decompress a list of output ks to a string."""

    coded_file = [int(i) for i in open(FileIn, 'r', encoding='utf-8').read().split()]
    decoded_file = open(FileOut, 'w', encoding=('utf-8'))

    # Build the dictionary.
    dict_size = 2048
    dictionary = dict((i, chr(i)) for i in range(dict_size))


    w = result = chr(coded_file.pop(0))
    decoded_file.write(result)
    for k in coded_file:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad encoding k: %s' % k)
        decoded_file.write(entry)

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    
    decoded_file.close()

#   ----------------------------------------------------------------------------

def main():
  choice = int(input("Select how the, message is encoded in the file\n1 - LZ77\n2 - LZ78\n3 - LZW\nSelected: "))
  if choice == 1:
    encode_LZ77('in.txt', 'encoded.txt')
    decode_LZ77('encoded.txt', 'decoded.txt')
  elif choice == 2:
    encode_LZ78('in.txt', 'encoded.txt')
    decode_LZ78('encoded.txt', 'decoded.txt')
  elif choice == 3:
    encode_LZW('in.txt', 'encoded.txt')
    decode_LZW('encoded.txt', 'decoded.txt')
  else:
    print('You entered invalid input')
    

if __name__ == "__main__":
    main()