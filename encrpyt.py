from tkinter import messagebox, simpledialog, Tk

p=True
while(p):
    choice=int(input('enter choice'))
    if (choice==1):

        def is_even(number):
            return number % 2 == 0

        def get_even_letters(message):
            even_letters = []
            for counter in range(0, len(message)):
                if is_even(counter):
                    even_letters.append(message[counter])
            return even_letters

        def get_odd_letters(message):
            odd_letters = []
            for counter in range(0, len(message)):
                if not is_even(counter):
                    odd_letters.append(message[counter])
            return odd_letters

        def swap_letters(message):
            letter_list = []
            if not is_even(len(message)):
                message = message + 'x'
            even_letters = get_even_letters(message)
            odd_letters = get_odd_letters(message)
            for counter in range(0, int(len(message)/2)):
                letter_list.append(odd_letters[counter])
                letter_list.append(even_letters[counter])
            new_message = ''.join(letter_list)
            return new_message

        def get_task():
            task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
            return task

        def get_message():
            message = simpledialog.askstring('Message', 'Enter the secret message: ')
            return message

        root = Tk()
        while True:
            task = get_task()
            if task == 'encrypt':
                message = get_message()
                encrypted = swap_letters(message)
                messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
                
            elif task == 'decrypt':
                message = get_message()
                decrypted = swap_letters(message)
                messagebox.showinfo('Plaintext of the secret message is:', decrypted)
            else:
                break
        root.mainloop()
        
    elif(choice==2):
            # try block to handle exception
        try:
            # take path of image as a input
            path = input(r'Enter path of Image : ')
            
            # taking encryption key as input
            key = int(input('Enter Key for encryption of Image : '))
            
            # print path of image file and encryption key that
            # we are using
            print('The path of file : ', path)
            print('Key for encryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to
            # perform encryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writing purpose
            fin = open(path, 'wb')
            
            # writing encrypted data in image
            fin.write(image)
            fin.close()
            print('Encryption Done...')

            
        except Exception:
            print('Error caught : ', Exception.__name__)


    elif(choice==3):
            # try block to handle the exception
        try:
            # take path of image as a input
            path = input(r'Enter path of Image : ')
            
            # taking decryption key as input
            key = int(input('Enter Key for encryption of Image : '))
            
            # print path of image file and decryption key that we are using
            print('The path of file : ', path)
            print('Note : Encryption key and Decryption key must be same.')
            print('Key for Decryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to perform decryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writing purpose
            fin = open(path, 'wb')
            
            # writing decryption data in image
            fin.write(image)
            fin.close()
            print('Decryption Done...')


        except Exception:
            print('Error caught : ', Exception.__name__)


    choice1=int(input('enter'))
    if(choice1==1):
        p=True

    else:
        p=False