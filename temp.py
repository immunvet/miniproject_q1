'''
x = 'a'
while x != 'q':
    print('enter character q to quit')
    user_input = str(input('\nHere\t'))
    x = user_input
'''    
'''   
def credit_card_length():
    
    credit_card_number = input("Please enter your credit card number here:\t")
    while len(credit_card_number) != 8 or credit_card_number[0] == '0':
        print('The number is invalid.')
        user_input=input("Please enter your credit card number here:\t")
        credit_card_number = user_input
'''        
'''       
def credit_card_firstletter():
    while credit_card_number[0] == '0':
        print('INVALID '*100)
        print('Please try to enter valid card number')
        user_input = input("Please enter your credit card number here:\t")
        credit_card_number = user_input
        break
'''
'''
def credit_card_length():
    
    credit_card_number = input("Please enter your credit card number here:\t")
    while len(credit_card_number) != 8 or credit_card_number.startswith('0') == True:
        print('The number is invalid.')
        user_input=input("Please enter your credit card number here:\t")
        credit_card_number = user_input
credit_card_length()    
#credit_card_firstletter()
'''
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''  

#define a list below 10 that are multiples of 3 or 5 
#define a sum of this list 

'''
x = [1,2,3,4,5,6,7,8,9,10]
total = 0
for i in range(1000): 
    if i % 3 == 0 or i %5 == 0:
        total = total + i
print(total)
 '''  
'''    
def find_numbers_for_func():
    global rnng
    rnng = int(input('Enter range of numbers,please:\t'))
    global b 
    b = int(input('ENter number 1:\t'))
    global c
    c = int(input('Enter number 2:\t'))
    

def find_sum_of_multiples(rang=int(rnng),mult1=int(b),mult2=int(c)):
    
    total = 0
    for i in range(rang):
        if i % mult1 == 0 or i % mult2 == 0:
            total += i
    print(total)

def main():
    find_numbers_for_func()
    find_sum_of_multiples()

main()    
'''
            



















'''
daily_revenues = [
    2356.23,  # Monday
    1800.12,  # Tuesday
    1792.50,  # Wednesday
    2058.10,  # Thursday
    1988.00,  # Friday
    2002.99,  # Saturday
    1890.75   # Sunday
]

#weekly revenue
#average daily revenue
total = 0
for i in daily_revenues:
    total += i
    print(total)
'''

'''
def func_to_change_letter(string, letter_to_change, new_letter):
    try:  
        if new_letter.isdigit() != True:
            changed_string = string.lower().replace(letter_to_change.lower(),new_letter.lower())
            print(changed_string)
    except:
        print('You are entering digit, please try one more time')
        
        

func_to_change_letter('Hello, World!','l','Hui')

'''

import pandas as pd 

location = r'./donor.tsv'
df = pd.read_csv(location, delimiter = '\t',encoding = 'utf-8')
df_dlbcl = df[(df.donor_diagnosis_icd10 == 'C83.3')]
df_dlbcl.to_csv('dlbcl.csv',encoding = 'utf-8',index = False)

loc = r'./dlbcl.csv'
new_df = pd.read_csv(loc, delimiter = ',', encoding = 'utf-8')
donor_ids = new_df['icgc_donor_id']
donor_ids.to_csv('donor_ids.csv', encoding = 'utf-8', index = False, header = 'icgc_donor_id')
#print(donor_ids)

loc1 = r'./mirna_seq.tsv'
mi_rna = pd.read_csv(loc1,delimiter= '\t', encoding = 'utf-8')
mi_rna.to_csv('mi_rna_csv.csv',encoding = 'utf-8',index = False)


mi_rna_csv = pd.read_csv(r'./mi_rna_csv.csv')
don_ids = pd.read_csv(r'./donor_ids.csv')
joined = pd.merge(mi_rna_csv,don_ids)
header = ['icgc_donor_id','mirna_id','normalized_read_count','raw_read_count']

joined.to_csv('mi_rna_dlbcl.csv',columns = header, encoding = 'utf-8',index = False)

#mi_rna_dlbcl = mi_rna_csv[(mi_rna_csv.icgc_donor_id == don_ids.icgc_donor_id)]
#mi_rna_dlbcl.to_csv('mi_rna_dlbcl.csv',encoding = 'utf-8',index = False)
#print(mi_rna_dlbcl)













 
    
    

    



















    

   

    
