"""Functions to help edit essay homework using string manipulation."""
def capitalize_title(title):
    # convertimos la primer letra de cada palabra en mayuscula
    return title.title()

def check_sentence_ending(sentence):
    # si termina con un . regresamos True si no regresamos False
    return sentence.endswith('.')

def clean_up_spacing(sentence):
    # usamos strip para quitar los espacios al inicio y al final 
    return sentence.strip()

def replace_word_choice(sentence, old_word, new_word):
    # remplazamos old_word por new_word
    return sentence.replace(old_word, new_word)