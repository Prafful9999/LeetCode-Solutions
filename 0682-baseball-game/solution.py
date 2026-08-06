class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i.lstrip('-').isdigit():
                stack.append(int(i))  # ← Convert to int before storing

            elif i == "+":
                if len(stack) < 2:
                    print("Not possible")
                else:
                    stack.append(stack[-1] + stack[-2])

            elif i == "D":
                if len(stack) == 0:
                    print("score is empty")
                else:
                    stack.append(stack[-1] * 2)

            else:  # "C"
                if len(stack) == 0:
                    print("score is empty")
                else:
                    stack.pop()

        return sum(stack)
