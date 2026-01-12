#AB 1st Finacial Calculator

#Project analysis
#Save Goal
#inputs amount, amount of months
#output amount per prefered consis
#Actions:
#amount divided by # of months


#Compound Interest
#inputs starting amount, interest percentage, time
#output end amount
#Actions:
#starting amount multiplyed by interest
#do this for an amount of time

#Budget
#input catigory, catigory percentage, income 
#output amount per catigory
#Actions:
#income multiplied by catigory percentage
#save and repeat

#Sale Price
#input starting price, percentage off
#output sale price
#Actions:
#starting price multiplied by percentage

#Tip
#input cost, tip percentage
#output total cost
#Actions:
#cost mulitiplied by percentage
#add percentage to cost

#Pseudocode
#FUNCTIONS
#multiply function
    #take two numbers get the product
    #return the product

#divide function
    #take two numbers and get the quotient
    #return the quotient

#Save Goal function
    #parameters are the amount you want to save(save) and amount per interval(amount)
    # time is call the divide funtion with the total as the numerator and the amount as the denominator for the arguments
    #frequency is the input the the quetion of months or weeks
    #return a message with all the info

#Compond Interest function
    #parameters are the starting amount and the interest percentage
    #start is the starting amount
    #interest is the interest percentage
    #time is the number of months the money will be left
    #for i in time
        #interest funtion
            #start multiplied by interest
            #return start
    #return interest

#Budget funtion
    #parameters are a kwarg of all the catigories and the percentages  and you income
    #for i in kwarg.key
        #number is call multiply funtion and use the percentage and income
        #i is number
    #return kwarg

#Sale price funtion
    #parameters are starting price(price) and the sale percentage (percent)
    #pecent_two is 100 - pecent
    #new_price is to call the multiply funtion and use percent_two and price as arguments
    #return new_price

#Tip funtion
    #parameters are the cost of the meal and the tip percentage
    #tip is 100 + percent
    #total is call multiply funtion with cost and tip as arguments
    #return total

#Main funtion
    #parameters choice
    #based on the number that is what action will be completed
    #for each there will be local variale that are inputs that will be the arguments for the specific funtion
    #return the answer of the desired funtion

#Main loop
#while true
    #print message about the program
    #print a message about the options with a corrisponding number
    #choice is what number
    #call main with choice
    #choice_two is ask if they would like to complete another action
    #if yes the contiue
    #else break

#Code
def multiply(num_1, num_2):
    num = num_1 * num_2
    return num

def divide(numerator, denominator):
    num = numerator / denominator
    return num

def save_goal(save, amount):
    time = int(divide(save, amount))
    print("""
             1. Weeks
             2. Months""")
    frequency = input("Enter here: ").strip()
    if frequency == "1":
        frequency = "weeks"
    else:
        frequency = "months"
    return f"It will take {time} {frequency} to save ${save:.2f}."

def compound_interest(start, interest, time):
    amount = start
    new_interest = (100 + interest) / 100
    for i in range(time):
        amount = multiply(amount, new_interest)
    return f"If you leave ${start:.2f} for {time} months with an interest of {interest}%, you will have ${amount:.2f}."

def budget(income, **kwarg):
    def calc_amount(percent):
        return multiply(income, percent / 100)
    
    result = ""
    for key in kwarg:
        amount = calc_amount(kwarg[key])
        result += f"For your {key} you need ${amount:.2f}.\n"
    return result

def sale(price, percent):
    percent_two = (100 - percent) / 100
    new_price = multiply(price, percent_two)
    return f"Your new sale price is ${new_price:.2f}."

def tip(cost, percent):
    tips = (100 + percent) / 100
    total = multiply(cost, tips)
    return f"When your meal cost ${cost:.2f} and you tip {percent}%, your total cost is ${total:.2f}."

def main(choice):
    if choice == "1":
        save = float(input("How much do you want to save: "))
        frequency = float(input("How much will you deposit each week or month: "))
        answer = save_goal(save, frequency)
    
    elif choice == "2":
        start = float(input("How much do you want to put in: "))
        interest = float(input("What is the interest percentage: "))
        time = int(input("How many months will you leave it: "))
        answer = compound_interest(start, interest, time)
    
    elif choice == "3":
        income = float(input("What is your income per month: "))
        kwarg = {}
        total_percent = 0
        print("Enter each budget category and what percentage of your income it should get. Total cannot exceed 100%. Type 'done' when finished.")
        
        while True:
            name = input("Category Name: ").strip()
            if name.lower() == "done":
                break
            percent_input = input("Percent of income: ").strip()
            
            if not percent_input.replace(".", "", 1).isdigit():
                print("Please enter a valid number for percentage.")
                continue
            
            percent = float(percent_input)
            if percent < 0:
                print("Percent must be positive.")
                continue
            if total_percent + percent > 100:
                print("That would put you over 100%. Try a smaller percentage.")
                continue
            
            kwarg[name] = percent
            total_percent += percent
        
        answer = budget(income, **kwarg)
    
    elif choice == "4":
        start = float(input("What is the original price: "))
        percent = float(input("What percent is off: "))
        answer = sale(start, percent)
    
    elif choice == "5":
        cost = float(input("What was the cost of your meal: "))
        tips = float(input("What was the percent of the tip: "))
        answer = tip(cost, tips)
    return answer

while True:
    print("""This is a financial calculator.
You have 5 options of calculations you can make:
1. Saving Goal
   Tells you how many weeks or months it will take to save a certain amount if you deposit a certain amount.
2. Compound Interest
   Tells you how much money you will have when leaving it with interest for a period of time.
3. Budget Allocator
   Tells you how much money you need to put into each of your budget categories based on percentages.
4. Sales Price Calculator
   Tells you the sales price based on the original price and percentage off.
5. Tip Calculator
   Calculates the tip you need to pay based on the cost of your meal and the percentage.""")

    choice = input("Input the number of the action to complete: ").strip()
    print(main(choice))
    
    choice_two = input("Would you like to quit? Input 1 for yes, 2 for no: ").strip()
    if choice_two == "2":
        continue
    else:
        print("Thank you for using the financial calculator.")
        break

    

    


