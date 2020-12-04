def main():
    infile = open("numbers.txt", "r")
    grades = [int(word.strip()) for word in infile]
    infile.close()
    avg = calculate_average(grades)
    above_average = calculate_percent_above_average(grades) * 100

    print ("Number of Grades:", len(grades))
    print ("Average Grade:", avg, "%")
    print ("Percentage of grades above average:", round(above_average, 2), "%")
    

def calculate_percent_above_average(grades):
    avg = calculate_average(grades)
    counter = 0
    for grade in grades:
        if grade > avg:
            counter += 1


    return (counter/len(grades))


    

def calculate_average(grades):
    if len(grades) == 0:
        return 0

    avg = sum(grades)/len(grades)
    
    return avg



main()