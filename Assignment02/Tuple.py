

def count_unique_users(transactions):
    unique_users = {transaction[1] for transaction in transactions}  
    return len(unique_users)


def find_transaction_with_highest_amount(transactions):
    return max(transactions, key=lambda x: x[2]) 


def extract_transaction_and_user_ids(transactions):
    transaction_ids = [transaction[0] for transaction in transactions]  
    user_ids = [transaction[1] for transaction in transactions] 
    return transaction_ids, user_ids


transactions_data = [
    (101, 1, 250.75, "2024-10-10 10:05:30"),
    (102, 2, 400.00, "2024-10-10 11:15:20"),
    (103, 1, 150.25, "2024-10-11 14:22:10"),
    (104, 3, 600.50, "2024-10-12 16:00:05"),
    (105, 4, 100.00, "2024-10-12 16:45:12"),
    (106, 2, 350.00, "2024-10-13 09:20:50"),
]

unique_user_count = count_unique_users(transactions_data)
print("Total number of unique users involved in transactions:", unique_user_count)

highest_transaction = find_transaction_with_highest_amount(transactions_data)
print("Transaction with the highest amount:", highest_transaction)

transaction_ids, user_ids = extract_transaction_and_user_ids(transactions_data)
print("Transaction IDs:", transaction_ids)
print("User IDs:", user_ids)
