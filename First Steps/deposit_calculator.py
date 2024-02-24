deposit_sum = float(input())
deposit_period_months = int(input())
annual_interest = float(input())

sum_interest = deposit_sum * (annual_interest / 100)
interest_for_month = sum_interest / 12
total_sum = deposit_sum + deposit_period_months * interest_for_month

print(total_sum)