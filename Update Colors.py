colors = []

answer = input("Would you like to make a list of colors? (yes/no): ")
if answer == "yes":
    color1 = input("Please enter your first color: ")
    color2 = input("Please enter your second color: ")
    color3 = input("Please enter your third color: ")
    color4 = input("Please enter your fourth color: ")

    colors.append(color1)
    colors.append(color2)
    colors.append(color3)
    colors.append(color4)

    size = len(colors)
    count = 0

    while count < size:
        print("Your " + str(count + 1) + " color is: " + colors[count])
        count += 1

    answer = input("Would you like to run again? (y/n): ")
    while answer == "y":
        colors = []
        color1 = input("Please enter your first color: ")
        color2 = input("Please enter your second color: ")
        color3 = input("Please enter your third color: ")
        color4 = input("Please enter your fourth color: ")

        colors.append(color1)
        colors.append(color2)
        colors.append(color3)
        colors.append(color4)

        size = len(colors)
        count = 0

        while count < size:
            print("Your " + str(count + 1) + " color is: " + colors[count])
            count += 1

        answer = input("Would you like to run again? (y/n): ") 
else: 
    print("Thank you for using the color counter!") 