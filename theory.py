# 일급함수 -> 함수도 변수에 할당하여 사용할 수 있다. -> 함수의 인자로 전달되기도 하고, 함수의 리턴 값이 되기도 한다.
# 고위함수 -> 함수를 인자로 받거나, 함수를 리턴하는 함수
# 데코레이터 -> 함수를 포괄해준다.
# 데코레이터는 가장 아래의 데코레이터부터 실행된다.
# 이터레이터 -> 반복자를 의미한다.
# 매직 메소드 ?
# 제너레이터 -> 발생자를 의미한다. / 함수의 형태인 이터레이터이다.
# 코루틴 -> 제너레이터의 또 다른 형태
# 제너레이터는 함수를 실행하면서 yield 키워드를 통해 값을 하나씩 순서대로 반환하는 이터레이터 역할을 한다.
# 코루틴은 반대로 값을 외부에서 하나씩 받아서 함수를 실행한다.
# 일반적인 함수: 동기적으로 작동 -> 동기적이란, 해당 함수가 실행이 끝날때까지 다른 일을 하지 않는 것
import time
import asyncio


async def foo():
    res = 0

    for i in range(1, 10):
        res += i
        print(res)
        await asyncio.sleep(1)

    return res


start = time.time()

asyncio.run(asyncio.wait([foo(), foo()]))

end = time.time()

over_time = round(end - start, 3)
print(f"걸린 시간 : {over_time}")
