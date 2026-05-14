# *********clear function**************#
def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)


# *********clear function**************#
from logo import bid_logo  # import logo

bids = {}  # make an empty list of bids
bidding_finished = False  # making a while loop condition


def find_highest_bidder(bidding_record):  # Make a bidding function :
    highest_bid = 0  # set highest bid
    winner = ""  # make a string name winner
    for bidder in bidding_record:  # FOR LOOP :
        bid_amount = bidding_record[bidder]  # derive bidders from bidding record {"Angela": 123, "James": 321}
        if bid_amount > highest_bid:  # if amount > the highest bid
            highest_bid = bid_amount  # highest bid = bid amount
            winner = bidder  # so this bidder is a winner
    print(bid_logo)  # Print logo
    print(f"The winner is {winner} with a bid of ${highest_bid}")  # Print winner


while not bidding_finished:  # While loop not false
    print(bid_logo)  # print logo
    name = input("What is your name?: ")  # input name
    price = int(input("What is your bid?: $"))  # input bid
    bids[name] = price  # insert this info in bids list
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()  # stop bid or not?
    if should_continue == "no":  # If no
        bidding_finished = True  # false turns into true
        clear()  # calling clear function
        find_highest_bidder(bids)  # calling bidding function by using bids list
    elif should_continue == "yes":  # else
        clear()  # calling clear function
