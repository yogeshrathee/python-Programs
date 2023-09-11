from forex_python.converter import CurrencyRates


def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()

    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = round(amount * exchange_rate, 2)
        return converted_amount
    except:
        return None


if __name__ == "__main__":
    print("Welcome to Currency Converter")
    print("Supported currencies: USD, EUR, GBP, JPY, INR, and more.")

    amount = float(input("Enter the amount: "))
    from_currency = input("From Currency (e.g., USD): ").upper()
    to_currency = input("To Currency (e.g., EUR): ").upper()

    result = convert_currency(amount, from_currency, to_currency)

    if result is not None:
        print(f"{amount} {from_currency} is equal to {result} {to_currency}")
    else:
        print("Currency conversion failed. Please check your inputs.")
