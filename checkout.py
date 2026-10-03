def checkout_total(prices, shipping=0):
    """Return prices plus shipping; tax and discounts are excluded."""
    subtotal = sum(prices)
    return subtotal + shipping


if __name__ == "__main__":
    print(checkout_total([12.50, 7.50], 5.00))