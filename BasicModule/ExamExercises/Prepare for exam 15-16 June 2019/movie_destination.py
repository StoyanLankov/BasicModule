# Read input
budget = float(input())
destination = input().strip()
season = input().strip()
days = int(input())

# Define destination prices
destinations_prices = {
    "Dubai": {"Winter": 45000, "Summer": 40000},
    "Sofia": {"Winter": 17000, "Summer": 12500},
    "London": {"Winter": 24000, "Summer": 20250},
}

# Calculate daily cost based on destination and season
daily_cost = destinations_prices[destination][season]

# Apply tax reductions/increases
if destination == "Dubai":
    daily_cost *= 0.7  # 30% discount for Dubai destination
elif destination == "Sofia":
    daily_cost *= 1.25  # 25% increase for Sofia destination

# Calculate total cost
total_cost = daily_cost * days

# Check if the budget is enough and print the result
if total_cost <= budget:
    remaining_budget = budget - total_cost
    print("The budget for the movie is enough! We have " + format(remaining_budget, ".2f") + " leva left!")
else:
    needed_amount = total_cost - budget
    print("The director needs " + format(needed_amount, ".2f") + " leva more!")
