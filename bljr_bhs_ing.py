import random

# Daftar kosakata: {kata asing: arti dalam bahasa Indonesia}
vocabulary = {
    "hello": "halo",
    "goodbye": "selamat tinggal",
    "thank you": "terima kasih",
    "please": "tolong",
    "sorry": "maaf",
    "yes": "iya",
    "no": "tidak",
    "morning": "pagi",
    "night": "malam",
    "food": "makanan",
}

def start_quiz():
    print("=== Program Belajar Bahasa Asing ===")
    print("Cocokkan kata asing dengan artinya dalam bahasa Indonesia.\n")
    score = 0
    total_questions = 5

    # Pilih beberapa kata secara acak
    questions = random.sample(list(vocabulary.items()), total_questions)

    for i, (word, meaning) in enumerate(questions, start=1):
        print(f"{i}. Apa arti dari kata '{word}'?")
        answer = input("Jawaban Anda: ").strip().lower()

        if answer == meaning:
            print("✔️ Benar!\n")
            score += 1
        else:
            print(f"❌ Salah! Jawaban yang benar adalah '{meaning}'.\n")

    print(f"Skor Anda: {score}/{total_questions}")
    if score == total_questions:
        print("Luar biasa! Anda menjawab semua dengan benar! 🎉")
    elif score >= total_questions // 2:
        print("Bagus! Tetap semangat belajar! 👍")
    else:
        print("Jangan menyerah, terus berlatih! 💪")

def main():
    while True:
        start_quiz()
        again = input("\nIngin mencoba lagi? (y/n): ").strip().lower()
        if again != 'y':
            print("Terima kasih telah belajar! Sampai jumpa!")
            break

if __name__ == "__main__":
    main()
