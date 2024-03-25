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
subject_list = []
main_list = []
pass_credits = 0
defer_credits = 0
fail_credits = 0
multiple_inputs = True
rangelist = [0, 20, 40, 60, 80, 100, 120]


# user defined functions
def Histogram(progress, trailer, retriever, exclude):
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


def student_file():
    print('')
    print('-' * 100)
    print("Part 3:")
    text_file = open("Credit.txt", 'w')
    for x in range(len(main_list)):
        for y in range(len(main_list[x])):
            str_list = str(main_list[x][y])
            text_file.write(str_list)
        text_file.write('\n')
    text_file.close()
    text_file = open("Credit.txt")
    file_content = text_file.read()
    print(file_content)
    text_file.close()


while multiple_inputs == True:
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
            subject_list = ["Progress - ", pass_credits,', ', defer_credits,', ', fail_credits]
        elif pass_credits == 100:
            print("Progress(module trailer)")
            trailer.append(0)
            subject_list = ["Progress(module trailer) - ", pass_credits,', ', defer_credits,', ', fail_credits]
        elif fail_credits >= 80:
            print("Exclude")
            exclude.append(0)
            subject_list = ["Exclude - ", pass_credits,', ', defer_credits, ', ', fail_credits]
        else:
            print("Do not progress - module retriever")
            retriever.append(0)
            subject_list = ["Do not progress - module retriever - ", pass_credits,', ', defer_credits,', ',
                            fail_credits]
        subject_list = list(subject_list)
        main_list.append(subject_list)

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
            

            # Histrogram
            Histogram(progress, trailer, retriever, exclude)

            # Part 2 – List (extension)
            print("Part 2:")
            for i in range(len(main_list)):
                print(*main_list[i])

            # Part 3 - Text File (extension)
            student_file()
            break

        else:
            print("Invalid option. Please Enter 'y' or 'q' \n")

# Reference Codes
# https://www.w3schools.com/python/ref_string_isdigit.asp
# https://www.w3schools.com/python/python_file_handling.asp

