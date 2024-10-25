from art import logo

print(logo)
name_and_bid = {}
is_going = True

while is_going:
    name = input("What is your name?:  ")
    bid = input("What is your bid?: $")
    is_more = input("Are there any other bidders? Type 'yes' or 'no'.")

    name_and_bid[name] = int(bid)
    if is_more == "no":
        is_going = False
    print("\n" * 1000)


winner_bidder = ["name", 0]

current_bid = 0

for key in name_and_bid:

    if name_and_bid[key] > current_bid:
        winner_bidder[0] = key
        winner_bidder[1] = name_and_bid[key]

    current_bid = name_and_bid[key]

print(f"The winner is {winner_bidder[0]} with a bid of ${winner_bidder[1]}.")