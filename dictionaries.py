# Write a Python function that takes two dictionaries as input and returns a new dictionary containing the keys and values that are common to both dictionaries.
def common_keys(dict1, dict2):
    # Get the keys that are common to both dictionaries
    common_keys = set(dict1.keys()) & set(dict2.keys())

    # Create a new dictionary with the common keys and their values
    common_dict = {k: dict1[k] for k in common_keys if dict1[k] == dict2[k]}

    return common_dict
# The function first gets the keys that are common to both dictionaries using the intersection of the sets of keys for each dictionary. It then creates a new dictionary with those keys and their corresponding values, but only if the values are the same in both dictionaries. Finally, it returns the new dictionary containing the common keys and values.