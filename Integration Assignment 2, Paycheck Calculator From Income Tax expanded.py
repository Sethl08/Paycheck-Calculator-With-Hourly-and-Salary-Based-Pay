type_of_pay = input(
    "Hourly pay or Salary based? "
    )
if type_of_pay == "Hourly pay" or type_of_pay == "Hourly Pay" or type_of_pay == "Hourly" or type_of_pay == "hourly" or type_of_pay == "hourly pay" or type_of_pay == "hourly Pay":
    hours_per_week = float(
        input(
            "How many hours do you work? "
            )
        )
    money_per_hour = float(
        input(
            "How much do you make per hour? "
            )
        )
    overtime_or_not = input(
        "Do you have overtime? "
        )
    if overtime_or_not == "Yes" or overtime_or_not == "yes":
        overtime_hours = float(
            input(
                "How many hours of overtime? "
                )
            )
        overtime_per_hour = float(
            input(
                "How much do you make for overtime? "
                )
            )
        total_overtime_pay = float(
            overtime_hours * overtime_per_hour
            )
        income_tax = float(
            input(
                "What is your income tax? (Don't include the %) "
                )
            )
        income_tax_as_a_decimal = float(
            income_tax / 100
            )
        tax_paid = float(
            (
                (
                    hours_per_week * money_per_hour
                    ) + total_overtime_pay
                ) * income_tax_as_a_decimal
            )
        total_money_made = float(
            (
                hours_per_week * money_per_hour
                ) + total_overtime_pay
            )
        take_home_pay = float(
            total_money_made - tax_paid
            )
        print(
            "Money taken home: ", "$" + format(
                take_home_pay, '.2f'
                )
            )
    else:
        income_tax = float(
            input(
                "What is your income tax? (Don't include the %) "
                )
            )
        income_tax_as_a_decimal = float(
            income_tax / 100
            )
        tax_paid = float(
            (
                (
                    hours_per_week * money_per_hour
                    )
                ) * income_tax_as_a_decimal
            )
        total_money_made = float(
            (
                hours_per_week * money_per_hour
                )
            )
        take_home_pay = float(
            total_money_made - tax_paid
            )
        print(
            "Money taken home: ", "$" + format(
                take_home_pay, '.2f'
                )
            )
elif type_of_pay == "Salary pay" or type_of_pay == "Salary Pay" or type_of_pay == "Salary" or type_of_pay == "salary" or type_of_pay == "salary pay" or type_of_pay == "salary Pay":
    annual_salary = float(
        input(
            "What is your annual salary? (Don't include the $) "
            )
        )
    pay_periods = input(
        "Paid weekly, bi-weekly, semi-monthly, or monthly? "
        )
    if pay_periods == "Weekly" or pay_periods == "weekly":
        weekly_paycheck = (
            annual_salary / 52
            )
        income_tax = float(
            input(
                "What is your income tax? (Don't include the %) "
                )
            )
        income_tax_as_a_decimal = float(
            income_tax / 100
            )
        tax_paid = float(
            weekly_paycheck * income_tax_as_a_decimal
            )
        take_home_pay = float(
            weekly_paycheck - tax_paid
            )
        print(
            "Money taken home: ", "$" + format(
                take_home_pay, '.2f'
                )
            )
    elif pay_periods == "Bi-weekly" or pay_periods == "bi-weekly" or pay_periods == "Bi-Weekly" or pay_periods == "bi-Weekly":
        bi_weekly_paycheck = (
            annual_salary / 26
            )
        income_tax = float(
            input(
                "What is your income tax? (Don't include the %) "
                )
            )
        income_tax_as_a_decimal = float(
            income_tax / 100
            )
        tax_paid = float(
            bi_weekly_paycheck * income_tax_as_a_decimal
            )
        take_home_pay = float(
            bi_weekly_paycheck - tax_paid
            )
        print(
            "Money taken home: ", "$" + format(
                take_home_pay, '.2f'
                )
            )
    elif pay_periods == "Semi-monthly" or pay_periods == "Semi-Monthly" or pay_periods == "semi-monthly" or pay_periods == "semi-Monthly":
        semi_monthly_paycheck = (
            annual_salary / 24
            )
        income_tax = float(
            input(
                "What is your income tax? (Don't include the %) "
                )
            )
        income_tax_as_a_decimal = float(
            income_tax / 100
            )
        tax_paid = float(
            semi_monthly_paycheck * income_tax_as_a_decimal
            )
        take_home_pay = float(
            semi_monthly_paycheck - tax_paid
            )
        print(
            "Money taken home: ", "$" + format(
                take_home_pay, '.2f'
                )
            )
    elif pay_periods == "Monthly" or pay_periods == "monthly":
        monthly_paycheck = (
            annual_salary / 12
            )
        income_tax = float(
            input(
                "What is your income tax? (Don't include the %) "
                )
            )
        income_tax_as_a_decimal = float(
            income_tax / 100
            )
        tax_paid = float(
            monthly_paycheck * income_tax_as_a_decimal
            )
        take_home_pay = float(
            monthly_paycheck - tax_paid
            )
        print(
            "Money taken home: ", "$" + format(
                take_home_pay, '.2f'
                )
            )
    else:
        print(
            "Invalid pay periods"
            )
else:
    print(
        "Invalid Payment Type"
        )
