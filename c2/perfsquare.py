start_range=int(input("Enter the lower limit (between 999 and 10000):"))
if(start_range>999 and start_range<10000):
    end_range = int(input("Enter the upper limit (between 999 and 10000):"))
    if (end_range > start_range and end_range < 10000):
        myList = []
        for i in range(start_range,end_range+1):
            if i % 2 == 0:
                square_root = int(i ** 0.5)
                if square_root * square_root == i:
                    myList.append(i)
        print("The list of four digit numbers in a given range with all their digits even and the number is a perfect square.:")
        print(myList)
    else:
        print("Invalid range!")
else:
    print("Invalid range!")
