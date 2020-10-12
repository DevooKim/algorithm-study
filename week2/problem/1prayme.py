# 3진법 뒤집기
class Solution:
    def re(self, n: int) -> int:
        # 예외처리
        if n < 3:
            return n
        elif n == 3:
            return 1

        answer = 0
        ternary = ""
        while n >= 3:
            ternary = str(n % 3) + ternary
            n = n // 3

        ternary = str(n) + ternary

        print(f'demical: {n} | ternary: {answer}')

        for i in range(len(ternary)):
            print(f'step: {i} | ternary[i]: {ternary[i]} | ternary[i] ** i: {int(ternary[i]) ** i} | answer: {answer}')
            answer += int(ternary[i]) * 3 ** i

        print(f"answer: {answer}")
        return answer


Solution().re(45)
