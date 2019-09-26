print("This program convert binary numbers to decimal.")

def main():
    while True:
        try:
            num = input('Enter up to 8 binary digits: ')
            if len(num) > 8:
                print("Please, enter up to 8 binary digits")
            
            else:    
                bin_num = int(num, 2)
                print("In Dec: ",bin_num)
                break
        
        except ValueError:
            print("\nWrong digit!\n")
        
            
               


if __name__ == "__main__":
    main()