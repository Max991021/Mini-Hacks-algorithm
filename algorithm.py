import random 
import sys

def people():
    
    with open('available_people.txt', 'r', errors='ignore') as file:
        contents = file.read()
        
        people = [element for element in contents.strip().split()]
        print(people)
        if len(people)==0:
            print('No People listed')
            sys.exit()
        count = 0
        groupselection = {}
        
        while len(people)>1:
            count += 1
            
            try:
                if len(people)%2 == 0:
                    peeps = random.sample(people, k=2)
                    groupselection['Group: '+str(count)] = peeps
                        
                    for ind,ele in enumerate(peeps):
                        people.pop(people.index(ele))
                else:
                    print(f"The group is missing one person to complete the algorithm, the count of people is {len(people)} with the names {people}")
                    break
            except ValueError as e:
                e = f"The group is missing one person to complete the algorithm, the count of people is {len(people)} with the names {people}"
                print(e)
                
        else:
            print('No people chosen or list is less than 2 people')
        
        with open('Teams.txt', 'w', errors='ignore') as writefile:
            writefile.write(f'Thank you all for participating in the Mini Hacks-----Happy Coding')
            writefile.write(f'\n-------------These will be your groups for the week----------------\n')
            for key,value in groupselection.items():
                writefile.write(f'{key} will be {value}\n')
                
    
people()
         
    
    