import tkinter as tk
import random
import pygame

pygame.mixer.init()

pygame.mixer.music.load("/home/uli/Desktop/tec/personal/SnakeGame/gaming-background-music-hd.wav")
pygame.mixer.music.play(-1) #se reproduce en un bucle 

name = input("1st player name: ")
name_2 = input("2nd player name: ")

# Variables para la interfaz
Rows = 25
Columns = 25
Tile_size = 25

Window_width = Tile_size * Rows
Window_height = Tile_size * Columns


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Ventana
window = tk.Tk()
window.title("snake")
window.resizable(False, False)

# Para personalizar el fondo
canvas = tk.Canvas(window, bg="black", width=Window_width, height=Window_height, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()

# Centrar la ventana
Window_width = window.winfo_width()
Window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (Window_width / 2))
window_y = int((screen_height / 2) - (Window_height / 2))

# Para que la ventana comience en el centro de la pantalla
window.geometry(f"{Window_width}x{Window_height}+{window_x}+{window_y}")

# Inicializar el juego
snake = Tile(5 * Tile_size, 5 * Tile_size)
snake2 = Tile(6 * Tile_size, 6 * Tile_size)
food = Tile(random.randint(0, Columns - 1) * Tile_size, random.randint(0, Rows - 1) * Tile_size)

# Para comer la comida
snake_body = []
snake_body_2 = []

# Para mover las serpientes
velocityx = 0
velocityy = 0
velocityx2 = 0
velocityy2 = 0

# GAME OVER
game_over = False
game_over2 = False
game_over3=False
game_over4=False
game_over5=False

score_snake_1 = 0
score_snake_2 = 0

def change_direction(e):
    global velocityx, velocityy, velocityx2, velocityy2
    if game_over or game_over2:
        return

    # Para jugador 1
    if e.keysym == "Shift_R" and velocityy != 1:
        velocityx = 0
        velocityy = -1
    elif e.keysym == "Down" and velocityy != -1:
        velocityx = 0
        velocityy = 1
    elif e.keysym == "Left" and velocityx != 1:
        velocityx = -1
        velocityy = 0
    elif e.keysym == "Right" and velocityx != -1:
        velocityx = 1
        velocityy = 0

    # Para jugador 2
    if e.keysym == "w" and velocityy2 != 1:
        velocityx2 = 0
        velocityy2 = -1
    elif e.keysym == "s" and velocityy2 != -1:
        velocityx2 = 0
        velocityy2 = 1
    elif e.keysym == "a" and velocityx2 != 1:
        velocityx2 = -1
        velocityy2 = 0
    elif e.keysym == "d" and velocityx2 != -1:
        velocityx2 = 1
        velocityy2 = 0

window.bind("<KeyPress>", change_direction)

def move():
    global snake, snake2, food, snake_body, snake_body_2, game_over, game_over2, score_snake_1, score_snake_2, game_over3, game_over4, game_over5

    if game_over and game_over2:
        return

    # Movimiento de la serpiente 1
    snake.x += velocityx * Tile_size
    snake.y += velocityy * Tile_size

    # Movimiento de la serpiente 2
    snake2.x += velocityx2 * Tile_size
    snake2.y += velocityy2 * Tile_size

    # Verificar colisiones para la serpiente 1
    if snake.x < 0 or snake.x >= Window_width or snake.y < 0 or snake.y >= Window_height:
        game_over = True

    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            game_over = True

    # Verificar colisiones para la serpiente 2
    if snake2.x < 0 or snake2.x >= Window_width or snake2.y < 0 or snake2.y >= Window_height:
        game_over2 = True

    for tile in snake_body_2:
        if snake2.x == tile.x and snake2.y == tile.y:
            game_over2 = True

    # Colisiones con la comida
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, Columns - 1) * Tile_size
        food.y = random.randint(0, Rows - 1) * Tile_size
        score_snake_1 += 1

    if snake2.x == food.x and snake2.y == food.y:
        snake_body_2.append(Tile(food.x, food.y))
        food.x = random.randint(0, Columns - 1) * Tile_size
        food.y = random.randint(0, Rows - 1) * Tile_size
        score_snake_2 += 1

    # Actualizar el cuerpo de la serpiente 1
    for i in range(len(snake_body) - 1, 0, -1): #recorre el cuerpo de la serpiente hasta el primero.
        snake_body[i].x = snake_body[i - 1].x #cada parte del cuerpo toma la posicion del anterior. para que el cuerpo siga a la cabeza correctamente
        snake_body[i].y = snake_body[i - 1].y
    if snake_body:
        snake_body[0].x = snake.x #este es el fragmento del cuerpo que recibe la direccion
        snake_body[0].y = snake.y

    # Actualizar el cuerpo de la serpiente 2
    for i in range(len(snake_body_2) - 1, 0, -1):
        snake_body_2[i].x = snake_body_2[i - 1].x
        snake_body_2[i].y = snake_body_2[i - 1].y
    if snake_body_2:
        snake_body_2[0].x = snake2.x
        snake_body_2[0].y = snake2.y


    # Verificar colisiones entre las serpientes
    for tile in snake_body_2:
        if snake.x == tile.x and snake.y == tile.y:
            game_over3 = True

    for tile in snake_body:
        if snake2.x == tile.x and snake2.y == tile.y:
            game_over4 = True

    # Verificar si las cabezas de las serpientes se tocan entre sí
    if snake.x == snake2.x and snake.y == snake2.y:
        game_over = True
        game_over5 = True

def draw():
    global snake, snake2, food, snake_body, snake_body_2, game_over, game_over2, score_snake_1, score_snake_2
    move()

    canvas.delete("all")

    # Dibujar la comida
    canvas.create_rectangle(food.x, food.y, food.x + Tile_size, food.y + Tile_size, fill="red")

    # Dibujar la serpiente 1
    canvas.create_rectangle(snake.x, snake.y, snake.x + Tile_size, snake.y + Tile_size, fill="lime green")
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + Tile_size, tile.y + Tile_size, fill="lime green")

    # Dibujar la serpiente 2
    canvas.create_rectangle(snake2.x, snake2.y, snake2.x + Tile_size, snake2.y + Tile_size, fill="blue")
    for tile in snake_body_2:
        canvas.create_rectangle(tile.x, tile.y, tile.x + Tile_size, tile.y + Tile_size, fill="blue")


    if game_over5:
        canvas.create_text(Window_width / 3, Window_height / 3 + 20, font="Arial 20", text=f"U both loose {name_2, name} ", fill="white")  

    if game_over3:
        canvas.create_text(Window_width / 4, Window_height / 4 + 20, font="Arial 20", text=f"Game over. {name} . U touch player 2 ", fill="white")
        canvas.create_text(Window_width / 3, Window_height / 3 + 20, font="Arial 20", text=f"U win {name_2} ", fill="white")

    if game_over4:
        canvas.create_text(Window_width / 3, Window_height / 3 + 20, font="Arial 20", text=f"Game over. {name_2} . U touch player 1 ", fill="white")
        canvas.create_text(Window_width / 3, Window_height / 3 + 20, font="Arial 20", text=f"U win {name} ", fill="white")

    
    if game_over5 or game_over3 or  game_over4 == True:
        pass
    else:
        if game_over:
            canvas.create_text(Window_width / 2, Window_height / 2 - 20, font="Arial 20", text=f"Game over {name} your score is: {score_snake_1}", fill="white")
        else:
            canvas.create_text(30, 20, font="Arial 10", text=f"Score: {score_snake_1}", fill="red")
        
        if game_over2:
            canvas.create_text(Window_width / 2, Window_height / 2 + 20, font="Arial 20", text=f"Game over {name_2} your score is: {score_snake_2}", fill="white")
        else:
            canvas.create_text(30, 40, font="Arial 10", text=f"Score: {score_snake_2}", fill="blue")
    
    

    window.after(100, draw)

draw()

window.bind("<KeyRelease>", change_direction)

window.mainloop()
