number_of_people = 0
total_vote = 0
average_vote = 0
while True:
    try:
        vote = int(input("Vote form 1 to 5(-1 to quit): "))
        if 0 < vote < 6:
            conform = input("Are you sure(y/n): ")
            if conform.capitalize() == "Y":
                print("You vote", vote, "stars")
                number_of_people = number_of_people + 1
                total_vote = total_vote + vote
            elif conform.capitalize() == "N":
                print("Returning.......")
            else:
                print("Please conform it right")
        elif vote == -1:
            print("Quitting..........")
            break
        else:
            print("Please vote right")
    except ValueError:
        print("Please vote right")

print()
print("======================================")
if number_of_people > 0:
    average_vote = total_vote/number_of_people
print("Number of people who vote:", number_of_people)
print("The average voting are:", average_vote)


