filenames = ["1poem.txt", "donkey.txt", "3.txt"]
for items in filenames:
    try :
        with open (items) as f :
            content = f.read()
        print(f'''Content of {items} is as follow:-
        {content}\n''')
    except (FileNotFoundError, FileExistsError):
           print(f"This File {items}is not available which you want to read")
    
print("Thank you for using our file reader")