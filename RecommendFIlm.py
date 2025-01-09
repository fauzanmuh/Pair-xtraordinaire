import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def recommend_movies(user_ratings, user_index, movie_titles, top_n=5):
    """
    Merekomendasikan film berdasarkan kesamaan pengguna.

    Args:
        user_ratings (ndarray): Matriks rating pengguna (users x movies).
        user_index (int): Indeks pengguna yang ingin direkomendasikan.
        movie_titles (list): Daftar judul film.
        top_n (int): Jumlah rekomendasi yang diinginkan.

    Returns:
        list: Film yang direkomendasikan dengan skor prediksi.
    """
    # Hitung kesamaan antar pengguna
    user_similarity = cosine_similarity(user_ratings)

    # Ambil rating pengguna yang ditargetkan
    target_user_ratings = user_ratings[user_index]

    # Cari indeks film yang belum ditonton (rating == 0)
    unrated_movies = np.where(target_user_ratings == 0)[0]

    # Prediksi rating untuk setiap film yang belum ditonton
    predicted_ratings = {}
    for movie in unrated_movies:
        similar_users = user_similarity[user_index]
        ratings_for_movie = user_ratings[:, movie]

        # Hanya gunakan rating dari pengguna lain yang sudah memberi rating film ini
        mask = ratings_for_movie > 0
        weighted_ratings = similar_users[mask] * ratings_for_movie[mask]
        
        if np.sum(mask) > 0:
            predicted_ratings[movie] = np.sum(weighted_ratings) / np.sum(mask)

    # Urutkan film berdasarkan skor prediksi
    recommended_movies = sorted(predicted_ratings.items(), key=lambda x: x[1], reverse=True)

    # Ambil top N rekomendasi
    recommendations = [(movie_titles[movie], score) for movie, score in recommended_movies[:top_n]]
    return recommendations

# Data Contoh
movie_titles = [
    "The Matrix", "Titanic", "Inception", "Avengers", "Interstellar", "The Godfather"
]

# Matriks Rating (users x movies)
user_ratings = np.array([
    [5, 4, 0, 0, 3, 0],  # User 0
    [4, 0, 5, 3, 4, 0],  # User 1
    [0, 4, 0, 5, 0, 4],  # User 2
    [5, 5, 4, 0, 0, 5],  # User 3
    [0, 0, 4, 5, 4, 0],  # User 4
])

# Indeks Pengguna yang Ingin Direkomendasikan
user_index = 0

# Rekomendasi Film
recommendations = recommend_movies(user_ratings, user_index, movie_titles, top_n=3)
print("Rekomendasi Film untuk Pengguna:")
for movie, score in recommendations:
    print(f"{movie} (Prediksi Skor: {score:.2f})")
