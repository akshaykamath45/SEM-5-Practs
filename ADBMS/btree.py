from BTrees.IIBTree import IIBTree


def print_menu():
    print("\n**** B Tree ****")
    print("1. Insert")
    print("2. Search")
    print("3. Show Tree")
    print("4. Delete")
    print("5. Exit")
    return input("Enter your choice: ")

btree = IIBTree(order=2)

while True:
    menu_choice = print_menu()
    
    if menu_choice  == '1':
        num = int(input("To enter: "))
        btree.insert(num, num)
        print(f"Element {num} entered into tree")
    if menu_choice == '2':
        num = int(input("To search: "))
        if num in btree:
            print("Element found!")
        else:
            print(f"{num} not found")
    if menu_choice == '3':
        for el in btree.items():
            print(el, end= " ")
    if menu_choice == '4':
        num = int(input("To delete: "))
        if num in btree:
            btree.__delitem__(num)
        print(f"Deleted {num}")
    if menu_choice == '5':
        exit()