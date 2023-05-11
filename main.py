def main():

    # Student's information: ID, Name, GradeLevel, Zip
    student_list = [[1001, 'Bill', 'Senior', 94568],
                    [1002, 'Kurt', 'Junior', 94598],
                    [1003, 'Kim', 'Senior', 94598]]

    for value in zip(*student_list):
        print(value)

    IDlist, Namelist, Glist, Zlist = zip(*student_list)
    return IDlist, Zlist, Glist, Zlist

    #########################################


if __name__ == '__main__':
    main()
