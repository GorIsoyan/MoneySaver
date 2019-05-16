import json
print("\nWelcome to MoneySaver program")


def student():
    with open("main.json") as data_file:
        activities = json.load(data_file)
    return activities['Student']['activity']


def name():
    user = {}
    user['name'] = str(input("\nPlease enter your name: "))
    user['password'] = str(input("\nPlease enter your password: "))
    user['data'] = []
    with open('data_saver.json', 'w') as file:
        file.write(json.dumps(user))


def set_up_json():
    with open("main.json") as data_file:
        file = json.load(data_file)
        weekdays = file['Student']['weekdays']
        activity = file['Student']['activity']
        money = file['Student']['budget']
        return weekdays, activity, money


def input_weekdays(weekdays):
    data = input("\nPlease enter your weekday: ")
    while True:
        if data in weekdays:
            return data
        else:
            data = input('\nYou have typed something wrong, input it again: ')


def input_activity(activity):
    term = input("\nPlease select one of this activities: ")
    while True:
        if term in activity:
            return term
        else:
            term = input('\nYou have typed something wrong, input it again: ')


def input_money():
    while True:
        data = input("\nPlease enter the amount of money: ")
        temp = data.replace('.', '', 1)
        if temp.isdigit() == True:
            data = float(data)
            return data
        else:
            print("\nSomething went wrong, try again:")


def info_input():
    new_data = {}
    with open("main.json") as data_file:
        file = json.load(data_file)
    weekdays = file['Student']['weekdays']
    activity = file['Student']['activity']
    money = file['Student']['budget']
    for j in activity:
        print(j)
    new_data['activity'] = input_activity(activity)
    for i in weekdays:
        print(i)
    new_data['weekdays'] = input_weekdays(weekdays)
    for a in money:
        print(a)
    new_data['money'] = input_money()
    with open('data_saver.json', 'r') as file:
        data = json.load(file)
        data['data'].append(new_data)
    with open('data_saver.json', 'w') as file:
        file.write(json.dumps(data))


def action():
    actions = int(input('\n1 - press for adding, 2 - press for report, 3 - press for exit: '))
    if actions == 1 or actions == 2:
        return actions
    elif actions == 3:
        print("You have exited")
        return actions
    else:
        print('Something went wrong, try again:')
        action()


def download_input():
    with open("data_saver.json") as data_file:
        new_data = json.load(data_file)
    for key in new_data:
        print(key, "-", new_data[key])


def main():
    while True:
        actions = action()
        if actions == 1:
            studentaccess = student()
            studennamepassword = name()
            setup = set_up_json()
            information = info_input()
        elif actions == 2:
            download_input()
            return actions
        elif actions == 3:
            break


main()

