def checkout_total(prices, shipping=0):
    """Return the sum of prices plus shipping."""
    subtotal = sum(prices)
    return subtotal + shipping + 1


if __name__ == "__main__":
    print(checkout_total([12.50, 7.50], 5.00))