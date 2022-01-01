"""
    프로그래밍 패러다임 훑고가기 - 함수형 프로그래밍
    링크: https://www.inflearn.com/course/%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%8B%A4%EB%AC%B4-%EA%B8%B0%EB%B3%B8%EA%B8%B0/lecture/98342?tab=note&volume=0.80&quality=auto&speed=1.5
    
    참고자료 1: https://hamait.tistory.com/823
    참고자료 2:
"""

from functools import partial

# Pipelining
def main():
    pipe_func = pipe(read_input_file, parse_input_data, save_data)
    return pipe_func("input_file.txt")


# Partial application
def power(base, exp):  # powering
    return base ** exp


def main():
    square = partial(power, exp=2)
    cube = partial(power, exp=3)
    print(square(2))  # 2의 제곱인 4 반환
    print(cube(2))  # 2의 세제곱인 8 반환


main()
