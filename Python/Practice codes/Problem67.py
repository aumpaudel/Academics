# list = []
# def value_list():
#     while True:
#         try :
#             user_input = input('''Enter Numbers Whose table you need:
#                           (if all numbers written then type d in next number.)
#                           Number:-   ''')
#             if user_input == "d":
#                 print("Your List is ready✅\n \n ")
#                 break
#             else:
#                 list.append(int(user_input))
#         except ValueError:
#             print("❌ Invalid input. Please enter a number or 'd' to finish.")
# value_list()

# def multification(n):
#     for i in range (1, 11):
#         print(f"{n} X {i} = {n*i}")
#     return "Table completed✅\n"

# for items in list:
#     print(f'Table of {items}:-')
#     print(f'{multification(items)}')


n = int(input("Enter the number whose table you need in list:- "))
table = []
for i in range (1, 11):
    d = (f"{n} X {i} = {n*i}")
    table.append(d)

print(table)

with open ("tables.txt" , "a") as f :
    f.write("\n".join(table))