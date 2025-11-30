import time
def error():
    print("Enter the values again.")

def enter():
    try:
        global a
        a = int(input("Enter the first value: "))
        global b
        b = int(input("Enter the second value: "))
        global c
        c = int(input("Enter the third value: "))
    except:
         error()
         return enter()

def check_roots():
    if b**2-4*a*c > 0 :
        print("The equation has two differnt roots.")
    elif b**2-4*a*c == 0 :
        print("The equation has two same roots.")
    else:
        print("The equation has not a root.")

def find_root():
    if diskrimant>=0:
        d = (-1*b+diskrimant**1/2)/2*a
        e = (-1*b-diskrimant**1/2)/2*a
        print(f"The first root is {d} and second root is {e}.")
    else:
         print("The process is ended.")

enter()
print(f"{a}x²+{b}x+{c} is your equation that you have created.")
check_roots()
diskrimant = b**2-4*a*c
find_root()
time.sleep(20)














