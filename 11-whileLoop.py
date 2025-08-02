i = int(input("Enter the number: "))
print(i)
while(i<=38):
  i = int(input("Enter the number: "))
  print(i)

print("Done with the loop")


count = 5
while (count > 0):
  print(count)
  count = count - 1
else:
  print("I am inside else")

# In Python, the else block **after a while loop only executes if the loop was not terminated by a break. That's its actual purpose.

# ✅ So when to use else with while?
# When you want to run something only if the loop completed fully (not broken early).

# Common in search problems, like:

nums = [1, 3, 5, 7]
target = 4
i = 0
while i < len(nums):
    if nums[i] == target:
        print("Found")
        break
    i += 1
else:
    print("Not found")  # runs only if loop didn’t `break`
