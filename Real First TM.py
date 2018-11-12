service_charge = $2
ticket_price = $10
tickets_remaning = 500

while tickets_remaning >= 1:
	print("There are {} tickets remaning.".format(tickets_remaning))
	name = input("What is your name?")
	tickets_num = input("How many tickets would you like, {}".format(name))
	try:
	tickets_num = int(tickets_num)
    if tickets_num > tickets_remaning:
    	raise ValueError("There are only {} tickets remaning".format(tickets_remaning))
    except ValueError as err:
    	print("Uh oh we encountered a issue. Try again.".format(err))
    else:
    amount_due = tickets_num * ticket_price
    print("The total due is ${}".format(amount_due))
    proceed = input("Would you like to proceed with your purchase?")
    if proceed == "Yes" or "yes":
    	print("Sold")
    	print("Done! Thank you for your time.")