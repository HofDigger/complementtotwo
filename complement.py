def decimal_to_binar(decimal_number,memory_size):
    binary_number = bin(decimal_number)[2:]
    binary_number = binary_number.zfill(memory_size)
    return binary_number
def complement_to_two(binary_number):
    complemented = ''
    for bit in reversed(binary_number):
        if bit == '0':
            complemented = '1' + complemented
        elif bit == '1':
            complemented = '0' + complemented
        else:
            complemented = bit + complemented
    complemented = bin(int(complemented, 2) + 1)
    return complemented[2:]
decimal_number = int(input("enter your decimal number: "))
memory_size = int(input("enter your memory size: "))
binary = decimal_to_binar(decimal_number,memory_size)
print(complement_to_two(binary))