def main():

    breakFlag = False

    while True:
        
        request = (input("Would you like to give us a rating?(y/n): "))
        
        if (request=="y"):

            while True:

                rating = input("Please rate the app from 1 to 5: ")

                if rating in('1', '2', '3', '4', '5'):

                    if (rating == "1"):
                        print(rating,": Sorry it sucked!")
                            
                    elif (rating == "2"):
                        print(rating,": Not the greatest then?")
                            

                    elif (rating == "3"):
                        print(rating,": We hate being average!")
                            

                    elif (rating == "4"):
                        print(rating,": Only a little bit lame then?")

                    elif (rating == "5"):
                        print(rating,": You're a good sport! Calc projects are lame but thanks for the review!")


                    while True:

                        next = input("Make another rating?(y/n): ")

                        if next!= "y" and next != "n":
                            print("Invalid option!")
                            continue
                        
                        if next == "y":
                            print("Great!")
                            break
                            
                        
                        elif next == "n":
                            print("Thanks for rating!")
                            breakFlag = True
                        break        

                    if breakFlag:
                        break
                                
                else:
                    print("Invalid option!")
                    continue

        
        elif request != "n" and request != "y":
            print("Invalid option!")
            continue

        else:
            print("CLOSED!")
        break




       


            
            