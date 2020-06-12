
def LZ77_coding():
    search_buffer = list()
    look_ahead_buffer = list()
    token = list()


    for character in s:
        look_ahead_buffer.append(character)

    for character in s:
        if character not in search_buffer:
            search_buffer.append(character)
            look_ahead_buffer.remove(character)
            token.append([0,0,character])
        else:
            parola = look_ahead_buffer[0] + look_ahead_buffer[1]
            for i in range(2, len(look_ahead_buffer) - 1)
                if parola in search_buffer:
                    parola = parola + look_ahead_buffer[i]
            print(parola)













if __name__ == '__main__':
    s = input("Inserire stringa da codificare: ")
    LZ77_coding()
