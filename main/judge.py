#
def classify_dict_values(dictionary):
    classified_dict = {}
    
    for key, value in dictionary.items():
        value_length = len(value)
        
        if value_length not in classified_dict:
            classified_dict[value_length] = []
            
        classified_dict[value_length].append(key)
    
    return classified_dict
##该函数用于整理回复报文，按键为长度，payload为值的形式