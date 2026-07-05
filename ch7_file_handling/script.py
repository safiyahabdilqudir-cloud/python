import os
# os.mkdir("my folder")
# os.removedirs("my folder")
folder_name = "friends_data"


if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print("folder created")
else:
    print("folder already exists")  
    
friend = ["Alice", "Bob", "Charlie", "David"]
file_path = os.path.join(folder_name, "friends.txt")        
# print(file_path)

# with open(file_path, "w") as file:
#     for name in friend:
#         file.write(name + "\n")

# print("All the friends have been written to the " + file_path + " file."    )

# print("\n--- Read Line By Line ---")
# with open(file_path, "r") as file:
#     for line in file:
#         print(line.strip())

new_friends = ["Frank", "Grace"]

with open(file_path, "a") as file:
    for friend in new_friends:
        file.write(friend + "\n")

print("\nNew friends added.")
