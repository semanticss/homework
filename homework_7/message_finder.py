def solve_message(ciphertext, S_inv, p):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    char_to_num = {c: i for i, c in enumerate(chars)}
    num_to_char = {i: c for i, c in enumerate(chars)}
    
    plaintext = ""
    for char in ciphertext:
        c_val = char_to_num[char]
        m_val = (c_val * S_inv) % p
        plaintext += num_to_char[m_val]
        
    return plaintext

ciphertext = "Q6MI7I2TBJ"
S_inv = 33
p = 37

print(solve_message(ciphertext, S_inv, p))