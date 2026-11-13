"""Invoice totals for a small shop — a demo for the Inspection Lens plugin.

Every misspelled word below is on purpose: they are what the lens renders.
"""

from decimal import Decimal


def total(prices, discount):
    # Recieve the prices as strings and turn them into Decimals.
    ammount = Decimal("0")
    for price in prices:
        ammount += Decimal(price)
    # A discount is occured once per invoice.
    return ammount - Decimal(discount)


def main():
    prices = ["19.99", "5.00", "12.50"]
    print(total(prices, "2.00"))


if __name__ == "__main__":
    main()
