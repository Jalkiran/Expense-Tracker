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
    def show(self):
        if self.expense:
            print('----Expenses----\n')
            for e in self.expense:
                print(f'Date:{e.date}')
                print(f'Category:{e.category}')
                print(f'Amount:{e.amount}')
        else:
            print('----No expenses found!----\n')
    
