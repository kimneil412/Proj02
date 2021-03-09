#####################################################
# Computer Project #2
# Algorithms
# Loops
# Prompt for inputs
# Using the inputs for calculations
# Display the calculations
# Diplay a closing message
#####################################################

# Prints the welcome statement
BANNER = "\nWelcome to car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BDW) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)"
# Asks the user for string to continue
PROMPT = '''\nWould you like to continue (Y/N)? '''
# All the variables used for inputs
cc = "\nCustomer code (BDW): "
days = "\nNumber of days: "
os = "Odometer reading at the start: "
oe = "Odometer reading at the end:   "
invalid = "\n\t*** Invalid customer code. Try again. ***"
cust_sum = "\nCustomer summary:"
class_c = "\tclassification code:"
rent_days = "\trental period (days):"
os_reading = "\todometer reading at start:"
oe_reading = "\todometer reading at end:"
miles = "\tnumber of miles driven:"
total_amount = "\tamount due: $"
ty = "Thank you for your loyalty."

print(BANNER)
in_str = input(PROMPT)
while in_str == 'Y':
    # Recieves input from user
    in_cc = input(cc)
    while not (in_cc == 'B' or in_cc == 'D' or in_cc == 'W'):
        print(invalid)
        in_cc = input(cc)
    in_days = input(days)
    int_days = int(in_days)
    # Converts the inputs to integers then to string
    in_os = input(os)
    int_os = int(in_os)
    str_os = str(int_os)
    in_oe = input(oe)
    int_oe = int(in_oe)
    str_oe = str(int_oe)

# Calculations for customer using code B
    if in_cc == 'B':
        if int_os > int_oe:
            int_oe = int_oe + 1000000
        base_charge = int_days * 40.00
        str_base = str(base_charge)
        miles_mth = (int_oe - int_os) / 10.00
        miles_charge = miles_mth * 0.25
        str_miles_charge = str(miles_charge)
        total_charge = base_charge + miles_charge
        str_total_charge = str(total_charge)
        print(cust_sum)
        print(class_c, in_cc)
        print(rent_days, int_days)
        print(os_reading, str_os)
        print(oe_reading, str_oe)
        print(miles, miles_mth)
        print(total_amount, str_total_charge)
        in_str = input(PROMPT)

# Calculations for customer using code D
    if in_cc == 'D':
        base_charge = int_days * 60.00
        str_base = str(base_charge)
        miles_mth = (int_oe - int_os) / 10.00
        miles_mth1 = miles_mth / int_days
        if miles_mth1 > 100.00:
            miles_charge = (miles_mth - (100.00*int_days)) * 0.25
        else :
            miles_charge = 0 * 0.25
        str_miles_charge = str(miles_charge)
        total_charge = base_charge + miles_charge
        str_total_charge = str(total_charge)
        print(cust_sum)
        print(class_c, in_cc)
        print(rent_days, int_days)
        print(os_reading, str_os)
        print(oe_reading, str_oe)
        print(miles, miles_mth)
        print(total_amount, str_total_charge)
        in_str = input(PROMPT)

# Calculations for customer using code W
    elif in_cc == 'W':
        if int_days <= 7:
            weeks = 1
        else :
            if (int_days % 7 == 0):
                weeks = int_days/7
            else :
                weeks = int(int_days/7) + 1
        base_charge = 190.00 * weeks
        str_base = str(base_charge)
        miles_mth = (int_oe - int_os) / 10.00
        miles_mth1 = miles_mth / weeks
        if miles_mth1 <= 900.00 * weeks:
            miles_charge = 0.00
        elif (miles_mth1 > 900) and ( miles_mth1 <= 1500):
            miles_charge = weeks * 100
        else:
            miles_charge = ((miles_mth1 - 1500) * 0.25 * weeks) + (200 * weeks)
        str_miles_charge = str(miles_charge)
        total_charge = base_charge + miles_charge
        total_charge = str(total_charge)
        # Prints out the output
        print(cust_sum)
        print(class_c, in_cc)
        print(rent_days, int_days)
        print(os_reading, str_os)
        print(oe_reading, str_oe)
        print(miles, miles_mth)
        print(total_amount, total_charge)
        in_str = input(PROMPT)

print(ty)