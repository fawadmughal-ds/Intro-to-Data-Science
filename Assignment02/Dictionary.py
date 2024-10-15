def filter_high_ratings(feedback_dict):
    high_ratings = {user_id: details['rating'] for user_id, details in feedback_dict.items() if details['rating'] >= 4}
    return high_ratings

def get_top_ratings(feedback_dict, top_n=5):
    sorted_feedback = sorted(feedback_dict.items(), key=lambda x: x[1]['rating'], reverse=True)
    return sorted_feedback[:top_n]

def combine_feedback(dict1, dict2):
    combined_feedback = dict1.copy()  # Start with dict1
    
    for user_id, feedback in dict2.items():
        if user_id in combined_feedback:
            combined_feedback[user_id]['rating'] = max(combined_feedback[user_id]['rating'], feedback['rating'])
            combined_feedback[user_id]['comments'] += ' ' + feedback['comments']
        else:
            combined_feedback[user_id] = feedback 
    return combined_feedback

def get_ratings_above_3(feedback_dict):
    return {user_id: details['rating'] for user_id, details in feedback_dict.items() if details['rating'] > 3}


user_feedback_1 = {
    1: {'rating': 5, 'comments': 'Excellent service!'},
    2: {'rating': 3, 'comments': 'Good, but could be better.'},
    3: {'rating': 4, 'comments': 'Very satisfied.'},
    4: {'rating': 2, 'comments': 'Not happy with the service.'}
}

user_feedback_2 = {
    2: {'rating': 4, 'comments': 'Updated feedback: Much improved.'},
    5: {'rating': 5, 'comments': 'Outstanding experience!'},
    6: {'rating': 1, 'comments': 'Terrible service.'}
}

filtered_ratings = filter_high_ratings(user_feedback_1)
print("Users with ratings 4 or higher:", filtered_ratings ,'\n')

top_5_users = get_top_ratings(user_feedback_1)
print("Top 5 users by rating:", top_5_users,'\n')

combined_feedback = combine_feedback(user_feedback_1, user_feedback_2)
print("Combined feedback:", combined_feedback,'\n')

ratings_above_3 = get_ratings_above_3(combined_feedback)
print("User IDs with ratings greater than 3:", ratings_above_3)
