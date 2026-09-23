from linkedlist import linkedlist

import insertion
import traversal
import deletion

print("----------------------------------- \n1) Create a linked list \n2) Insert at beginning \n3) Insert at end \n4) Insert at a specific index \n5) Delete by value \n6) Delete first node \n7) Delete last node \n8) Count number of nodes \n9) Display \n10) Exit")
choice = int(input("Enter your choice: "))

if choice == 1:
    l1 = linkedlist()
    l1.display

elif choice == 2:
    data = int(input("Enter value to enter: "))
    l1.insertAtBeginning(data)
    l1.display()

elif choice == 3:
    data = int(input("Enter value to enter: "))
    l1.insertAtEnd(data)
    l1.display()

elif choice == 4:
    data = int(input("Enter value to enter: "))
    value = int(input("Enter index to enter: "))
    l1.insertAtIndex(value, data)
    l1.display()

elif choice == 5:
    value = int(input("Enter index to enter: "))
    l1.deleteFromIndex(value)
    l1.display()

elif choice == 6:
    l1.deleteFromBeginning()
    l1.display()