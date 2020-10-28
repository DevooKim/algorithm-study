class Solution:
    def isValid(self, s: str) -> bool:
        # stack = 후입 선출
        # ASCII TABLE
        # ( = 40, ) = 41
        # [ = 91, ] = 93
        # { = 123, } = 125
        # 우선순위를 알아야한다.

        small, medium, large = 0, 0, 0
        for i in s:
            if i == '(':
                small += 1
            elif i == ')':
                small -= 1
            elif i == '[':
                medium += 1
            elif i == ']':
                medium -= 1
            elif i == '{':
                large += 1
            elif i == '}':
                large -= 1

            if small < 0 or medium < 0 or large < 0:
                return False

        return True


    def book(self, s: str) -> bool:
        stack = []
        table = {
            ')':'(',
            '}':'{',
            ']':'[',
        }

        for char in s:
            if char not in table: # table.keys()에 없으면 즉, 여는 괄호일 떄
                stack.append(char) # stack에 추가
            elif not stack or table[char] != stack.pop(): # stack이 비어있지 않거나 닫힌 괄호가 없으면..
                return False
        return len(stack) == 0

for i in ["()", "()[]{}", "(]", "([)]", "{[]}"]:
    print(Solution().isValid(i))
    # print(Solution().book(i))