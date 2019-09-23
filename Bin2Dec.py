print("This program convert binary numbers to decimal.")

num = input("Enter up to 8 binary digits 0 or 1: ")

def converter():
    bin_num = int(num, 2)
    print(bin_num)
    
    
    
def wrong_dig():
    print("Wrong digits")

def main():
    if len(num) != 8:
        wrong_dig()
        
    else:
        for i in num:
            if i == '0' or i == '1':
                continue
            else:
                wrong_dig()
                exit()
        
        converter()        
            
            
               


if __name__ == "__main__":
    main()