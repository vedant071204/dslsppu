'''
Experiment No. 13 : Write a python program to maintain club members, sort on roll numbers in ascending order.
                    Write function “Ternary_Search” to search whether particular student is member of club or not.
                    Ternary search is modified binary search that divides array into 3 halves instead of two.
'''

def accept_roll():
    roll_no = []
    no_of_students = int(input("Enter the number of students: "))
    for i in range(no_of_students):
        roll_no.append(int(input("Enter Roll Number of Student {0}: ".format(i+1))))
    return roll_no

def print_roll(roll_no):
    for roll_number in roll_no:
        print(roll_number, sep="\n")

def insertion_sort(roll_no):
    for i in range(1, len(roll_no)):
        key = roll_no[i]
        j = i - 1
        while j >= 0 and key < roll_no[j]:
            roll_no[j + 1] = roll_no[j]
            j -= 1
        roll_no[j + 1] = key
    return roll_no

def NR_Ternary_Search(roll, roll_find):
    left = 0
    right = len(roll) - 1
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = left + 2 * (right - left) // 3
        if roll_find == roll[left]:
            return left
        elif roll_find == roll[right]:
            return right
        elif roll_find < roll[left] or roll_find > roll[right]:
            return -1
        elif roll_find <= roll[mid1]:
            right = mid1
        elif roll_find > roll[mid1] and roll_find <= roll[mid2]:
            left = mid1 + 1
            right = mid2
        else:
            left = mid2 + 1
    return -1

def R_Ternary_Search(roll, left, right, roll_find):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if roll[mid1] == roll_find:
            return mid1
        if roll[mid2] == roll_find:
            return mid2

        if roll_find < roll[mid1]:
            return R_Ternary_Search(roll, left, mid1 - 1, roll_find)
        elif roll_find > roll[mid2]:
            return R_Ternary_Search(roll, mid2 + 1, right, roll_find)
        else:
            return R_Ternary_Search(roll, mid1 + 1, mid2 - 1, roll_find)
    return -1

def main():
    unsorted_roll = []
    sorted_roll = []
    flag = 1

    while flag == 1:
        print("\n---------------------MENU---------------------")
        print("1. Accept Student Roll Numbers")
        print("2. Display the Roll Numbers of Students")
        print("3. Sort Roll Numbers from the list")
        print("4. Perform Non-Recursive Ternary Search")
        print("5. Perform Recursive Ternary Search")
        print("6. Exit\n")

        ch = int(input("Enter your choice (from 1 to 6): "))

        if ch == 1:
            unsorted_roll = accept_roll()

        elif ch == 2:
            print_roll(unsorted_roll)

        elif ch == 3:
            print("Elements after performing Insertion Sort:\n")
            sorted_roll = insertion_sort(unsorted_roll)
            print_roll(sorted_roll)

        elif ch == 4:
            find_roll = int(input("Enter the Roll Number to be searched: "))
            index = NR_Ternary_Search(sorted_roll, find_roll)
            if index != -1:
                print("The Roll Number", find_roll, "is found at position", index + 1)
            else:
                print("Roll Number", find_roll, "not found!!")

        elif ch == 5:
            find_roll = int(input("Enter the Roll Number to be searched: "))
            left = 0
            right = len(sorted_roll) - 1
            index = R_Ternary_Search(sorted_roll, left, right, find_roll)
            if index != -1:
                print("The Roll Number", find_roll, "is found at position", index + 1)
            else:
                print("Roll Number", find_roll, "not found!!")

        elif ch == 6:
            print("Thanks for using this program!!")
            flag = 0

        else:
            print("Wrong choice!!")
            flag = 0

if __name__ == "__main__":
    main()

