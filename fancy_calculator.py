def fancy_calculator():
    print("🧠 Welcome to the Emoji Calculator 3000! 🧠\n")

    # Step 1: Get user inputs
    try:
        num1 = float(input("🔢 Enter the first number: "))
        num2 = float(input("🔢 Enter the second number: "))
    except ValueError:
        print("🚫 That's not a number! Try again next time.")
        return

    # Step 2: Choose operation
    print("\n🧮 Choose an operation:")
    print(" ➕ for Addition")
    print(" ➖ for Subtraction")
    print(" ✖️ for Multiplication")
    print(" ➗ for Division")

    op = input("👉 Your choice (+, -, *, /): ").strip()

    # Step 3: Define operations
    operations = {
        '+': ('+', lambda x, y: x + y),
        '-': ('-', lambda x, y: x - y),
        '*': ('×', lambda x, y: x * y),
        '/': ('÷', lambda x, y: x / y if y != 0 else None)
    }

    # Step 4: Perform operation
    if op in operations:
        symbol, func = operations[op]
        if op == '/' and num2 == 0:
            print("😱 Division by zero?! Even my circuits can't handle that.")
        else:
            result = func(num1, num2)
            print(f"\n✅ Result: {num1} {symbol} {num2} = {result}")
    else:
        print("❓ Unknown operation. Please use one of: +, -, *, /")

    print("\n🎉 Thanks for using Emoji Calculator 3000!")

# Run the calculator
fancy_calculator()
