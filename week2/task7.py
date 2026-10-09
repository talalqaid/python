NUM_SHARES = 1000
PURCHASE_PRICE = 32.87
SELLING_PRICE = 33.92
COMMISSION_RATE = 0.02

amount_paid = NUM_SHARES * PURCHASE_PRICE
purchase_commission = amount_paid * COMMISSION_RATE

amount_sold = NUM_SHARES * SELLING_PRICE
selling_commission = amount_sold * COMMISSION_RATE

total_paid = amount_paid + purchase_commission
total_received = amount_sold - selling_commission

profit_loss = total_received - total_paid

print(f"Amount paid for stock: £{amount_paid:.2f}")
print(f"Purchase commission: £{purchase_commission:.2f}")
print(f"Amount stock sold for: £{amount_sold:.2f}")
print(f"Selling commission: £{selling_commission:.2f}")
print(f"Money left / Profit or Loss: £{profit_loss:.2f}")

if profit_loss > 0:
    print("Joe made a profit.")
elif profit_loss < 0:
    print("Joe made a loss.")
else:
    print("Joe broke even.")