#!/usr/bin/env python3

db = [('William Gates', [653772.32, 12.17]),
        ('Jeff Bezos', [877.33,708.42,3500.00]),
        ('Paul Allen', [663.23, 5443.87, 10123.32]),
        ('Mark Zuckerberg', [1663.23, 4300.87, 10432.0]),
        ]

def donor_list():
    names = []
    for donor in db:
        names.append(donor[0])
    return ('\n'.join(names))

def add_donor(name,amount):

    name = name.strip()
    
    for donor, donations in db:
        # Compare names in current list
        if name.lower() == donor.lower():
            donor = (donor,donations)
            #print (donor[0])
            #print (donations[0])
            donations.append(amount)
            return
        
    donor = (name, [amount])
    db.append(donor)

def main_selection():

    while True:
        

        action = input('''
                Make a choice:
                1 - Send a Thank You
                2 - Create a Report
                Q - Quit'
                ''')

        
        if action == str(1) or action == str(2):
            return action.strip().upper() # Use upper() so strings are always uppercase

        elif action == str('q') or action == str('Q'):
            return action.strip().upper() # Use upper() so strings are always uppercase

        try:
            print ('Try Again')
        except  ValueError:
            continue

            
                    
        


def letter(name,amount):

    thank_you = (f'\nDear {name},\nThank you for your very kind donation of ${float(amount):.2f}. It will be put to very good use.\nSincerely,\n-The Team')
    print (thank_you)
    return thank_you

def thank_you():
    # Get donor information to create thank you letter.
    while True:
        name = input("Enter a donor's name or 'list' to see all donors or 'menu' to exit)\n> ").strip()
        if name == 'list':
            print (donor_list())
        elif name == 'menu':
            break
        
        try:
            amount = float(input('Enter the amount of donation: '))
            letter(name,amount)
            add_donor(name,amount)
            break
        
        except ValueError:
            print('No, start over and input donation amount with cents.')
            #amount = int(input('Enter the amount of donation: '))
            continue
        #else:
            #break

def sort(column):
    # Sort function
    return column[1]

def donor_report():
    
    # Report of the donors and donations.
    report_rows = []
    for (name, gifts) in db:
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))
        
    #print (report_rows)
    # Sort the report data
    
    report_rows.sort(key=sort, reverse=True)
    
    #print (report_rows)
    #Format report.
    report = []
    report.append("\n" * 2)
    report.append("-" * 66)
    report.append(f"{'Donor Name':25s} | {'Total Given':11s} | {'Num Gifts':9s} | {'Average Gifts':12s}")
    report.append("-" * 66)
    
    #for row in report_rows:
    for row in report_rows:
        report.append("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))

    report = ("\n".join(report))
    
    #print (report)
    return report


if __name__ == '__main__':
    
    # 
    while True:
        selection = main_selection()
        if selection == '1':
            thank_you()
        elif selection == '2':
            print (donor_report())
        elif selection == 'Q':
            break
        else:
            print('Wrong Selection')