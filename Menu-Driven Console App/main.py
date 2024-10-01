
from students import students
from os import system
import menu_funcs as mf

menu_items = "1.Highest Achievers\n2.Average GPA\n3.Student List\n4.Exit\n\nChooseMenu Item: "

choice = input(menu_items)
while choice != "4":
    if choice == "1":
        msg = mf.high_achievers(students)
    elif choice == "2":
        msg = mf.avg_gpa(students)
    elif choice == "3":
        msg = mf.print_list(students)
    elif choice == "4":
        break
    else:
        msg = "Invalid Menu Choice"

    input(f"{msg}\nPress any key to continue")
    system("cls")
    choice = input(menu_items)