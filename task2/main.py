import turtle


def koch_curve(t, order, size):
    """Функція для створення кривої Коха."""
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    """Функція для створення сніжинки Коха."""
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Створення сніжинки Коха шляхом малювання трьох кривих Коха
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    # Виклик функції з можливістю користувача вказати рівень рекурсії
    try:
        order = int(input("Будь ласка, введіть рівень рекурсії для сніжинки Коха: "))
        draw_koch_snowflake(order)
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")
