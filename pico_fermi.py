original_number = '123'


while True:

    output = []
    guess_number = input('Enter Your gues: ')
    if len(original_number) != len(guess_number):
        print(f"Enter {len(original_number)} digit number")
        continue

    if len(original_number) != len(set(guess_number)):
        print("Duplicate Number")
        continue

    if (int(original_number) - int(guess_number)) == 0:
        print('Fermi '  * len(original_number))
        print("\nYou Win!!!")
        break


    for i in range (len(original_number)):
        for j in range(len(guess_number)):
            if original_number[i] == guess_number[j]:
                if i == j:
                    output.append('Fermi ')
                else:
                    output.append('Pico')

    output_string = ''
    for item in output:
        output_string = output_string + ' '+ item

    if len(output) == 0:
        print('Bagels')
    else:
         print(output_string)

# print(f"the number is {original_number}")
# a = 122
# print(len(set(original_number)))
