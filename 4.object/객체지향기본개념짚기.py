"""객체지향의 기본개념 짚기

    주요개념:
        1. 클래스 변수, 인스턴스 변수
            - 클래스 변수: 같은 클래스의 모든 인스턴스가 공유
            - 인서턴스 변수: 인스턴스별로 독립된 메모리 공간을 가짐
        2. 메써드: 공개형, 비공개형으로 나뉨 단 Java 언어처럼 접근제어자로 제약하는 것은 아님
        3. 상속: 클래스의 상속
        4. 인터페이스 / 추상클래스
            - 인터페이스: 클래스의 메써드를 명시

    참고자료: https://www.inflearn.com/course/%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%8B%A4%EB%AC%B4-%EA%B8%B0%EB%B3%B8%EA%B8%B0/lecture/98343?tab=note&volume=0.80&quality=auto&speed=1.5
    참고자료: https://wikidocs.net/16075 (추상클래스)
"""

# 1. 비어있는 클래스
class User:
    pass


user_1 = User()
user_2 = User()

print(user_1 == user_2)

# 2. 인스턴수 변수만 있는 클래스
class User:
    def __init__(self, name: str, job: str) -> None:
        self.name = name
        self.job = job


user_1 = User(name="jjm", job="data_engineer")
user_2 = User(name="other", job="project_manager")
print(user_1.name, user_1.job)
print(user_2.name, user_1.job)

# 3. 클래스 변수를 추가한 클래스
class User:
    num_users: int = 0

    def __init__(self, name: str, job: str) -> None:
        self.name = name
        self.job = job
        User.num_users += 1


user_1 = User(name="jjm", job="data_engineer")
user_2 = User(name="other", job="project_manager")
print(user_1.name, user_1.job)
print(user_2.name, user_1.job)
print(User.num_users)

# 4. 공개형 메써드를 추가한 클래스
class User:
    def __init__(self, name: str, job: str) -> None:
        self.name = name
        self.job = job

    def work(self) -> None:
        if self.job == "data_engineer":
            print("데이터 엔지니어링 관련된 일을 합니다.")
        elif self.job == "project_manager":
            print("프로젝트 매니징 관련된 일을 합니다.")


user_1 = User(name="jjm", job="data_engineer")
user_2 = User(name="other", job="project_manager")
print(user_1.name, user_1.job)
user_1.work()
print(user_2.name, user_2.job)
user_2.work()

# 5. 비공개형 메써드
class User:
    def __init__(self, name: str, job: str) -> None:
        self.name = name
        self.job = job

    def work(self) -> None:
        work_type = self._get_work_type()
        print(f"{work_type} 관련된 일을 합니다.")

    def _get_work_type(self) -> str:
        if self.job == "data_engineer":
            return "데이터 엔지니어링"
        elif self.job == "project_manager":
            return "프로젝트 매니징"


print("비공개형 메써드, 접근제어자 문법은 아니지만 메써드 앞에 언더스코어(_)를 붙임으로써 명시함")
user_1 = User(name="jjm", job="data_engineer")
user_1.work()
user_2 = User(name="other", job="project_manager")
user_2.work()

# 6. 상속
class Job:
    def do(self) -> None:
        print(f"{self.work_type} 관련된 일을 합니다.")


class DataEnginner(Job):
    work_type = "데이터 엔지니어링"


class ProjectManager(Job):
    work_type = "프로젝트 매니징"


print("상속 예시")

data_enginner = DataEnginner()
data_enginner.do()
print(data_enginner.work_type)

# 7. 인터페이스, 파이썬에는 인터페이스가 별도로 없어 추상클래스로 구현
# 추가자료: https://wikidocs.net/16075
from abc import ABC, abstractmethod


class Job(ABC):
    @abstractmethod
    def do(self) -> None:
        pass


class DataEngineer(Job):
    def do(self) -> None:
        print("데이터 엔지니어링 관련된 일을 합니다.")


class ProjectManager(Job):
    def do(self) -> None:
        print("프로젝트 매니징 관련된 일을 합니다.")


print("7. 추상클래스")
data_enginner = DataEngineer()
data_enginner.do()
