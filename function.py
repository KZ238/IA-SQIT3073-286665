#Import Pandas and OS into the module.#
import pandas as pd
import os

#User verification Function based on IC No and password.#
def verify_user(ic_number, password):
    """For user's credentials verification purposes"""
    if len(ic_number) == 12 and password == ic_number[-4:]:
        return True
    return False

#Tax calculation function based on user's income and tax relief.#
def calculate_tax(income, tax_relief):
    """Calculate the tax payable based on the Malaysian tax rates for the current year"""
    taxable_income = income - tax_relief
    tax_payable  = 0

    if taxable_income <= 5000:
        tax_payable = 0
    elif taxable_income <= 20000:
        tax_payable = (taxable_income - 5000) * 0.01
    elif taxable_income <= 35000:
        tax_payable = 150 + ((taxable_income - 20000) * 0.03)
    elif taxable_income <= 50000:
        tax_payable = 600 + ((taxable_income - 35000) * 0.06)
    elif taxable_income <= 70000:
        tax_payable = 1500 + ((taxable_income - 50000) * 0.11)
    elif taxable_income <= 100000:
        tax_payable = 3700 + ((taxable_income - 70000) * 0.19)
    elif taxable_income <= 400000:
        tax_payable = 9400 + ((taxable_income - 100000) * 0.25)
    elif taxable_income <= 600000:
        tax_payable = 84400 + ((taxable_income - 400000) * 0.26)
    elif taxable_income <= 2000000:
        tax_payable = 136400 + ((taxable_income - 600000) * 0.28)
    else:
        tax_payable = 528400 + ((taxable_income - 2000000) * 0.3)

    return tax_payable

#Data saving function.#
def save_to_csv(data, filename):
    """Save user's data to a CSV file"""
    df = pd.DataFrame([data])
    df['Income (RM)'] = df['Income (RM)'].round(2)
    df['Tax Relief (RM)'] = df['Tax Relief (RM)'].round(2)
    df['Tax Payable (RM)'] = df['Tax Payable (RM)'].round(2)
    file_exists = os.path.isfile(filename)
    
    if not file_exists:
        df.to_csv(filename, index_label='No', mode='w', header=True)
    else:
        df.to_csv(filename, index = False, header = False, mode ='a')

#Data reading from CSV file function.#
def read_from_csv(filename):
    """Read data from CSV file"""
    if not os.path.isfile(filename):
        return None
    
    else:
        return pd.read_csv(filename, dtype = {'IC No' : str})

