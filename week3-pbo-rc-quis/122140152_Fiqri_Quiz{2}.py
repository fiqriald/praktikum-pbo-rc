import random

# List kata-kata untuk permainan Hangman
kataa = [
    'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
    'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
    'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
    'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
    'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip'
]

# Daftar tahap gambar Hangman
stages = ["""
            ------
            |    |
            |
            |
            |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |
            |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |   /
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |   / \\
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |  --|
            |    |
            |   / \\
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |  --|--
            |    |
            |   / \\
            |
        ------------
        """]

def pilih_kata(kataa):
    # Pilih kata secara acak dari daftar kata-kata
    return random.choice(kataa)

def hangman():
    kata = pilih_kata(kataa)
    word_letters = set(kata)
    guessed_letters = set()
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    
    while incorrect_guesses < len(stages) - 1:
        # Tampilkan status kata
        tampilkan_kata = ''.join([letter if letter in guessed_letters else '_' for letter in kata])
        print(tampilkan_kata)

        # Jika semua huruf sudah ditebak
        if tampilkan_kata == kata:
            print("Selamat! Anda menebak kata itu dengan benar:", kata)
            break

        guess = input("Tebak katanya: ").lower()

        if guess in guessed_letters:
            print("Kata yang anda masukan salah. Coba lagi.")
        elif guess in word_letters:
            print("Teabakan yang bagus!")
            guessed_letters.add(guess)
        else:
            print("Tebakan salah")
            incorrect_guesses += 1
            print(stages[incorrect_guesses])

        print("")

    # Jika pemain gagal menebak kata
    if incorrect_guesses == len(stages) - 1:
        print("Maaf, Anda gagal menebak kata tersebut. Kata itu adalah:", kata)

hangman()
