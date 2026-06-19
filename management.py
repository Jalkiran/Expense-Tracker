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
    def total(self):
            if self.expense:
                total={}
                for e in self.expense:
                    if e.category in total:
                        total[e.category]+=e.amount
                    else:
                        total[e.category]=e.amount
                print('----Category Wise Total----\n')
                for category,amount in total.items():
                    print(f'{category}: {amount}')
            else:
                print('----No expenses found----\n')
    def save(self):
        data=[]
        for e in self.expense:
            data.append({'Amount':e.amount,'Category':e.category,'Date':e.date})
        with open('expenses.json','w')as f:
            f.dump(data,f,indent=4)
        print('Expenses Saved Successfully')
