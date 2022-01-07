# Script by Antonio Sànchez.
# If you liked the script pls give it an star

# Github: https://github.com/felxansl
# Stack OverFlow: https://es.stackoverflow.com/users/264900/antonio-s%c3%a1nchez
# Twitter: https://twitter.com/felxansl

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
    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
    ████╗ ████║██╔════╝████╗  ██║██║   ██║
    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝                               
        """+ color.END)
print(" ")

pick = 0
while True:
    print(" ")
    elec = str(input(color.PURPLE + " So.. tell me, ¿you will use decimals? (type yes or no): "+ color.END) )
    print(" ")
    if elec == 'yes':
        import __init__
    elif elec == 'no':
        import __xinit__
    else:
        print(" ")
        print(color.RED + "     ERROR:"+ color.END + color.YELLOW +" you typed an invalid argument type yes or no."+ color.END)
        continue
