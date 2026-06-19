from management import ExpenseManagement
em=ExpenseManagement()
while True:
    print("\n----- Expense Tracker -----")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Category Wise Total")
    print("4. Save Expenses")
    print("5. Exit")
    choice =int(input("Enter Choice: "))

    if choice==1:
        em.add()
    elif choice==2:
        em.show()
    elif choice==3:
        em.total()
    elif choice==4:
        em.save()
    elif choice==5:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")