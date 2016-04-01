
import subprocess #for using linux command with python
import operator #for sorting

#files to be compared
arrayA = ['1.py', '2.py','3.py', '4.py', '5.py', '6.py' ,'7.py', '8.py', '9.py', 
          '10.py', '11.py', '12.py', '13.py', '14.py', '15.py', '16.py', '17.py']
arrayB = ['1.py', '2.py','3.py', '4.py', '5.py', '6.py' ,'7.py', '8.py', '9.py', 
          '10.py', '11.py', '12.py', '13.py', '14.py', '15.py', '16.py', '17.py']



def explode_file(name): #function to explode filename
    name_array = name.split('.')
    return name_array[0]
def swap(name): #function that swap names of files example making 1.py 2.py to 2.py 1.py
    swap = name.split(',')
    return swap[1] + ',' + swap[0]

loop_array = [] #array that hold comparison that has already been made so as not to duplicate. 
percentage_array = {} #dictionary that holds final result
for arow in arrayA:
    for brow in arrayB:
        aname = explode_file(arow)
        bname = explode_file(brow)
        name = aname+','+bname
        if arow != brow: 
            if not name in loop_array:           
                aname = explode_file(arow)
                bname = explode_file(brow)
                name = aname+','+bname
                swap_name = swap(name) #swap function is called so as not to repeat comparison example 1.py and 2.py is the same as 2.py and 1.py
                loop_array.append(swap_name)
                
                diff = 'wdiff -si123 ' + arow + ' ' + brow 
                popen = subprocess.Popen(diff, shell = True, stdout = subprocess.PIPE)

                output = popen.communicate()
                percentage_output = output[0]
                percent_end = percentage_output.find('%')               
                percent_start = percentage_output[:percent_end].rfind(' ')
                percentage = int(percentage_output[percent_start:percent_end]) 
                percentage_array[name] = percentage #I used the name of the file as the key for this array so that each combination is unique
                
              
sorted_percentage = sorted(percentage_array.items(), key=operator.itemgetter(1),reverse=True) #sorted array from most similar to least similar based on the value
for diff in sorted_percentage:
    diff_string = str(diff)
    
    diff_string = diff_string.replace("(","") #stripped charcters not needed
    diff_string = diff_string.replace(")","")
    diff_string = diff_string.replace("'","")
    str_ex = diff_string.split(',')
    
    file1 = 'Files '+str_ex[0]+ '.py' #put result in a readable format
    file2 = ' and '+str_ex[1]+ '.py'
    percentage = ' are' +str_ex[2]+ '% similar'
    
    comparison = file1 + file2 + percentage
    
    
    print comparison 


    
            
            
            




