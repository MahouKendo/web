candidates_list = ["Steve", "Obama", "Conan", "Henry", "God"]
votes_list = [0, 0, 0, 0, 0]

def main():
    while all(i < 5 for i in votes_list):
        time = -1
        print("=====================Ranking board=======================")
        for i, j in zip(candidates_list, votes_list):
            print(i, j)
        votes = input("Pick the candidate that you want to vote for: ")
        for i, j in zip(candidates_list, votes_list):
            time = time + 1
            if votes.capitalize() == i:
                print("You have vote for", i)
                vote = j + 1
                votes_list[time] = vote
        for i, j in zip(range(len(candidates_list)), range(len(votes_list))):
            for l, k in zip(range(i + 1, len(candidates_list)), range(j + 1, len(votes_list))):
                if votes_list[j] < votes_list[k]:
                    candidates_list[i], candidates_list[l] = candidates_list[l], candidates_list[i]
                    votes_list[j], votes_list[k] = votes_list[k], votes_list[j]
        return main()
    print("=============Vote end===================")
    for i, j in zip(candidates_list, votes_list):
        if j == 5:
            print("The winner is:", i)



main()



