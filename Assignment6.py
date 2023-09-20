#create an empty dictionary to store employee details 
employee = {}
#get employee details from the user input
domain = input("Enter the domain:")
name = input("Enter the name:")
empid = input("Enter employee ID:")
email = input("Enter the email:")
#add empolyee details in dictionary
employee["Domain"]= domain
employee["Name"]= name
employee["Employee ID"]= empid
employee["Email"]= email
print("employee Details:")
for key, values in employee.items () :
    print(key=+":"+values)