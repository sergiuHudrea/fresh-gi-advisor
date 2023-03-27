
def theCleaner():

    print("Welcome to your So Fresh & So Clean GI advisor!")
  

    ownGi = ""
    while ownGi != "y" and ownGi != "n":
        ownGi = input("Are you wondering how to properly clean and take care of your beloved gi? (y/n): ")
        print("")
        if ownGi == "y":
            print("Perfect, let's get started!")
        elif ownGi =="n":
            print("I am sorry, but I think I cannot be of service for you in that case... I am a mere Fresh Gi Advisor.")
            return print("OSSS")

    typeOfCleaning = ""
    stain = ""
    while typeOfCleaning != "normal" and typeOfCleaning != "specific":
        typeOfCleaning = input("Are you looking to find out about normal maintenance or something more specific? (normal/specific): ")
        if typeOfCleaning == "normal":
            print("")
            print("Great, here are a few basic things to know for properly taking care of your Gi: ")
            print(" • Wash your Gi as soon as you can after training, this will stop the sweat impregnate the cotton.")
            print(" • Wash your Gi at cold temperatures, never higher than 40º.")
            print(" • Avoid softeners, this will damage the cotton fibers.")
            print(" • Hang dry as washer dryers will shrink your Gi to the size of a pea.")
            print(" • Don't forget to put in the was that cool belt as well!")
            print(" • Wash your Gi after every training session, your Gi and your training partners will deeply appreciated it.")
            print("")
        elif typeOfCleaning == "specific":
            specificity = input("I see, is it about a stain then? (y/n): " )
            
    print("Hope you got something out of me my friend! OSSS")






theCleaner()
