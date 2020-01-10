class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_n = str(n)
        product = int(str_n[0])
        sum_of_digit = int(product)
        for index in range(len(str_n)-1):
            if len(str_n) > 1:
                print(product, sum_of_digit)
                product *= int(str_n[index+1])
                sum_of_digit += int(str_n[index+1])
                print(product, type(product))
                print(sum_of_digit, type(sum_of_digit))
            else:
                return 0
        return (product-sum_of_digit)