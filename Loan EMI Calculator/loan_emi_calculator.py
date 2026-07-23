"""
=========================================================
                LOAN EMI CALCULATOR
---------------------------------------------------------
Author      : Shravan Dalavi
Language    : Python 3
Description : Calculate Loan EMI, Interest and
              Total Payment with Amortization Schedule.
=========================================================
"""

from math import pow


LINE = "=" * 60


def currency(value: float) -> str:
    """Return value formatted as currency."""
    return f"₹{value:,.2f}"


def calculate_emi(principal: float,
                  annual_rate: float,
                  tenure_months: int):
    """
    Calculate EMI, Total Payment and Interest.
    """

    monthly_rate = annual_rate / (12 * 100)

    if monthly_rate == 0:
        emi = principal / tenure_months
    else:
        emi = (
            principal
            * monthly_rate
            * pow(1 + monthly_rate, tenure_months)
        ) / (
            pow(1 + monthly_rate, tenure_months) - 1
        )

    total_payment = emi * tenure_months
    total_interest = total_payment - principal

    return emi, total_payment, total_interest


def amortization_schedule(principal,
                          annual_rate,
                          tenure_months,
                          emi):
    """
    Print loan repayment schedule.
    """

    monthly_rate = annual_rate / (12 * 100)

    balance = principal

    print("\n" + LINE)
    print("AMORTIZATION SCHEDULE")
    print(LINE)

    print(
        f"{'Month':<8}"
        f"{'Principal':>15}"
        f"{'Interest':>15}"
        f"{'Balance':>18}"
    )

    print("-" * 60)

    for month in range(1, tenure_months + 1):

        interest = balance * monthly_rate
        principal_paid = emi - interest

        if principal_paid > balance:
            principal_paid = balance

        balance -= principal_paid

        if balance < 0:
            balance = 0

        print(
            f"{month:<8}"
            f"{principal_paid:>15.2f}"
            f"{interest:>15.2f}"
            f"{balance:>18.2f}"
        )


def get_positive_float(message):
    while True:
        try:
            value = float(input(message))

            if value <= 0:
                print("Enter a value greater than zero.")
                continue

            return value

        except ValueError:
            print("Invalid input.")


def get_positive_int(message):
    while True:
        try:
            value = int(input(message))

            if value <= 0:
                print("Enter a value greater than zero.")
                continue

            return value

        except ValueError:
            print("Invalid input.")


def main():

    while True:

        print("\n" + LINE)
        print("           LOAN EMI CALCULATOR")
        print(LINE)

        principal = get_positive_float(
            "Loan Amount (₹): "
        )

        annual_rate = get_positive_float(
            "Annual Interest Rate (%): "
        )

        years = get_positive_int(
            "Loan Tenure (Years): "
        )

        months = years * 12

        emi, total_payment, total_interest = calculate_emi(
            principal,
            annual_rate,
            months
        )

        print("\n" + LINE)
        print("RESULT")
        print(LINE)

        print(f"Loan Amount       : {currency(principal)}")
        print(f"Interest Rate     : {annual_rate:.2f}%")
        print(f"Loan Tenure       : {years} Years")
        print(f"Monthly EMI       : {currency(emi)}")
        print(f"Total Interest    : {currency(total_interest)}")
        print(f"Total Payment     : {currency(total_payment)}")

        choice = input(
            "\nShow Amortization Schedule? (y/n): "
        ).lower()

        if choice == "y":
            amortization_schedule(
                principal,
                annual_rate,
                months,
                emi
            )

        again = input(
            "\nCalculate another loan? (y/n): "
        ).lower()

        if again != "y":
            print("\nThank you!")
            break


if __name__ == "__main__":
    main()