# Exercise 5: menu-driven program using the circle module
import circle

def main():
    while True:
        print('a. Calculate the area of a circle')
        print('b. Calculate the circumference of a circle')
        print('c. End the program')
        choice = input('Choose a, b, or c: ').strip().lower()
        if choice == 'c':
            print('Goodbye!')
            break
        elif choice == 'a' or choice == 'b':
            radius = float(input('Enter the radius: '))
            if radius < 0:
                print('Radius cannot be negative.')
                continue
            if choice == 'a':
                print(f'Area:{circle.area(radius):.2f}')
            else:
                print(f'Circumference:{circle.circumference(radius):.2f}')
        else:
            print('Invalid choice. Try again.')
main()
