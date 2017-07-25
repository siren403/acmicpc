'''
입력받은 문자를 출력하는 문제1
'''

while True:
    try:
        print(input())
    except EOFError:
        break;