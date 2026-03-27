#count vowels in a string 
str = "pratibha"
count = 0 
for ch in str:
    if ch in "aeiou":
        count = count+ 1
#to print count
print(count)
