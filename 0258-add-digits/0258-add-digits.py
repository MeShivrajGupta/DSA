class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            result = 0

            num = str(num)

            for i in range(len(num)):
                result = result + int(num[i])

            num = result

        return num