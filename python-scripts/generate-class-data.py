import random
import sys
import pandas as pd


def GenerateData(number_of_students=200):
    
    if sys.argv[1] is not None:
        number_of_students = int(sys.argv[1])

    class_df = pd.DataFrame(columns=["Class", "Score", "Pass/Fail"])
    class_options = [1, 2, 3]
    class_list = []
    score_list = []
    while number_of_students > 0:
        class_choice = random.choice(class_options)
        score = random.randint(45, 100)
        class_list.append(class_choice)
        score_list.append(score)
        number_of_students -= 1

    class_df["Class"] = class_list
    class_df["Score"] = score_list

    return class_df

if __name__ == "__main__":
    csv_to_save = GenerateData()
    csv_to_save.to_csv("../data/ClassScores.csv", index=False)