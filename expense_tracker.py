expenses = {}



while True:
    decision = input("Would you like to add, update, delete, or view your expenses? Or exit?")
    if decision.lower() == "add":
        new_expense = input("Pleae enter the name of the expense you would like to add: ")
        new_expense_amt = input("Please enter the cost of that expense: ")
        expenses[new_expense] = new_expense_amt
   
    elif decision.lower() == "update":
        updated_expense = input("Which expense would you like to update? ")
        updated_amt = input(f"Please enter the updated amount for {updated_expense}")
        expenses[updated_expense] = updated_amt
    
    elif decision.lower() == "delete":
        deleted_expense = input("Which expense would you like to delete? ")
        del expenses[deleted_expense]
    
    elif decision.lower() == "view":
        expense_titles = expenses.keys()
        for key in expenses.keys():
            print("For expense:", key, "your cost was:". expenses[key])
    
    elif decision == "exit":
        break

    else:
        print("Looks like you typed an unavailable option or something wrong... please try again. ")
        


