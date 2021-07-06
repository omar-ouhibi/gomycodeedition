amt = int(input("Enter Sale Amount: "))
if(amt>0):
    if amt>=500:
       disc = amt*0.5
    elif amt>=200 & amt<=500:
        disc=amt*0.3
    elif amt<=200:
         disc=0.1 * amt

    print("Discount : ",disc)
    print("Net Pay  : ",amt-disc)
else:
    print("Invalid Amount")