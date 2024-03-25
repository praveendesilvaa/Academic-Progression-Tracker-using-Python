# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221895
# Date: 2023.04.20
# UOW ID: W1985643
# Name: Praveen de Silva

# variables
progress = []
trailer = []
retriever = []
exclude = []
student_list = []
student_credits = []
pass_credits = 0
defer_credits = 0
fail_credits = 0
dict = {}
multiple_inputs = True
rangelist = [0, 20, 40, 60, 80, 100, 120]


while multiple_inputs == True:
    while True:
        student_ID = input("Enter your student ID ")
        if student_ID[0] != "w" or len(student_ID) != 8:
            print("Invalid ID")
        else:
            break
    while True:
        pass_credits = input("please enter pass credits: ")
        if pass_credits.isdigit():
            pass_credits = int(pass_credits)
            if pass_credits in rangelist:
                break
            else:
                print("out of range\n")
        else:
            print("integer required\n")

    while True:
        defer_credits = input("please enter defer credits: ")
        if defer_credits.isdigit():
            defer_credits = int(defer_credits)
            if defer_credits in rangelist:
                break
            else:
                print("out of range\n")
        else:
            print("integer required\n")

    while True:
        fail_credits = (input('Please enter your credits at Fail: '))
        if fail_credits.isdigit():
            fail_credits = int(fail_credits)
            if fail_credits in rangelist:
                break
            else:
                print('Out of range.\n')
        else:
            print('Integer required\n')

    if pass_credits + defer_credits + fail_credits == 120:
        if pass_credits == 120:
            print("progress")
            progress.append(0)
            subject_list = ["Progress - ", pass_credits, ', ', defer_credits, ', ', fail_credits]
        elif pass_credits == 100:
            print("Progress(module trailer)")
            trailer.append(0)
            subject_list = ["Progress(module trailer) - ", pass_credits, ', ', defer_credits, ', ', fail_credits]
        elif fail_credits >= 80:
            print("Exclude")
            exclude.append(0)
            subject_list = ["Exclude - ", pass_credits, ', ', defer_credits, ', ', fail_credits]
        else:
            print("Do not progress - module retriever")
            retriever.append(0)
            subject_list = ["Do not progress - module retriever - ", pass_credits, ',', defer_credits, ',',
                            fail_credits]

        student_list.append(student_ID)
        student_credits = list(subject_list)
        dict[student_ID] = student_credits
    else:
        print("incorrect total\n")
        continue
    # Multiple Outcomes
    while True:
        print("\n")
        multiple_inputs = input(
            "Would you like to enter another set of data?\n Enter 'y' for yes or 'q' to quit and view results: ")
        print("\n")
        if multiple_inputs.lower() == 'y':
            multiple_inputs = True
            break
        elif multiple_inputs.lower() == 'q':
            multiple_inputs = False
            
            #Histogram
            print('-' * 100)
            print('Histogram')
            print('Progress', len(progress), ':', '*' * len(progress))
            print('Trailer', len(trailer), ':', '*' * len(trailer))
            print('Retriever', len(retriever), ':', '*' * len(retriever))
            print('Excluded', len(exclude), ':', '*' * len(exclude))
            print("\n")
            total_outputs = len(progress) + len(trailer) + len(retriever) + len(exclude)
            print(total_outputs, 'outcomes in total.')
            print('-' * 100)

            #Part 4 – Dictionary (separate program)
            print('part 4')
            z = 0
            for z in range(len(student_list)):
                x = str(student_list[z])
                y = dict.get(x)
                print(x, ':', *y)
            break
        else:
            print("Invalid option. Please Enter 'y' or 'q' \n")

# Reference Codes

# https://www.w3schools.com/python/python_dictionaries.asp


