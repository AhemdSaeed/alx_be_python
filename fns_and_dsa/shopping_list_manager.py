def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    try:
        while True:
            display_menu()
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                item = input("Enter the item to add: ").strip()
                if item:
                    shopping_list.append(item)
                    print(f"'{item}' has been added to the list.")
                else:
                    print("No item entered. Nothing was added.")

            elif choice == '2':
                item = input("Enter the item to remove: ").strip()
                if not item:
                    print("No item entered.")
                    continue
                found_index = next((i for i, it in enumerate(shopping_list) if it.lower() == item.lower()), None)
                if found_index is not None:
                    removed = shopping_list.pop(found_index)
                    print(f"'{removed}' has been removed from the list.")
                else:
                    print(f"'{item}' was not found in the shopping list.")

            elif choice == '3':
                if shopping_list:
                    print("Your Shopping List:")
                    for idx, it in enumerate(shopping_list, start=1):
                        print(f"{idx}. {it}")
                else:
                    print("Your shopping list is empty.")

            elif choice == '4':
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nGoodbye!")

if __name__ == "__main__":
    main()
