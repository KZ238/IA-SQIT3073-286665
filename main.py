import pandas as pd
import functions as funct

def main():
    filename = 'IA.csv'

    print("++++++++++Welcome to the Malaysian Tax Calculation System++++++++++")

    registered_users = funct.read_from_csv(filename)

    if registered_users is None:  #Check the data availability or the existence of CSV file.#
        registered_users = pd.DataFrame(columns = ['ID', 'IC No', 'Income (RM)', 'Tax Relief (RM)', 'Tax Payable (RM)'])
        registered_users.index = range(1, len(registered_users) + 1)
        
    
    user_action = input("Are you a registered user? (Yes/No): ").strip().lower()

    if user_action == 'no':
        id = input("Enter your ID: ")
        ic_number = str(input("Enter your IC number(Without '-'): "))

        print("Registration: Your IC number will be used as your password.")
        ic_password = ic_number[-4:]
        confirm_password = input("Confirm your password (last 4 digits of your IC): ")
        while ic_password != confirm_password:
            print("Passwords do not match. Please try again.")
            return main()
            
        print("Registration successful. Please log in.")
        return main()
    
    elif user_action == 'yes':
        id = input("Enter your ID: ")
        ic_number = str(input("Enter your IC number: "))
        ic_password = input("Enter your password (last 4 digits of your IC): ")

        while not funct.verify_user(ic_number, ic_password):
            print("Invalid credentials. Please try again.")
            return main()
    
    else:
        print("Invalid option. Please enter 'Yes' or 'No'.")
        return main()
    
    print("Login successful.")

    try:
        annual_income = float(input("Enter your annual income in ringgit (RM): " ))
        tax_relief = float(input("Enter your total tax relief amount in ringgit (RM):"))

    except ValueError:
        print("Invalid input.Please enter numeric values only for annual income and tax relief.")
        return main()
    
    tax_payable = funct.calculate_tax(annual_income, tax_relief)
    print(f"Your calculated tax payable is RM{tax_payable:.2f}")

    #Create dictionaries of user data after prompting their input.#
    user_data = {
        'ID': id,
        'IC No': str(ic_number),
        'Income (RM)': annual_income,
        'Tax Relief (RM)': tax_relief,
        'Tax Payable (RM)': tax_payable
        }
    
    #Save data to CSV file and notify user that his/her data has been saved.#
    funct.save_to_csv(user_data,filename)
    print("Your data has been saved successfully.")

    #Print the records in CSV file#
    records = funct.read_from_csv(filename)
    if records is not None:
            print(records)
        
#Calling the main() method.#
if __name__ == "__main__":
    main()        




