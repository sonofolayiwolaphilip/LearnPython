### Function Add expense
1. Prompt the user to input the Expense Name, category, Amount and Description
2. Create a dictionary mapping those inputs to specific Keys(Expense, category, Amount, Description)
3. Open the data file in read mode inside a try/except guard block
Load the existing data into a list, initialize an empty list of the file is not found
Append the new expense dictionary to the data list
Reopen the data file in write mode 
Save the updated list back to the file in a clean JSON format. 

### Function to View All Expense
1. 

### AUDIT FEEDBACK
1. Validate all the inputs. Most especially amount

2. Make some of the field optional, but category, name and amount are mandatory. 
3. validate that the amount inputed is not less than 1 nor negative and can be converted to a float or integer. 
4. 
### AUDIT FEEDBACK
1. Automatic ID assignment upon creation of record. 
2. create a record with ID as key a dictionary as value
3. select from a existing list of categories
