rands = input("How much was the meal? ")
amount = float(rands.replace("R", ""))
tip = amount * 0.10
print(f"Leave R {tip:.2f}")