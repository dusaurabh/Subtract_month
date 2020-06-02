

"""
implement function 'subtract_months' to subtract 'n' number of months from a given year and month.

Inputs: Is a list of tuples [(year1, month1, months_to_subtract1), (year2, month2, months_to_subtract2), ...] 
where, year is a 4 digit integer
month is an interger value between 1 to 12, 1=January, 2=February, ... 12=December) and 
months_to_subtract is an integer

Output: Is a list of tuples [(result_year1, result_month1), (result_year2, result_month2), ...] 
year (4 digit integer) month (interger value between 1 to 12, 1=January, 2=February, ... 12=December)

For example: subtract 3 months from May 2020. This should result in an output Feb 2020
In this example inputs: year=2020 month=5
output: year=2020 month=2



"""

def subtract_months(year,month,sub_month):
    output_list = []
  
    result_month = 0
    result_year = 0
    if month > (sub_month % 12):
        result_month = month - (sub_month % 12)
        result_year = int((year - (sub_month / 12))+1)
    else:
        result_month = 12 - (sub_month % 12) + month
        result_year = int((year - (sub_month / 12 + 1))+1)
    output_list.append((result_year,result_month))
    

    return output_list

print(subtract_months(2020,5,3)) # You can change this value with your custom year and month value 

