import sys
sys.stdin = open('solution_input.txt')

# 들여쓰기 단위 = 2
INDENTATION = 2

T = int(input())

for _ in range(T):
    # 첫 번째 입력은 데이터의 길이가 주어지고,
    length = int(input())
    # 그 다음 줄에 데이터가 문자열로 주어진다.
    data = input().rstrip()

    # 괄호 검증을 할 스택을 준비한다.
    stack = []
    # 결과로 출력할 올바른 Json 문자열
    result = ""
    # 주어진 data를 순회하기 위한 인덱스 변수
    idx = 0
    # 들여쓰기 깊이
    depth = 0

    # 모든 데이터를 순회한다.
    while idx < length:
        # 여는 괄호일 때
        if data[idx] == '{' or data[idx] == '[':
            # 괄호를 스택에 넣고 들여쓰기 깊이를 증가시킨다.
            stack.append(data[idx])
            depth += 1
            # 괄호를 결과에 넣고 줄 바꾼 뒤, 들여쓰기한다.
            result += data[idx] + '\n' + ' ' * depth * INDENTATION
        # 닫는 괄호일 때
        elif data[idx] == '}' or data[idx] == ']':
            # 괄호 쌍이 맞지 않지 않다면 반복문을 종료한다.
            if stack[-1] == '{' and not data[idx] == '}' \
                    or stack[-1] == '[' and not data[idx] == ']':
                break
            # 괄호 쌍이 맞다면 스택에서 괄호 하나를 빼고 들여쓰기 깊이를 감소시킨다.
            stack.pop()
            depth -= 1
            # 줄바꾸고 들여쓰기한 뒤 괄호를 결과에 넣는다.
            result += '\n' + ' ' * depth * INDENTATION + data[idx]
        # 쉼표일 때
        elif data[idx] == ',':
            # 쉼표를 결과에 넣고 줄 바꾼 뒤, 들여쓰기한다.
            result += data[idx] + '\n' + ' ' * depth * INDENTATION
        # 콜론일 때
        elif data[idx] == ':':
            # 콜론을 결과에 넣고 띄어쓰기한다.
            result += data[idx] + ' '
        # 그 외의 경우에는 그냥 해당 문자열만 결과에 넣는다.
        else:
            result += data[idx]
        # 인덱스를 증가하여 다음 데이터를 확인한다.
        idx += 1
    # 스택에 값이 남아있다면 잘못된 데이터이다.

    if stack:
        print('Wrong Data')
    # 그 외의 경우에는 결과를 출력한다.
    else:
        print(result)
