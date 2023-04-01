'''
To do:
 - Play around with Django
 
Create a blog post using Medium, Dev.to, or some other blogging platform.

Your blog post should include the following:

    A compelling title about your program
    An introduction sharing the background info (the “why”)
    An image or a GIF of your program
    An accompanying paragraph describing your Python code
    A link to your code on GitHub.
    A conclusion

'''

from asciiAndInstructions import stinky, stainy, normie, oss, gi

def insideCleaner(anythingElse):
        ownGi = ""
        while ownGi != "y" and ownGi != "n":
            print("")
            ownGi = input("Are you wondering how to properly clean and take care of your beloved gi? (y/n): ")
            print("")
            if ownGi == "y":
                print("Perfect, let's get started!")
            elif ownGi =="n":
                print("I am sorry, but I think I cannot be of service for you in that case... I am a mere Fresh Gi Advisor.")
                anythingElse = "n"
                return anythingElse
            else:
                print("Sorry, I didn't get that properly.")

        typeOfCleaning = ""
        stain = ""
        newLease = ""
        while typeOfCleaning != "normal" and typeOfCleaning != "specific":
            typeOfCleaning = input("Are you looking to find out about normal maintenance or something more specific? (normal/specific): ")
            print("")
            if typeOfCleaning == "normal":
                print(normie)
            elif typeOfCleaning == "specific":
                while stain != "y" and stain != "n":
                    stain = input("Is it about a stain? (y/n): " )
                    print("")
                    if stain == "y":
                      print(stainy)
                    elif stain == "n":
                        while newLease != "y" and newLease != "n":
                            newLease = input("Is your Gi stinky from many grueling sessions of grapplling and not applying the tender love and care the Gi deserved? (y/n): ")
                            print("")
                            if newLease == "y":
                                print(stinky)
                            elif newLease == "n":
                                print("I am sorry my friend, but in that case I don't know how I can help you... You have reached the bottoms of my superficial intelligence.")
                                print("Anwyay...")
                                print("")
                            else:
                                print("Excuse me, but I didn't get that.")
                                print("As I was previously saying.")
                    else:
                        print("")
                        print("Sorry my friend, but I didnt get that...")
            else:
                print("Sorry my friend, but I didnt get that...")
                
        anythingElse = input("Is there anything else I can help you with? (y/n): ")
        return anythingElse



def theCleaner():
    print(gi)
    print("")
    print("Welcome to your So Fresh & So Clean GI advisor!")
  
    anythingElse = ""
    while anythingElse != "n" and anythingElse != "y":
        print("")
        anythingElse = input("Is there anything else I can help you with? (y/n): ")
        while anythingElse == "y":
            anythingElse = insideCleaner(anythingElse)
        if anythingElse == "n":
            print("")
            print("In that case, it was great conversating with you human.")
        else:
            print("My apologies, but I didn't get that.")

    print("Hope you got something out of me my friend!")
    print(oss)



theCleaner()

