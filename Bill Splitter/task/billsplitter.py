import random

numberofpeople=int(input("Enter the number of friends joining (including you):"))
people=list()
people_dict={}
if numberofpeople<=0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    for i in range(numberofpeople):
        people.append(input())
    bill=int(input("\nEnter the total bill value:"))

    luck=input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    if luck=="Yes":
        lucky=random.choice(people)
        print("\n{} is the lucky one!".format(lucky))
        per = round(bill / (numberofpeople-1), 2)
        for i in people:
            if i == lucky:
                people_dict[i] = 0
            else:
                people_dict[i] = per
        print("\n",people_dict,sep="")
    else:
        print("\nNo one is going to be lucky")
        per = round(bill / numberofpeople, 2)
        for i in people:
            people_dict[i] = per
        print("\n",people_dict,sep="")