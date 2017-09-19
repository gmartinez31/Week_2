import json
ephoneb = "Electronic Phone Book"
dashes = "====================="
look = "1. Look up an entry"
setting = "2. Set an entry"
delete = "3. Delete an entry"
listall = "4. List all entries"
quit = "5. Quit"
save = "6. Save(Always be sure to save before exiting this program.)"
print(ephoneb)
print(dashes)
print(look)
print(setting)
print(delete)
print(listall)
print(quit)
print(save)

phonebook = {
    'Gustavo': "911",
    'Sergu': '311'
}
initialquestion = input("What would you like to do (1-6s)?")
if int(initialquestion) == 1:
    name = raw_input("Name? ")
    if name in phonebook:
        print(phonebook[name])
elif int(initialquestion) == 2:
    newname = raw_input("Name? ")
    phonenum = raw_input("Phone Number? ")
    phonebook[newname] = [phonenum]
    print(phonebook)
elif int(initialquestion) == 3:
    delname = raw_input("Who do you want to delete? ")
    if delname in phonebook:
        del phonebook[delname]
    print phonebook
elif int(initialquestion) == 4:
    print phonebook
elif int(initialquestion) == 6:
    with open('database4phonebook.json', 'w') as file_handle:
        json.dump(phonebook, file_handle)
else:
    quit
