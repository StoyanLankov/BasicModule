def calculate_ticket_price(movie, package, tickets):
    ticket_prices = {
        "John Wick": {"Drink": 12, "Popcorn": 15, "Menu": 19},
        "Star Wars": {"Drink": 18, "Popcorn": 25, "Menu": 30},
        "Jumanji": {"Drink": 9, "Popcorn": 11, "Menu": 14},
    }

    ticket_price = ticket_prices[movie][package]

    if movie == "Star Wars" and tickets >= 4:
        ticket_price *= 0.7  # 30% discount for 4 or more tickets

    if movie == "Jumanji" and tickets == 2:
        ticket_price *= 0.85  # 15% discount for exactly 2 tickets

    total_price = ticket_price * tickets
    return total_price


def main():
    movie = input().strip()
    package = input().strip()
    tickets = int(input())

    final_price = calculate_ticket_price(movie, package, tickets)
    print(f"Your bill is {final_price:.2f} leva.")


if __name__ == "__main__":
    main()
