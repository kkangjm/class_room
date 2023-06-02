
def calc_test (a, b, operator='+'):
    result = 0
    if operator == '+' : result = a + b
    elif operator == '-' : result = a - b
    elif operator == '*' : result = a * b
    elif operator == '/' : result = a / b
    elif operator == '**' : result = a ** b
    else : print('ERROR')
    return result

print('결과 = ', calc_test(2, 10, '**'))


# def return_test(a, b):
#     plus = a + b
#     minus = a - b
#     return plus, minus

# print(calc_test(3, 4, '*'))
# print(return_test(5, 4))



# if __name__ == '__main__':
#     print(calc_test(3, 4))
#     print(calc_test(3, 4, '*'))
#     print(return_test(5, 4))
