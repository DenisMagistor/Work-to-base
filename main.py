def calculator(expression):
    allowed = '+-/*'

    if not any(sign in expression for sign in allowed):
        raise ValueError('Выражение должно содержать хоть один знак {}'.format(allowed))

    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)

                if sign == '+':
                    return left + right

                if sign == '-':
                    return left - right

                if sign == '*':
                    return left * right
                    
                if sign == '/':
                    return left / right
            
            except (ValueError, TypeError):
                raise ValueError('Выражения должно содержать 2 числа и 1 знак')
            

if __name__ == '__main__':
    print(calculator('2*2'))