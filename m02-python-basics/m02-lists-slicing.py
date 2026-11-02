# Lists Slicing
# Andrew Jochl
# June, 27 2026

# ===== CODE BELOW HERE =====
amazon_cart = ["notebooks", "sunglasses", "toys", "books", "tools"]

amazon_cart[0] = "laptop"
new_cart = amazon_cart  # This is what is in memory
new_cart[0] = "gum"
print(new_cart)
print(amazon_cart)

print("\n")

amazon_cart[0] = "laptop"
new_cart = amazon_cart[:]  # Copy the list
new_cart[0] = "gum"
print(new_cart)
print(amazon_cart)

# ===== CODE ABOVE HERE =====

# NOTES
#
