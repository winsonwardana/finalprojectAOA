import mysql.connector
from mysql.connector import Error
from beautifultable import BeautifulTable

table = BeautifulTable()
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='finalproject',
                                         user='root',
                                         password='')
except Error as e:
    print("Error reading data from MySQL table", e)


table.column_headers = ["Fullname","Date of Birth","Gender","Address","Contact","Age","Parent's name"]


name = []
age = []

def show():
    global table
    global name
    global age
    sql_select_Query = "select * from customer"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for row in records:
        name.append(row[1])
        age.append([int(row[6]),row[0]])
        table.append_row([row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
    print(table)
    table.clear()

def getNameById(arr,id):
    sql_select_Query = "select * from customer where id = {}".format(id)
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for row in records:
        arr.append([row[1],row[0]])


def binarySearch(L, target):
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start + end)// 2
        midpoint = L[middle][0]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return middle

# def mergeSort(arr):
#     if len(arr) >1:
#         mid = len(arr)//2 #Finding the mid of the array
#         L = arr[:mid] # Dividing the array elements
#         R = arr[mid:] # into 2 halves
#
#         mergeSort(L) # Sorting the first half
#         mergeSort(R) # Sorting the second half
#
#         i = j = k = 0
#
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i][0] < R[j][0]:
#                 arr[k] = L[i]
#                 i+=1
#             else:
#                 arr[k] = R[j]
#                 j+=1
#             k+=1
#
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i+=1
#             k+=1
#
#         while j < len(R):
#             arr[k] = R[j]
#             j+=1
#             k+=1

def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

# def insertionSort2D(arr):
#
#     # Traverse through 1 to len(arr)
#     for i in range(1, len(arr)):
#
#         key = arr[i][0]
#
#         j = i-1
#         while j >= 0 and key < arr[j][0] :
#                 arr[j + 1][0] = arr[j][0]
#                 j -= 1
#         arr[j + 1][0] = key


# def mergeSort2(arr):
#     if len(arr) >1:
#         mid = len(arr)//2 #Finding the mid of the array
#         L = arr[:mid] # Dividing the array elements
#         R = arr[mid:] # into 2 halves
#
#         mergeSort(L) # Sorting the first half
#         mergeSort(R) # Sorting the second half
#
#         i = j = k = 0
#
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i+=1
#             else:
#                 arr[k] = R[j]
#                 j+=1
#             k+=1
#
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i+=1
#             k+=1
#
#         while j < len(R):
#             arr[k] = R[j]
#             j+=1
#             k+=1
#

def printSortedName():
    insertionSort(name)

    for i in range(len(name)):
        sql_select_Query = "select * from customer where name = '{}' ".format(name[i])
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            table.append_row([row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
    print("")
    print(table)
    table.clear()


def printSortedAge():
    insertionSort(age)

    for i in range(len(age)):
        sql_select_Query = "select * from customer where id = '{}' ".format(age[i][1])
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            table.append_row([row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
    print("")
    print(table)
    table.clear()
    age.clear()
        #     # print("Id = ", row[0], )
        #     # print("Name = ", row[1])
        #     # print("Age  = ", row[6], "\n")

def searchName(x):
    p = 0
    unsorted=[]
    temp=[]
    sql_select_Query = "select * from customer"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for row in records:
        unsorted.append([row[1],row[0]])
    found = []
    temp = []
    insertionSort(unsorted)
    for name in unsorted:
        if(len(name[0]) >= len(x)):
            test = ''
            z = name[0]
            for i in range(len(x)):
                test+=z[i]
            found.append([test,name[1]])


    masihAda = True
    while masihAda:
        result = binarySearch(found, x)
        if result != None:
            temp.append(found[result])
            del found[result]
            p = 1
        else:
            masihAda = False
    fullName = []
    for i in range (len(temp)):
        getNameById(fullName,temp[i][1])
    temp=[]


    for name in fullName:
        if(len(x) < len(name[0])):
            temp.append([name[0][len(x)],name[1]])
        elif(len(x) == len(name[0])):
            temp.append([" ",name[1]])


    insertionSort(temp)
    fullName = []
    for i in range (len(temp)):
        getNameById(fullName,temp[i][1])
    for name in fullName:
        sql_select_Query = "select * from customer where id = '{}' ".format(name[1])
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            table.append_row([row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
    print(table)
    table.clear()
    return p





while True :

    print("")
    print("MONTESORRY CMS DATABASE")
    print("")
    print("1. SHOW")
    print("2. SEARCH")
    print("3. EXIT")
    choice = int(input("Enter Choice : "))

    if(choice == 1):
        show()

        print("Sort By ? : ")
        print("1. Name")
        print("2. Age")
        choice =int(input("Enter Choice : "))
        if(choice == 1):
            printSortedName()
        elif(choice == 2):
            printSortedAge()

    elif(choice == 2):
        search = input("Enter Name : ")
        if(searchName(search) == 0):
            print("no data found")



    elif(choice == 3):
        print("Exiting...")
        exit()
    else:
        print("wrong input")
