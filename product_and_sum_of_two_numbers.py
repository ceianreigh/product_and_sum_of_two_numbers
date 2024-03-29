# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# pseudocode


# compute product of two numbers
def multiply_and_sum(num_1, num_2):
    product = num_1 * num_2

    # if product of two numbers is less than or equal to 1000, return product
    if product <= 1000:
        return (
            "The product of the two numbers is equal or lower than 1000. The product is "
            + str(product)
            + "."
        )
    # if product is greater than 1000, compute sum of two numbers
    else:
        sum = num_1 + num_2
        return (
            "The product of the two numbers is greater than 1000. The sum is "
            + str(sum)
            + "."
        )


# ask user for two numbers
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
result = multiply_and_sum(num_1, num_2)
print(result)
