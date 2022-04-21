
def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")    # end assignment
    try:
        open_file = open(file_name)
    except:
        print("File name not found")

    week = dict()
    for line in open_file:
        line_split = line.split()
        
        if len(line_split) < 3 or line_split[0] != 'From':
            continue
        else:
            if line_split[2] not in week:
                week[line_split[2]] = 1
            else:
                week[line_split[2]] += 1
            
    print(week)
## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##countDayOfTheWeek()