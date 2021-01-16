def is_armstrong_number(number):
    number_list = list(str(number))
    new_list = []

    for num in number_list:
      new_list.append(int(num)**len(number_list))
    
    return number == sum(new_list)