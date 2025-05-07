#https://leetcode.com/problems/plus-one/description/
# sei da solucao de ''.join, quero tentar a "tecnica" antes.
# acabou sendo que a de ''.join era pior
# se pá eu que otimizei d mais a outra


digits = [1,2,3]

# nums = ''.join(str(x) for x in digits)
# nums = int(nums)
# nums += 1
# out = []
# for num in str(nums):
#     out.append(int(num))
# print(out)


digits = digits[::-1]
if digits == [9]:
    print([1,0])
else:
    digits[0] += 1
    if digits[0] < 10:
        print(digits[::-1])
    else:
        digits[0] = 0
        digits[1] += 1
        for i in range(1, len(digits)-1):
            if digits[i] >= 10:
                digits[i] = 0
                digits[i+1] += 1
            pass
        if digits[len(digits)-1] == 10:
            digits[len(digits)-1] = 0
            digits.append(1)
    print(digits[::-1])