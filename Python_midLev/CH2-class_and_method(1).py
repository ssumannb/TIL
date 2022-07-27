# chaper02-01

# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
# 과거에 규모가 큰 프로젝트는 함수 중심으로 구현되었음 -> 데이터가 방대해짐 -> 복잡해지는 문제
# 클래스 중심으로 코딩 -> 데이터가 중심에 있음 -> 함수의 파라미터 감소 -> 프로그램의 요소가 객체로 관리
# 절차 지향 vs 객체 지향

# 일반적인 코딩
# 동일한 속성, 기능을 하는 요소들을 각각 변수로 정의하여 나열해줌
# 리스트 구조를 사용하여 리스트업 함 
# 요소들이 늘어날수록 관리하기가 힘들어짐

#차량 1
car_companay_1 = "Ferrari"
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

#차량 2
car_companay_2 = "BMW"
car_detail_2 = [
    {'color': 'black'},
    {'horsepower': 300},
    {'price': 5000}
]
# ...

# 리스트 구조
# 인덱스 접근 시 실수 가능성이 있고 삭제가 불편함
car_company_list = ['Ferrari', 'BMW']
car_detail_list = [
    {'color': 'white', 'horsepower': 400, 'price': 8000},
    {'color': 'black', 'horsepower': 300, 'price': 5000}
    # ...
]

del car_company_list[1]
del car_detail_list[1]

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등의 불편함이 있음
car_dicts = [
    {'car_company':'Ferrari', 'car_detail':{'color':'whilte', 'horseposer':400, 'price':8000}},
    {'car_company':'BMW', 'car_detail':{'color': 'black', 'horsepower': 300, 'price': 5000}}
]


# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
    def __init__(self, company, details):
        self._company = company
        self._detail = details

    def __str__(self): # 미리 정의된 일반 메소드 
        # print함수 사용 시 클래스의 속성 정보를 출력해주는 메소드로 구현할 수 있다.
        # 사용자 입장의 출력하는 메소드 (비공식적, user level)
        return 'str : {} - {} '.format(self._company, self._detail)

    def __repr__(self): # 미리 정의된 일반 메소드 
        # 조금 더 엄격한 type 정보를 출력하는 메소드 (developer level)
        return 'repr : {} - {} '.format(self._company, self._detail)


car1 = Car('Ferrari', {'color':'whilte', 'horseposer':400, 'price':8000})
print(car1) # str, repr와 같은 출력 함수가 정의되지 않은 경우 가장 상위 정보인 object에 대한 정보를 출력함
car2 = Car('BMW', {'color': 'black', 'horsepower': 300, 'price': 5000})

# dict이라는 일반 속성 접근
print(car1.__dict__) # namespace (클래스 속성) 정보를 모두 볼 수 있다.

print(dir(car1)) # car1의 모든 meta 정보를 보여줌

# list로 관리

car_list = [Car]
car_list.append(car1)
car_list.append(car2)

# 리스트 안의 객체로 출력할 땐 repr으로 출력
# 리스트 요소를 반복문 내에서 출력할 땐 str으로 출력