bidders = {}
bidding_on = True


def highest_bidder(bidding_record):
    hightest_amount = 0
    winner = ""
    for b in bidding_record:
        bid_amount = bidding_record[b]
        if bid_amount > hightest_amount:
            hightest_amount = bid_amount
            winner = b

    print(f"the winner is {winner} with a bid of ${hightest_amount}")


while bidding_on == True:

    name = input("What is your name?: ")
    amount = int(input("how much do you bid?: "))
    bidding_cont = input("Are there more bidders?: T/F ")

    bidders[name] = amount

    if bidding_cont == "F":
        bidding_on = False
        highest_bidder(bidders)
