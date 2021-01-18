from replit import clear
#HINT: You can call clear() to clear the output in the console. 
from art import logo 
print(logo)

# Code below has some issues will work on it : 
# def silent_auction(bidder_name,bid_value):
#   silent_bid={}
#   silent_bid["name"]=bidder_name
#   silent_bid["bid"]=bid_value 
#   print(silent_bid) 
#   other_bids=input("Are there any other bids? Type 'yes' or 'no.'\n") 
#   if other_bids=="yes":
#     clear()
#     silent_bid["name"]=input("Please input your name: ")
#     silent_bid["bid"]=input("Please enter your bid-value:$ " )
#   elif other_bids=="no":
  
   
#     # winner=""
#     highest_bid=0  
#     for bidder in silent_bid:
#       bid_amount=silent_bid[bidder]
#       if bid_amount>highest_bid:
#         highest_bid=bid_amount
#         # winner="name"
#         print(f"The highest bid is {highest_bid}")


# silent_auction(bidder_name,bid_value)



# Alternate-Method:

bids={}
bidding_finished=False
def find_highest_bidder(bidding_record):
  highest_bid=0
  winner=""
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The winning-bid is {highest_bid} and the winner is {winner}")






while not bidding_finished:
  
  bidder_name=input("Please input your name: ")
  bid_value=int(input("Please enter your bid-value:$ ") )

  bids[bidder_name]=bid_value 
  should_continue=input("Are there any other bids? Type 'yes' or 'no.'\n")
  if should_continue=='no':
    bidding_finished=True
    find_highest_bidder(bids)
  elif should_continue=='yes':
    clear()

  