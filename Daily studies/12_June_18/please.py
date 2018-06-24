I.	General knowledge
1.	dir: List các file trong folder
2.	Dấu “=”: Assign giá trị
“==”: Bolean function
“!=”: Different
3.	Parse = convert
4.	for i in range(start, stop, step):
start: default = 0; stop: default = n -1; step: default = 1
i: loop counter
5.	length += 5 (length = length + 5)
6.	Lưu thông tin: Lưu biến
7.	Lowercase: lower()
8.	Uppercase: upper()
9.	Shuffle
10.	 Hàm randint và choice
from random import randint
random_number = randint(0, 100)

from random import choice
random_item = choice(list)

II.	Các lệnh trong List
1.	Delete
remove
del list[i]
pop

2.	Break: phá vỡ vòng lặp gần nhất. Nếu dùng biến để dừng vòng lặp thì dừng ở lần tiếp theo

3.	Đầu list: 0
Cuối list: -1

4.	Lặp từ chỗ nào  cho vào vòng lặp từ chỗ đấy

5.	Kiểm tra list rỗng hay không: len(list) == 0

6.	Create list
List = [ , , , ]

7.	Print
Print(*list)

8.	Check length of list
len(list)

9.	Check value trong list
List[i] = …

10.	Print list
	for i in range(5):
	    print(i + 1, ".", list[i], sep = " ")
	
	for i in range(5):
	    print("{0}. {1}".format(i + 1, list[i]))

	for index, item in enumerate(list):
	    print("{0}. {1}".format(i + 1, item))

	for item in list:
	    print(item)

11.	 Update list
Replace:
list[i] = replace_item

Add:
List.append(content)

Check position:
Position = list.index(“value”)

12.	Tách phần tử trong string
list(string)

13.	Tách list by space
list.strip().split(sep = " ")

14.	List có thể chứa integer, string, các loại khác. Chỉ nên lưu dữ liệu cùng loại, không nên lưu dữ liệu loại khác

III.	Các lệnh trong dictionary
Dictionary: 1 cặp key và value; ngăn cách nhau bởi dấu “,”
Phần tử trong dictionary có thể coi như 1 biến

1.	Khai báo dictionary
dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}

2.	Kiểm tra phần tử có trong list hay không:
if item in list:

3.	Thêm mới vào dictionary:
dictionary[key] = value

Update trong dictionary:
dictionary[key] = new_value

Thêm mới khác với update: có key mới

4.	Đặt biến theo value trong dictionary
variable = dictionary[key]

5.	Print 
print(dictionary)

6.	Delete
del dictionary[key]

7.	Kiểm tra phần tử có trong dictionary không
if key in dictionary:
   print("key")
else:
   print("not found")

8.	Print item in list
for k in dictionary:
    print(k, dictionary[k])

for key, value in dictionary.items():
    print(key, value)

for value in dictionary.values():
    print(value)

9.	Print cách 1 line: bấm enter để tiếp tục
print()

***************************

Example 1. Check whether a number is a prime number
number = int(input("Please input number"))
is_prime = True

# Process
for i in range(2,number):
    if number % i == 0 :
        is_prime = False
        break

# Output
if is_prime == True:
    print("{0} is a prime number".format(number))
else:
    print("{0} is not a prime number".format(number))

Example 2. Check whether a list is sorted or not. If sorted, print “sorted”. If not, sort the list
enter_list = input("Please enter your list, separated by space")
new_list = enter_list.strip().split(sep=" ")

# list ko ro sort chua
numbers =[]
# final list
sorted_list = []

length = len(new_list)

# chuyen list sang int
for item in new_list:
    numbers.append(int(item))

# Solution
print(numbers)
is_sorted = True
for i in range(len(numbers)-1):
    if numbers[i] > numbers[i+1]:
        is_sorted = False
        break

if is_sorted:
    print("Your sequence is sorted")
else:
    print("Your sequence is not sorted")
    print()
    for j in range(0,len(numbers)):
        min_number = min(numbers)
        position = numbers.index(min_number)
        del numbers[position]
        sorted_list.append(min_number)
        
    print("After sorted: ",sorted_list)

Example 3. Login 3 times
# Solution
print("Hi there is a superuser gateway")
count = 0

while True:
    user_name = input("Username")
    if user_name == "c4e":
        password = input("Password: ")
        if password == "codethechange":
            print("welcome")
            break
        else:
            print("password incorrect")
    else:
        print("You are not a superuser")     
count += 1
    if count == 3:
        print("You failed to login 3 times, go away")
        break   

Example 4. Control the while loop
Count = 0
Loop = True

while loop:
    if count >= 7:
        loop = False
    else:
        Run the program
    count += 1

while loop:
    print("Running")
    count += 1
    if count ==5:
        loop = False

Example 5.
n = int(input("Please input the number"))
for i in range(n):
    print(n - i)

Example 6.
for i in range(3):
    for j in range(5):
        print("* ", end =" ")
    print()


