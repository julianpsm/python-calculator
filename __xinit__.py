# Script by Antonio Sànchez.
# If you liked the script pls give it an star

# Github: https://github.com/felxansl
# Stack OverFlow: https://es.stackoverflow.com/users/264900/antonio-s%c3%a1nchez
# Twitter: https://twitter.com/felxansl

# import of sys.exit()
import sys
# Text colors and stuff
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
#========================#

print(color.YELLOW + """ 
     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗     
    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    
    ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝    
    ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗    
    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║    
     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    
                                                                                       
    ██╗    ██╗██╗████████╗██╗  ██╗ ██████╗ ██╗   ██╗████████╗                              
    ██║    ██║██║╚══██╔══╝██║  ██║██╔═══██╗██║   ██║╚══██╔══╝                              
    ██║ █╗ ██║██║   ██║   ███████║██║   ██║██║   ██║   ██║                                 
    ██║███╗██║██║   ██║   ██╔══██║██║   ██║██║   ██║   ██║                                 
    ╚███╔███╔╝██║   ██║   ██║  ██║╚██████╔╝╚██████╔╝   ██║                                 
     ╚══╝╚══╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝                                 
                                                                                       
    ██████╗ ███████╗ ██████╗██╗███╗   ███╗ █████╗ ██╗     ███████╗                         
    ██╔══██╗██╔════╝██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝                         
    ██║  ██║█████╗  ██║     ██║██╔████╔██║███████║██║     ███████╗                         
    ██║  ██║██╔══╝  ██║     ██║██║╚██╔╝██║██╔══██║██║     ╚════██║                         
    ██████╔╝███████╗╚██████╗██║██║ ╚═╝ ██║██║  ██║███████╗███████║                         
    ╚═════╝ ╚══════╝ ╚═════╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝                                                                                                      
"""+ color.END)
print(" ")
pick = 0
while True:
    try:
        n1 = int(input(color.PURPLE + " Type your first number (without decimals): "+ color.END) )
        print(" ")
        n2 = int(input(color.PURPLE + " Type your second number (without decimals): "+ color.END) )
    except:
        print(" ")
        print(color.RED + "     ERROR:"+ color.END + color.YELLOW + " you typed an invalid argument pls use only int numbers."+ color.END)
        print(" ")
    else:
        break
def cnf():
    option = 0
    while True:
        global n1, n2     
        print(color.YELLOW + """ 
        Chose an option for your numbers:

        1( Add.
        2( Multiply.
        3( Substract them.
        4( Divide.
        5( Change my numbers.
        6( Change my numbers to (with decimals).
        7( Exit.
        """ + color.END)
        opt = 0
        while True:
            try:
                option = int(input(color.PURPLE + " Pick a number: " + color.END) )
            except:
                print(" ")
                print(color.RED + "     ERROR:"+ color.END + color.YELLOW + " you typed an invalid argument pls use only int numbers."+ color.END)
                print(" ")
            else:
                break
        if option == 1:
            print(" ")
            print(color.GREEN + " The total of", n1, "+", n2, "is:", n1+n2)
        elif option == 2:
            print(" ")
            print(color.GREEN + " The total of", n1, "x", n2, "is:", n1*n2)
        elif option == 3:
            print(" ")
            print(color.GREEN + " The total of", n1, "-", n2, "is:", n1-n2)
        elif option == 4:
            print(" ")
            print(color.GREEN + " The total of", n1, "/", n2, "is:", n1/n2)
        elif option == 5:
            while True:
                try:
                    n1 = float(input(color.PURPLE + " Type your first number (with decimals): "+ color.END) )
                    print(" ")
                    n2 = float(input(color.PURPLE + " Type your second number (with decimals): "+ color.END) )
                except:
                    print(" ")
                    print(color.RED + "     ERROR:"+ color.END + color.YELLOW + " you typed an invalid argument pls use only float numbers."+ color.END)
                    print(" ")
                else:
                    break
        elif option == 6:
            import __init__
        elif option == 7:
            print(color.YELLOW + """ 
    ██████╗ ██╗   ██╗███████╗██╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║
    ██████╔╝ ╚████╔╝ █████╗  ██║
    ██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝
    ██████╔╝   ██║   ███████╗██╗
    ╚═════╝    ╚═╝   ╚══════╝╚═╝ 
        """+ color.END)
            sys.exit()
        else:
            print(" ")
            print(color.RED + "     ERROR:" + color.END + color.YELLOW + " please introduce a list number:"+ color.END)
