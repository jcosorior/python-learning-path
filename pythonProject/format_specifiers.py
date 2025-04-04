# format specifiers =  {:flags} format a value based on what
#                               flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center aling
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = coma separator


price1 = 3000.14159 
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 1 is ${price2:+,.2f}")
print(f"Price 1 is ${price3:+,.2f}")