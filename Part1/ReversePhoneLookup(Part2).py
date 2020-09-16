# Question 4
# You have been asked to write a function that supplies the "reverse lookup" name for the person associated with a phone number.
# This means that given a phone number, you get the name of the person who is registered with that phone number.
# For this problem, you have been asked to write a solution using a dictionary


from typing import Dict

def reverse_lookup_dictionary(phone_num: str,
                              phone_to_name: Dict[str, str]) -> str:
    # """This function receives a phone number phone_num, and a dictionary
    # phone_to_name in which each key is a phone number and each value
    # is the name associated with that phone number.

    # Return the name associated with phone_num in phone_to_name, or
    # an empty string if there is no match.
    #
    # example:
    # >>> reverse_lookup_dictionary("416-555-3498", {"416-555-3498": \
    #     "John A. Macdonald", "647-555-9812": "Louis Riel", "416-555-6543": \
    #     "Canoe Head", "905-555-6681":"Tim Horton"})
    # 'John A. Macdonald'
    # """