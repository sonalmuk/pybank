test="first home work"
print('This is 2nd  test')

import os
import csv

csvpath=os.path.join(".","Resources","budget_data.csv")
monthcnt=0
total=0
orig_col=[]
shifted_col=[]
diff_col=[]
shifted_val=0
prev_value=0
diff_val=0
with open(csvpath) as csvfile:
    cvsreader=csv.reader(csvfile,delimiter=",")
    headerline=next(csvfile)
    #monthcnt=sum(1 for line in cvsreader)
    for row in cvsreader:
        total+=int(row[1])
        monthcnt=monthcnt+1
        print(f'prevval {prev_value}')
        if (prev_value==0):
            diff_val=0
        else:
            diff_val=int(row[1])-prev_value
        print(f'diffval {diff_val}')
        row.append(prev_value)
        row.append(diff_val)
        prev_value=int(row[1])
        diff_col.append(diff_val)
        print(row)
    #for cols in cvsreader:
        #print(f"total # of months : {sum(1 for line in cvsreader)}")
        #monthcnt=monthcnt+1
    print('Finanial Analysis')
    print('------------------------')
    print(f'Total Months:{monthcnt}')
    print(f'Total: ${total:,.2f}')
    print(f'Average Change:${sum(diff_col)/monthcnt:,.2f}')
    print(f'Greatest Increase in Profits:${max(diff_col):,.2f}')
    print(f'Greatest Decrease in Profits:${min(diff_col):,.2f}')
    
    csvpathoutput =os.path.join(".","output","budget_data_analysis.txt")
    csvwriter= open(csvpathoutput,'w')
        #csvwriter=csv.writer(csvfile)
        
    csvwriter.write('Finanial Analysis\n')
    csvwriter.write('------------------------\n')
    csvwriter.write(f'Total Months:{monthcnt}\n')
    csvwriter.write(f'Total: {total}\n')
    csvwriter.write(f'Average Change:{sum(diff_col)/monthcnt}\n')
    csvwriter.write(f'Greatest Increase in Profits:{max(diff_col)}\n')
    csvwriter.write(f'Greatest Decrease in Profits:{min(diff_col)}\n')
    csvwriter.close()
#print(monthcnt-1)    

    