

def filter_users_by_age_and_country(users, age_limit, countries):
    filtered_names = [user[1] for user in users if user[2] > age_limit and user[3] in countries]
    return filtered_names

def get_top_oldest_users(users, top_n=10):
    sorted_users = sorted(users, key=lambda x: x[2], reverse=True)
    return sorted_users[:top_n]

def find_duplicate_names(users):
    name_counts = {}
    duplicates = []
    for user in users:
        name = user[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
    
    for name, count in name_counts.items():
        if count > 1:
            duplicates.append(name)
    return duplicates

users_data = [
    (1, "Alice", 25, "USA"),
    (2, "Bob", 35, "Canada"),
    (3, "Charlie", 40, "USA"),
    (4, "David", 32, "Canada"),
    (5, "Eva", 28, "Germany"),
    (6, "Frank", 45, "USA"),
    (7, "Grace", 36, "Canada"),
    (8, "Alice", 42, "Mexico"),
    (9, "Henry", 29, "Canada"),
    (10, "Isaac", 50, "USA"),
]

filtered_names = filter_users_by_age_and_country(users_data, 30, ["USA", "Canada"])
print("Filtered names (age > 30 from USA/Canada):", filtered_names)

top_10_oldest_users = get_top_oldest_users(users_data)
print("Top 10 oldest users:", top_10_oldest_users)

duplicate_names = find_duplicate_names(users_data)
if duplicate_names:
    print("Duplicate names found:", duplicate_names)
else:
    print("No duplicate names found.")
