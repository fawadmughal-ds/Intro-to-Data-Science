
def visitors_both_pages_a_b(page_a, page_b):
    return page_a & page_b  

def visitors_either_page_a_or_c_but_not_both(page_a, page_c):
    return page_a ^ page_c  

def update_page_a_visitors(page_a, new_visitors):
    page_a.update(new_visitors)  

def remove_users_from_page_b(page_b, users_to_remove):
    page_b.difference_update(users_to_remove)  


page_a_visitors = {1, 2, 3, 4, 5}
page_b_visitors = {3, 4, 6, 7}
page_c_visitors = {5, 6, 8, 9}

users_both_pages = visitors_both_pages_a_b(page_a_visitors, page_b_visitors)
print("Users who visited both Page A and Page B:", users_both_pages)

users_either_a_or_c = visitors_either_page_a_or_c_but_not_both(page_a_visitors, page_c_visitors)
print("Users who visited either Page A or Page C, but not both:", users_either_a_or_c)

new_visitors = {10, 11, 5}
update_page_a_visitors(page_a_visitors, new_visitors)
print("Updated Page A visitors:", page_a_visitors)

users_to_remove = [3, 7]
remove_users_from_page_b(page_b_visitors, users_to_remove)
print("Updated Page B visitors after removing users:", page_b_visitors)
