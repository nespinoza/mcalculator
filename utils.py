import numpy as np

def monthly_payment(loan, downpayment, n, rmonth):
    """
    This function returns the monthly payment expected from a loan given a downpayment, 
    assuming payment over n months, and a per-month-interest rate rmonth. Doesn't consider 
    property tax or insurance.
    """
    f1 = rmonth * (loan - downpayment) * ( (1. + rmonth)**(n) )
    f2 = (1. + rmonth)**(n) - 1.
    return f1/f2

def return_schedule(loan, downpayment, n, rmonth):
    """
    This function returns the payment schedule for the principal (i.e., total amount 
    of money that went to the principal) and the interest (i.e., total 
    amount of money going to interest) each month.

    Returns two arrays, one for the principal, one for the interest.
    """
    # Prepare arrays:
    principal = np.zeros(n)
    interest = np.zeros(n)

    # Calculate monthly payment:
    Pmonth = monthly_payment(loan, downpayment, n, rmonth)

    # Fill arrays:
    for i in range(n):
        if i == 0:
            interest[i] = (loan - downpayment)*rmonth
        else:
            interest[i] = (loan - downpayment - np.sum(principal[:i]))*rmonth
        principal[i] = Pmonth - interest[i]
    print('Monthly payment is:',Pmonth,'USD')
    return principal, interest

def return_cummulative_schedule(loan, downpayment, n, rmonth):
    """ 
    This function returns the *cummulative* payment schedule for the principal (i.e., total amount 
    of money that went to the principal) and the interest (i.e., total 
    amount of money going to interest) each month. Useful for comparing how much money you have left to 
    pay (e.g., to sell a house/car while mortgage still going).

    Returns two arrays, one for the principal, one for the interest.
    """

    # Prepare arrays:
    principal = np.zeros(n)
    cummulative_principal = np.zeros(n)
    interest = np.zeros(n)
    cummulative_interest = np.zeros(n)

    # Calculate monthly payment:
    Pmonth = monthly_payment(loan, downpayment, n, rmonth)

    # Fill arrays:
    for i in range(n):
        if i == 0:
            interest[i] = (loan - downpayment)*rmonth
        else:
            interest[i] = (loan - downpayment - np.sum(principal[:i]))*rmonth
        principal[i] = Pmonth - interest[i]
        cummulative_interest[i] = np.sum(interest[:i+1])
        cummulative_principal[i] = np.sum(principal[:i+1])
    print('Monthly payment is:',Pmonth,'USD')
    return cummulative_principal, cummulative_interest
