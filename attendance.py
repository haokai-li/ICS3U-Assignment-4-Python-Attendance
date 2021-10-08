#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program check about student's attendance


def main():
    # This function check about student's attendance

    # input
    classes_held_string = input("Number of your classes held: ")
    classes_attended_string = input("Number of your classes attended: ")
    print("")

    # process
    try:
        classes_held_number = int(classes_held_string)
        classes_attended_number = int(classes_attended_string)
        answer_number = classes_attended_number / classes_held_number
        # output
        print("attendance = {}".format(answer_number))
        print("")
        if answer_number >= 0.75:
            print("OK, you will be allowed to sit in the exam.")
        else:
            print(
                "Your attendance is less than 75%, you will not be allowed to sit in the exam"
            )

    except Exception:
        # output
        print("You didn't enter an integer.")
        print("")

    print("\nDone.")


if __name__ == "__main__":
    main()
