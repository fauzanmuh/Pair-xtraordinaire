import random

class LanguageLearning:
    def __init__(self):
        # Kamus kata yang akan digunakan untuk latihan
        self.words = {
            "hello": "hola",  # English -> Spanish
            "good morning": "buenos días",
            "thank you": "gracias",
            "goodbye": "adiós",
            "please": "por favor",
            "yes": "sí",
            "no": "no",
            "sorry": "lo siento",
            "cat": "gato",
            "dog": "perro"
        }
    
    def start(self):
        print("Selamat datang di program belajar bahasa!")
        print("Kita akan mulai dengan beberapa kata dan frasa dalam bahasa asing.")
        self.quiz()
    
    def quiz(self):
        # Pilih kata secara acak
        english_word, spanish_word = random.choice(list(self.words.items()))
        
        print(f"\nApa terjemahan dari kata '{english_word}' dalam bahasa Spanyol?")
        answer = input("Jawaban Anda: ")
        
        if answer.lower() == spanish_word.lower():
            print("Benar! Bagus sekali.")
        else:
            print(f"Salah. Jawaban yang benar adalah '{spanish_word}'.")
        
        self.ask_again()
    
    def ask_again(self):
        # Tanya apakah pengguna ingin mencoba lagi
        again = input("\nApakah kamu ingin mencoba lagi? (y/n): ")
        
        if again.lower() == 'y':
            self.quiz()
        else:
            print("Terima kasih telah belajar! Sampai jumpa lagi.")

# Menjalankan program
if __name__ == "__main__":
    learning = LanguageLearning()
    learning.start()
