"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluates to number of key-value entries
print(len(ice_cream))

# add key-value entries using subscription notation
ice_cream["mint"] = 10

# access values by their key using subscription notiation
mint_orders: int = ice_cream["mint"]
print(mint_orders)

# reassign values by their using assignment
ice_cream["mint"] = ice_cream["mint"] + 1
ice_cream["mint"] += 1

# remove items by key using the pop method
ice_cream.pop("strawberry")

# test if a key is in the dictionary
print("strawberry" in ice_cream)
print("vanilla" in ice_cream)

# loop through items using for-in loops

# the variable (flavor) iterates over
# each key one by one in the dictionary

for flavor in ice_cream:
    print(f"{flavor}: {ice_cream[flavor]}")
