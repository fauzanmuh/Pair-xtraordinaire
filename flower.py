import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("white")

# Setup pen
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(10)
pen.color("red")

# Fungsi untuk menggambar kelopak bunga
def draw_petal():
    pen.circle(100, 60)  # Membuat lengkungan kelopak bunga
    pen.left(120)
    pen.circle(100, 60)
    pen.left(120)

# Fungsi utama untuk menggambar bunga
def draw_flower():
    for _ in range(6):  # Menggambar 6 kelopak bunga
        draw_petal()
        pen.left(60)

# Menyusun bunga
pen.up()
pen.setposition(0, -100)  # Menempatkan turtle ke posisi yang lebih baik
pen.down()
draw_flower()

# Menyembunyikan turtle setelah selesai menggambar
pen.hideturtle()

# Menunggu untuk menutup layar
turtle.done()
