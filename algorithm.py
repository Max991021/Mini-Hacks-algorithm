import random 

def people():
    listinput = input('Names of people in the mini hacks?: ')
    people = [element for element in listinput.strip().split(',')]
    
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
    
    print(groupselection)
    
people()
            
        
    
    