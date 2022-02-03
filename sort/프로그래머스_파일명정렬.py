# 파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현하기로 했다.
# 소스 파일 저장소에 저장된 파일명은 100 글자 이내로, 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다.
# 파일명은 영문자로 시작하며, 숫자를 하나 이상 포함하고 있다.

'''
파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬한다.
이때, 문자열 비교 시 대소문자 구분을 하지 않는다. MUZI와 muzi, MuZi는 정렬 시에 같은 순서로 취급된다.
파일명의 HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다.
9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬된다.
숫자 앞의 0은 무시되며, 012와 12는 정렬 시에 같은 같은 값으로 처리된다.
두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다.
MUZI01.zip과 muzi1.png가 입력으로 들어오면, 정렬 후에도 입력 시 주어진 두 파일의 순서가 바뀌어서는 안 된다.
'''
'''
입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
'''
import re

def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''
        number_check = False

        for i in range(len(f)):
            # f[i]가 숫자 일때 number에 요소 넣고 number_check = True
            if f[i].isdigit():
                number += f[i]
                number_check = True
            # number 이전 요소를 head에 넣기
            elif not number_check:
                head += f[i]
            # 그 외(number 이후 요소) tail에 넣기
            else:
                tail += f[i:]
                break

        answer.append((head, number, tail))
    # head를 우선, head가 같을 시에 number를 기준으로 정렬
    answer.sort(key= lambda x:(x[0].upper(), int(x[1])))
    # 공백없이 이어 붙여 출력
    return [''.join(i) for i in answer]
'''

# 정규표현식을 이용한 풀이 1
import re
def solution(files):
    answer = [re.split(r"[0-9]+)", s) for s in files]

    answer.sort(key = lambda x: (x[0].lower(), int(x[1])))

    return [''.join(i) for i in answer]
'''
'''
# 정규표현식을 이용한 풀이 2
import re 
def solution(files): 
    files.sort(key = lambda x: (re.findall('\D+', x)[0].lower(), int(re.findall('\d+', x)[0]))) 
    return files
'''

'''
파이썬 정규 표현식

import re

p = re.compile(r'regExp')

p.match(target, S/I/M).group/start/end()

p.search(target, S/I/M).group/start/end()

p.findall(target, S/I/M)
'''
