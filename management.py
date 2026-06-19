from expense import Expense
class ExpenseManagement:
    def __init__(self):
        self.expense=[]
    def add(self):
        amount=int(input('Enter Amount:'))
        category=input('Enter Category:').title
        date=input('Date:')
        e=Expense(amount,category,date)
        self.expense.append(e)
        print('---Expense Added Successfully!---\n')
    