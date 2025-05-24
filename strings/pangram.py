def is_pangram(sentence):
    a = list("qwertyuiopasdfghjklzxcvbnm")
    oracion = sentence.lower()

    for elemento in oracion:
        if elemento in a:
            a.remove(elemento)
    
    return not a
        
palabra = "Five quacking Zephyrs jolt my wax bed."
print(is_pangram(palabra))