# davaleba 1
def usg_find(number_one, number_two):
    biggest_number = 0  # უდიდესი რიცხვი,გამოვიყენებ ვაილ ციკლში
    if number_one > number_two:
        biggest_number = number_one
    elif number_one < number_two:
        biggest_number = number_two

    i = 1
    usg = 1  # უდიდესი საერთო გამყოფი
    while i < biggest_number:
        if number_one % i == 0 and number_two % i == 0:
            usg = i
        i += 1

    if number_one == number_two:  # თუ ორივე რიცხვი ტოლია,უსგ თავად რიცხვები არიან
        usg = number_two

    return usg


x = int(input('enter int: '))
y = int(input('enter int: '))
print(usg_find(x, y))

'''


'''
# დავალება 2

dict = {5: {6: 3}, "hi": {18: 12}, "no": {100: "go"}, 50: {2: 20}}


def dictionary(dict):
    max_value = 0  # მაქსიმალური ველუ
    for value in dict.values():
        try:
            for value in value.values():  # რადგან ველუებად გვაქვს დიქტი, ველუებიდან ცალკე ველუ ამოვიღე
                max_value += value

        except:
            TypeError
            pass

    dict["max"] = max_value
    return dict


print(dictionary(dict))
'''



'''
# დავალება 3
tuple = ((20, 'hi'), (40, 'like'), (60, 'lock'), (80, 'look'))


def tuple_return(tuple):
    numbers = ()  # თუფლი რიცხვებისთვის
    i = 0
    while i < len(tuple):
        if tuple[i][1][0] == 'l':
            numbers += (tuple[i][0],)  # ვინახავ რიცხვებს თუფლში
        i += 1

    max_number = max(numbers)  # მაქსიმალური რიცხვი
    min_number = min(numbers)  # მინიმალური რიცხვი
    usg = 0  # უდიდესი საერთო გამყოფი
    for i in range(1, max_number):
        if max_number % i == 0 and min_number % i == 0:
            usg = i

    return usg, numbers


print(tuple_return(tuple))
