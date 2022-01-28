# s "[]()"
from collections import deque


def is_valid(s):
    pair = {
        '}':'{',
        ')': '(',
        ']': '['
    }
    opener = "{[("
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)
        else:
            if not stack:
                return False

            top = stack.pop()
            if pair[char] != top:
                return False

    return not stack



def get_card(num):
    """
    1. 제일 위 카드를 버린다.
    2. 그 다음 카드를 뒤로 옮긴다.
    3. 한 장 남은 카드를 반환한다.
    """
    queue = deque([n for n in range(1, num+1)])
    while len(queue) > 1:
        # 1
        queue.popleft()
        # 2
        queue.append(queue.popleft())
    #3
    return queue.popleft()




assert is_valid("{}[]()")
assert is_valid("{[]}")
assert is_valid("({[]})")

assert not is_valid("{{{}")



assert get_card(6) == 4

# (익명)14번 else 에서 char가 pair일 때는 append 해주지 않아도 되는건가요???