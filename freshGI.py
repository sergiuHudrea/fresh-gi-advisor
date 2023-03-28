def theCleaner():
    print("Welcome to your So Fresh & So Clean GI advisor!")
  
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
                print("OSSS")
                anythingElse = "n"
                return anythingElse
            else:
                print("Sorry, I didn't get that properly.")

        typeOfCleaning = ""
        stain = ""
        newLease = ""
        while typeOfCleaning != "normal" and typeOfCleaning != "specific":
            print("")
            typeOfCleaning = input("Are you looking to find out about normal maintenance or something more specific? (normal/specific): ")
            print("")
            if typeOfCleaning == "normal":
                print("Great, here are a few basic things to know for properly taking care of your Gi: ")
                print(" • Wash your Gi as soon as you can after training, this will stop the sweat impregnate the cotton.")
                print(" • Wash your Gi at cold temperatures, never higher than 40º, and on a gentle wash setting.")
                print(" • To give it a longer lifespan try washing it inside out.")
                print(" • Avoid softeners, this will damage the cotton fibers.")
                print(" • Hang dry as washer dryers will shrink your Gi to the size of a pea, also, avoid direct sunlight, you don't want that midnigt black Gi turn into 50 Shades of Grey.")
                print(" • Don't forget to put in the wash that cool belt as well! Although... BJJ wizards often say that washing the belt can remove its magic abilities.")
                print(" • Wash your Gi after every training session, your Gi and your training partners will deeply appreciated it.")
                print(" • No need to iron your Gi, you'll mess it up in the first 3 minutes of the training anyway.")
                print("")
            elif typeOfCleaning == "specific":
                while stain != "y" and stain != "n":
                    print("")
                    stain = input("Is it about a stain? (y/n): " )
                    print("")
                    if stain == "y":
                        print("Ahh, I remember my first stain. First day of using this brand new white Gi and I got blood all over it (my enemie's of course). It is the white Gi curse...")
                        print("Wait... AI cannot do BJJ, what is happening?")
                        print("Maybe my creator put this thoughts in my neural networks.")
                        print("Anyway, I am straying away from the point.")
                        print("")
                        print("I know stains can be daunting, but there is a very easy way to get them out of your Gi by following these simple steps: ")
                        print(" 1. Apply some hydrogen peroxide on the stain (you can find it in a chemist shop or just order online).")
                        print(" 2. Put some dishwasher liquid on top of the stain and scrub, you should see the stain fading.")
                        print(" 3. Lastly, throw that Gi in the washing machine and let the last part of the spell unfold.")
                        print("")
                    elif stain == "n":
                        while newLease != "y" and newLease != "n":
                            print("")
                            newLease = input("Is your Gi stinky from many grueling sessions of grapplling and not applying the tender love and care the Gi deserved? (y/n): ")
                            print("")
                            if newLease == "y":
                                print("Nothing worse than looking to your beautiful Gi and realising that if you wear it one more time in class, you will probably choke your colleagues with your smelly Gi..")
                                print("But again, no need to worry, I am here to help you on this as well.")
                                print("")
                                print("The only things you need to do are these: ")
                                print(" 1. Put all your gear in the bathtub or a bucket.")
                                print(" 2. Add 2-3 cups of white vinegar and fill the rest of the tub/container with water until the gear is submerged.")
                                print(" 3. Leave it overnight to soak.")
                                print(" 4. Drain it and put it in the wash.")
                                print("")
                                print("Boom!! Now you have a new lease on that cool Gi of yours.")
                                print("Plus, the vinegar for sure helped banish any curse that was casted upon your now holy Gi and your training partner will be enthralled with that unbelievable crispness of your fighting gear.")
                                print("")
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
    

    anythingElse = ""
    while anythingElse != "n" and anythingElse != "y":
        print("")
        anythingElse = input("Is there anything else I can help you with? (y/n): ")
        print("")
        while anythingElse == "y":
            anythingElse = insideCleaner(anythingElse)
        if anythingElse == "n":
            print("In that case, it was great conversating with you human.")
        else:
            print("My apologies, but I didn't get that.")

    print("Hope you got something out of me my friend! OSSS")



theCleaner()
