# The list to store all your expenses.
# Each item will be a dictionary: {'desc': 'Groceries', 'amount': 45.50}
expenses = []

# --- Start the main input process ---
print("--- Simple Expense Tracker ---")
print("Enter expenses one by one. Type 'done' to finish.\n")

while True:
    # 1. Get the description
    description = input("Enter expense description (e.g., Dinner, Travel, etc.): ").strip()

    # Check if the user wants to quit
    if description.lower() == 'done':
        break
    
    # Simple check for empty description
    if not description:
        print(">> Description cannot be empty. Try again.\n")
        continue

    # 2. Get the amount, with error handling
    while True:
        amount_input = input("Enter amount spent: ₹").strip()
        
        # Check if the user wants to quit here too
        if amount_input.lower() == 'done':
            # This break exits the inner loop, then the outer loop break handles the exit
            break 
            
        try:
            # Convert text input to a number
            amount = float(amount_input)
            if amount <= 0:
                print(">> Amount must be positive. Please re-enter the amount.")
                continue
            break
        except ValueError:
            print(">> Invalid input. Please enter a valid number (e.g., 50, 75, etc).")

    # If the user typed 'done' in the amount prompt, we exit the main loop
    if amount_input.lower() == 'done':
        break

    # 3. Store the expense
    new_expense = {
        'desc': description,
        'amount': amount
    }
    expenses.append(new_expense)
    print(f"✅ Added: {description} (₹{amount:.2f})\n")


# --- Calculate and display results ---

if not expenses:
    print("\nNo expenses entered. Tracker closed.")
else:
    # Calculate total
    total_expense = 0
    for item in expenses:
        total_expense += item['amount']

    print("\n" + "="*31)
    print("     FINAL EXPENSE SUMMARY")
    print("="*31)
    
    # List all recorded expenses
    for i, item in enumerate(expenses):
        print(f"{i+1}. {item['desc']} | ₹{item['amount']:.2f}")

    print("-" * 31)
    print(f"TOTAL SPENT: ₹{total_expense:,.2f}")
    print("="*31)

    '''Error handling to keep in mind:
    1. description cannot be empty
    2. if 'done' is entered anywhere(both description and amount), it should break 
    3. amount should be converted into float and >0
    4. if any non-number is entered, it should have exception showing "invalid input"
    5. if 'done' is entered without entering any expense, it should not print total'''