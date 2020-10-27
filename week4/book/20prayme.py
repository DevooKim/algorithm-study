class Solution:
    def isValid(self, s: str) -> bool:
        # stack = 후입 선출
        # ASCII TABLE
        # ( = 40, ) = 41
        # [ = 91, ] = 93
        # { = 123, } = 125

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
            elif small + medium + large > 1:
                return False
        return True


for i in ["()", "()[]{}", "(]", "([)]", "{[]}"]:
    print(Solution().isValid(i))