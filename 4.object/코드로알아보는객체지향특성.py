"""객체지향특성
    참고자료: https://yansfil.github.io/awesome-class-materials/3.object-oriented/5.%20%EC%BD%94%EB%93%9C%EB%A1%9C%20%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94%20%EA%B0%9D%EC%B2%B4%20%EC%A7%80%ED%96%A5%EC%9D%98%20%ED%8A%B9%EC%84%B1.html
    
    주요내용
    
    객체지향의 특성 4가지:
        1. 상속
        2. 추상화
        3. 다형성
        4. 캡슐화
    
    객체지향의 설계 5원칙 (SOLID)
        1. SRP(Single Responsibility Principle)
            - 하나의 객체는 하나의 책임만 가지도록 설계하는 것이 일반적으로 좋다.
    
    책임주도 설계: 객체들의 인스턴스, 메써드보다 객체들의 책임부터 정의하고 시스템을 설계한다.
"""

# 책임
class User:
    def __init__(self) -> None:
        pass

    def drive(self) -> None:
        pass


class MorningCar:
    def __init__(self) -> None:
        pass

    def accelerate(self) -> None:
        pass

    def decelerate(self) -> None:
        pass


# 협력
class User:
    def __init__(self) -> None:
        self.car = MorningCar()  # User는 MorningCar를 의존하고 있습니다.

    def drive(self) -> None:
        self.car.accelerate()  # User는 MorningCar가 제공하는 공개 메서드를 사용합니다.


class MorningCar:
    def __init__(self):
        self.speed = 0
        self._fuel = 0  # 파이썬 특성상 private을 _ prefix를 붙여 암묵적으로 사용함

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


class PorscheCar:
    def __init__(self):
        self.speed = 0
        self._fuel = 0

    def accelerate(self):
        self.speed += 3

    def decelerate(self):
        self.speed -= 3


# 추상화: 추상화가 없을 때
class User:
    def __init__(self, car_name: str) -> None:
        if car_name == "morning":
            self.car = MorningCar()
        elif car_name == "porsche":
            self.car = PorscheCar()

    def drive(self):
        self.car.accelerate()


print("추상화 미적용")

m = User("morning")
p = User("porsche")

m.drive()
print(f"모닝 속도: {m.car.speed}")
p.drive()
print(f"포르쉐 속도: {p.car.speed}")

# 추상화: 추상화가 있을 때

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def accelerate(self) -> None:
        pass

    @abstractmethod
    def decelerate(self) -> None:
        pass


class MorningCar(Car):
    def __init__(self) -> None:
        self.speed = 0
        self._fuel = 0

    def accelerate(self) -> None:
        self.speed += 1

    def decelerate(self) -> None:
        self.speed -= 1


class PorscheCar(Car):
    def __init__(self) -> None:
        self.speed = 0
        self._fuel = 0

    def accelerate(self) -> None:
        self.speed += 3

    def decelerate(self) -> None:
        self.speed -= 3


class User:
    def __init__(self, car: Car) -> None:  # 클래스를 받는 것을 이런식으로 표현하는 구나, 배우고 간다.
        self.car = car

    def drive(self):
        self.car.accelerate()


print("추상화 적용")

# 모닝 차량을 운전하고 싶을 때
user = User(MorningCar())
user.drive()
print(f"모닝 속도: {user.car.speed}")

# 포르쉐 차량을 운전하고 싶을 때
user = User(PorscheCar())
user.drive()
print(f"포르쉐 속도: {user.car.speed}")
