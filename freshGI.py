from asciiAndInstructions import stinky, stainy, normie, oss, gi

def insideCleaner():
        ownGi = ""
        while ownGi != "y" and ownGi != "n":
            ownGi = input("\nAre you wondering how to properly clean and take care of your beloved gi? (y/n): ")
            if ownGi == "y":
                print("\nPerfect, let's get started!")
            elif ownGi =="n":
                print("\nI am sorry, but I think I cannot be of service for you in that case... I am a mere Fresh Gi Advisor.")
                return "n"
            else:
                print("\nSorry, I didn't get that properly.")

        typeOfCleaning = ""
        stain = ""
        newLease = ""
        while typeOfCleaning != "normal" and typeOfCleaning != "specific":
            typeOfCleaning = input("\nAre you looking to find out about normal maintenance or something more specific? (normal/specific): ")

            if typeOfCleaning == "normal":
                print(normie)

            elif typeOfCleaning == "specific":
                while stain != "y" and stain != "n":
                    stain = input("\nIs it about a stain? (y/n): " )
                    
                    if stain == "y":
                      print(stainy)
                    elif stain == "n":
                        while newLease != "y" and newLease != "n":
                            newLease = input("\nIs your Gi stinky from many grueling sessions of grapplling and not applying the tender love and care the Gi deserved? (y/n): ")
                            if newLease == "y":
                                print(stinky)
                            elif newLease == "n":
                                print("\nI am sorry my friend, but in that case I don't know how I can help you... You have reached the bottoms of my superficial intelligence. \nAnwyay...")
                            else:
                                print("\nExcuse me, but I didn't get that.\nAs I was previously saying...")
                    else:
                        print("\nSorry my friend, but I didnt get that...")
            else:
                print("\nSorry my friend, but I didnt get that...")
        return "y"



def theCleaner():
    print(gi)
    print("\nWelcome to your So Fresh & So Clean GI advisor!")
  
    anythingElse = insideCleaner()
    while anythingElse != "n":
        anythingElse = input("\nIs there anything else I can help you with? (y/n): ")
        if anythingElse == "y":
            anythingElse = insideCleaner()
        elif anythingElse == "n":
            print("\nIn that case, it was great conversating with you human.")
        else:
            print("My apologies, but I didn't get that.")

    print("Hope you got something out of me my friend!")
    print(oss)



theCleaner()

