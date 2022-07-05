figure = input("what figure to draw? ")

if figure == "line":
  print("-----")

elif figure == "square":
    print(" -----"'\n',"|   |"'\n',"|   |"'\n',"-----")

elif figure == "square full":
    for i in range(4):
        print('*' * 9)

elif  figure == "parallel vertical lines":
    print(" |   |"'\n',"|   |")

else:
  print("CAN'T DRAW SUCH FIGURE!")  
