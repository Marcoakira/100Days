# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. ๐ฒ
import random
# ๐จ Don't change the code below ๐
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# ๐จ Don't change the code above ๐ It's only for testing your code.

# Write the rest of your code below this line ๐

print(test_seed)

head_tails = test_seed
if head_tails % 2 == 0:
    print('cabeรงa')
else:
    print('calda')