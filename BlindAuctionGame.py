import art
print("welcome to blind auction project".upper())
print(art.logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
continue_bidding =True
while continue_bidding:
    name = input("enter your name = ".upper())
    price = int(input("enter your bid = $".upper()))

    bids[name]= price

    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n".capitalize())

    if should_continue == "no" or should_continue == "No" or should_continue == "NO" or should_continue == "nO":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes" or should_continue == "YES" or should_continue == "Yes":
        print("\n"*50)
    else:
        print("INVALID ENTRY!!!")