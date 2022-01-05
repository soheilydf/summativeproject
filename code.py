print("i have changed the code again *2   ") 
def function(intlist,strlist):                
        if (len(intlist) == len(strlist)):
            newlist = []
            count = 0
            while(count < len(intlist)):           
                item1 = str(intlist[count])       
                item2 = strlist[count] 
                item3 = item1 + item2      
                newlist.append(item3)    
                count += 1
            print("complete!")
            print("The new list is: ",newlist)
            return newlist
        elif(len(intlist) != len(strlist)):
            print("sorry this function will not work")
