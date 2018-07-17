the_string = input("Enter a long string? ")
result = the_string.split(" ")
backwards_result = result[::-1]
reverse = " ".join(backwards_result)
print(reverse)