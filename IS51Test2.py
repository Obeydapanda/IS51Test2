"""


main():
    infile = open("numbers.txt", "r")
    grades = [word.strip() for word in infile]
    infile.close()
    calculate_average()
    calculate_percent_above_average(grades)

    print ("Number of Grades:", len(grades))
    print ("Average Grade:", calculate_average(grades))
    print ("Percentage of grades above average:", calculate_percent_above_average(grades), "%")
    

calculate_percent_above_average(grades):
    avg = calculate_average(grades)
    counter = 0
    for grade in grades:
        if grade > avg:
            counter += 1


    return (counter/len(grades))


    

calculate_average(grades)
    if len(grades) == 0:
        return 0
    
    avg = sum(grades)/len(grades)
    
    return avg



main()

"""

"""


"""