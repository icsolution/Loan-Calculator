import argparse
import math

# calculate differentiated payments
def diff(principal, periods, interest):
    interest = interest / 100 / 12
    total = 0
    for month in range(1, periods + 1):
        result = math.ceil(principal / periods + interest * (principal - (principal * (month - 1)) / periods))
        print(f'Month {month}: payment is {result}')
        total += result
    print(f'\nOverpayment = {total - principal}')

# calculate annuity monthly payments
def monthly_payments(principal, periods, interest):
    interest = interest / 100 / 12
    result = math.ceil(principal * ((interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1)))
    print(f'Your annuity payment = {result}!')
    print(f'Overpayment = {result * periods - principal}')

# calculate loan principal
def loan_principal(payment, periods, interest):
    interest = interest / 100 / 12
    result = int(payment / ((interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1)))
    print(f'Your loan principal = {result}!')
    print(f'Overpayment = {payment * periods - result}')

# calculate number of months
def total_months(principal, payment, interest):
    interest = interest / 100 / 12
    result = math.ceil(math.log((payment / (payment - interest * principal)), (1 + interest)))
    if result % 12 == 0:
        total = 'year' if result == 12 else 'years'
        print(f'It will take {result // 12} {total} to repay this loan!')
        print(f'Overpayment = {result * payment - principal}')
    else:
        years = n // 12
        months = n % 12
        s_years = 'year' if y == 1 else 'years'
        s_months = 'month' if m == 1 else 'months'
        if y > 0:
            print(f'It will take {years} {s_years} and {months} {s_months} to repay this loan!')
            print(f'Overpayment = {result * payment - principal}')
        else:
            print(f'It will take {months} {s_months} to repay this loan!')
            print(f'Overpayment = {result * payment - principal}')

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', choices=['diff', 'annuity'])
    parser.add_argument('--principal', type=int, default=False)
    parser.add_argument('--periods', type=int, default=False)
    parser.add_argument('--interest', type=float, default=False)
    parser.add_argument('--payment', type=int, default=False)

    args = parser.parse_args()


    if args.type == 'diff':
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            diff(args.principal, args.periods, args.interest)
    if args.type == 'annuity':
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            monthly_payments(args.principal, args.periods, args.interest)
        elif args.payment > 0 and args.periods > 0 and args.interest > 0:
            loan_principal(args.payment, args.periods, args.interest)
        elif args.principal > 0 and args.payment > 0 and args.interest > 0:
            total_months(args.principal, args.payment, args.interest)
        else:
            print('Incorrect parameters')

if __name__ == '__main__':
    Main()
