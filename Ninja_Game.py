from tkinter import *
import random
import sys

window = Tk()
window.geometry("450x410")
window.title("Ninja Dash")
window.configure(bg="#432e55")
score = 0
name = ""
game_level = 1
Load = False
paused = True
freeze = True
classic_movement = True
list = []
list_1 = []
T = 0
K = 0


def store_variables():
    """Stores the current game into the scoreboard"""
    global user_input, score, name
    if Load == False:
        name = user_input.get()
    if score < 1000:
        score = str(score)
        score = score.zfill(4)
    else:
        pass
    with open("scoreboard.txt", "a") as f:
        f.write(str(score) + "," + name + "\n")


def leaderboard():
    """displays the leaderboard"""
    newWindow = Toplevel(window)
    newWindow.title("Leaderboards")
    newWindow.configure(bg="#c8abba")
    newWindow.geometry("1280x720")
    # sets the geometry of toplevel
    file = open("scoreboard.txt", "r")
    readthefile = file.readlines()
    sortedData = sorted(readthefile, reverse=True)
    for line in range(5):
        list.append(str(line + 1) + "   " + str(sortedData[line]) + "\n")
    n = len(list)
    element = "\n" + "\n" + ""
    for i in range(n):
        element = element + list[i] + "\n"
    Label(
        newWindow,
        text="\n" + "Top 5 Leaderboard",
        font=("Helvetica", 26, "bold"),
        bg="#c8abba",
        width=40,
    ).pack(side=TOP, fill="x")
    Label(
        newWindow, text=element, font=("Helvetica", 18, "bold"), bg="#c8abba", width=40
    ).pack(side=TOP, fill="x")
    endSplash = Button(
        newWindow,
        text="Play Again",
        highlightbackground="yellow",
        height=2,
        bg="#c8abba",
        font=("Helvetica", 18,"bold"),
        command=restart,
        borderwidth=0,
        width=20,
    )
    endSplash.pack(side=TOP)


def restart():
    """restarts the game"""
    global score, game_level, T, K, list, list_1
    score = 0
    game_level = 1
    list = []
    list_1 = []
    T = 0
    K = 0
    first_level()


def first_level():
    """Creates the first level"""
    window.withdraw()
    new_window = Toplevel(window)
    new_window.title("First Level")
    new_window.configure(bg="yellow")
    new_window.geometry("1280x720")
    new_window.resizable(False, False)
    background = Canvas(new_window, width=600, height=600, bg="orange", bd=1, border=1)
    background.grid(column=1, row=2, columnspan=5)

    def save_game():
        """Saves the current game data in a file, Game_file.txt"""
        global score, game_level, name
        name = user_input.get()
        with open("Game_file.txt", "w") as file:
            file.write(str(score) + "\n" + str(game_level) + "\n" + name)

    endSplash = Button(
        new_window,
        text="Save Game",
        highlightbackground="yellow",
        height=2,
        bg="yellow",
        font=("Helvetica", 18),
        command=save_game,
        borderwidth=0,
        width=20,
    )
    endSplash.grid(column=6, row=0)

    def update_score():
        """Updates the score in the game"""
        Label1 = Label(
            new_window,
            text="Score:{}".format(score),
            font=("consolas", 20),
            bg="yellow",
        )
        Label1.grid(column=0, row=0)

    update_score()

    def freeze_enemies(event):
        """Stops the enemies from moving"""
        global freeze
        if freeze == True:
            freeze = False
        else:
            freeze = True
            new_window.after(500, move_enemy)

    def update_paused():
        """update display to show that the game is paused"""
        if paused == False:
            Label3 = Label(
                new_window,
                text="Game is paused",
                font=("consolas", 20),
                bg="yellow",
                width=20,
            )
            Label3.grid(column=5, row=0)
        else:
            Label3 = Label(
                new_window,
                text="Game is running",
                font=("consolas", 20),
                bg="yellow",
                width=20,
            )
            Label3.grid(column=5, row=0)

    update_paused()
    """pauses the game"""
    Label2 = Label(
        new_window,
        text="Game Level:{}".format(game_level),
        font=("consolas", 20),
        bg="yellow",
    )
    Label2.grid(column=3, row=0)

    ninja_star_Img = PhotoImage(file="ninja_star.png")
    ninja_star_Img_image = ninja_star_Img

    ninjaImg = PhotoImage(file="Ninja.png")
    ninja_Img = ninjaImg
    ninja = background.create_image(50, 200, image=ninjaImg)

    enemyImg = PhotoImage(file="Enemy.png")
    enemy_Img = enemyImg
    enemy = background.create_image(500, 300, image=enemyImg)

    def edge_Reached():
        """Prevents the user from going out of bounds"""
        ninja_boundary = background.bbox(ninja)
        ninja_left = ninja_boundary[0]
        ninja_top = ninja_boundary[1]
        ninja_right = ninja_boundary[2]
        ninja_bottom = ninja_boundary[3]
        if ninja_left < 0:
            background.move(ninja, 15, 0)
        if ninja_top < 0:
            background.move(ninja, 0, 15)
        if ninja_right > 600:
            background.move(ninja, -15, 0)
        if ninja_bottom > 600:
            background.move(ninja, 0, -15)

    def collision():
        """Checks if the shuriken makes contact with the enemy"""
        global score, game_level
        N_star = background.bbox(ninja_star)
        enmy = background.bbox(enemy)
        if enmy[0] < N_star[2] < enmy[2] and enmy[1] < N_star[1] < enmy[3]:
            background.move(enemy, 5000, 5000)
            score = score + 100
            game_level += 1
            new_window.destroy()
            second_level()

    def boss_key(event):
        """pauses the game if boss key is pressed"""
        global paused
        if paused:
            paused = False
            update_paused()
            boss()
            new_window.wm_state("iconic")
        else:
            new_window.state("normal")

    def boss():
        """proves functionality to boss key"""
        newWindow4 = Toplevel(window)
        newWindow4.title("Leaderboards")
        newWindow4.configure(bg="yellow")
        newWindow4.geometry("1863x931")
        Canvas_2 = Canvas(newWindow4, height=931, width=1863)
        filename = PhotoImage(file="Background.png")
        background_label = Label(newWindow4, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = filename  # reference to the image
        Canvas_2.grid(row=0, column=0, rowspan=5, columnspan=3)

    def move_right(event):
        if paused:
            background.move(ninja, 15, 0)
            edge_Reached()

    def move_left(event):
        if paused:
            background.move(ninja, -15, 0)
            edge_Reached()

    def move_up(event):
        if paused:
            background.move(ninja, 0, -15)
            edge_Reached()

    def move_down(event):
        if paused:
            background.move(ninja, 0, 15)
            edge_Reached()

    def move_ninjastar():
        if paused:
            global ninja_star, Loop
            background.move(ninja_star, 20, 0)
            collision()
            Loop = window.after(10, move_ninjastar)
            collision()

    def skip(event):
        global game_level
        game_level += 1
        new_window.destroy()
        second_level()

    def pause(event):
        """Chcecks whether to pause or unpause the game"""
        global paused
        if paused:
            paused = False
            update_paused()
        else:
            paused = True
            update_paused()
            new_window.after(500, move_enemy)

    def move_enemy():
        """Gives random movement to the enemies"""
        global paused, freeze
        if paused and freeze:
            background.move(
                enemy, random.randrange(-30, 30), (random.randrange(-30, 30))
            )
            enemy_edge_reached()
            new_window.after(500, move_enemy)  # reschedule event in 2 seconds

    new_window.after(500, move_enemy)

    def enemy_edge_reached():
        """Makes sure the enemy stays within bounds"""
        enemy_boundary = background.bbox(enemy)
        enemy_left = enemy_boundary[0]
        enemy_top = enemy_boundary[1]
        enemy_right = enemy_boundary[2]
        enemy_bottom = enemy_boundary[3]
        if enemy_left < 100:
            background.move(enemy, 30, 0)
        if enemy_top < 0:
            background.move(enemy, 0, 30)
        if enemy_right > 600:
            background.move(enemy, -30, 0)
        if enemy_bottom > 600:
            background.move(enemy, 0, -30)

    def add_score(event):
        global score
        score = score + 100
        update_score()

    def shoot(event):
        """creates and provides movement for the shuriken"""
        if paused:
            global ninja_star, Loop, score
            score = score - 10
            update_score()
            try:
                window.after_cancel(Loop)
                background.delete(ninja_star)
                ninja1 = background.bbox(ninja)
                horizontal_middle = (ninja1[0] + ninja1[2]) / 2
                vertical_middle = (ninja1[1] + ninja1[3]) / 2
                ninja_star = background.create_image(
                    horizontal_middle, vertical_middle, image=ninja_star_Img
                )
                move_ninjastar()
            except NameError:
                ninja1 = background.bbox(ninja)
                horizontal_middle = (ninja1[0] + ninja1[2]) / 2
                vertical_middle = (ninja1[1] + ninja1[3]) / 2
                ninja_star = background.create_image(
                    horizontal_middle, vertical_middle, image=ninja_star_Img
                )
                move_ninjastar()

    if classic_movement == True:
        background.bind_all("<Right>", move_right)
        background.bind_all("<Left>", move_left)
        background.bind_all("<Up>", move_up)
        background.bind_all("<Down>", move_down)
        background.bind_all("<space>", shoot)
        background.bind_all("<p>", pause)
        background.bind_all("<b>", boss_key)
        background.bind_all("<k>", skip)
        background.bind_all("<c>", add_score)
        background.bind_all("<f>", freeze_enemies)
    else:
        background.bind_all("<d>", move_right)
        background.bind_all("<a>", move_left)
        background.bind_all("<w>", move_up)
        background.bind_all("<s>", move_down)
        background.bind_all("<space>", shoot)
        background.bind_all("<p>", pause)
        background.bind_all("<b>", boss_key)
        background.bind_all("<k>", skip)
        background.bind_all("<c>", add_score)
        background.bind_all("<f>", freeze_enemies)
    new_window.mainloop()


def second_level():
    """Creates the second level"""
    new_window1 = Toplevel(window)
    new_window1.title("Second Level")
    new_window1.configure(bg="yellow")
    new_window1.geometry("1280x720")

    background = Canvas(new_window1, width=600, height=600, bg="orange")
    background.grid(column=1, row=2, columnspan=5)

    def save_game():
        """Saves the current game data in a file, Game_file.txt"""
        global score, game_level, name
        name = user_input.get()
        with open("Game_file.txt", "w") as file:
            file.write(str(score) + "\n" + str(game_level) + "\n" + name)

    endSplash = Button(
        new_window1,
        text="Save Game",
        highlightbackground="yellow",
        height=2,
        bg="yellow",
        font=("Helvetica", 18),
        command=save_game,
        borderwidth=0,
        width=20,
    )
    endSplash.grid(column=6, row=0)

    def pause(event):
        global paused
        if paused:
            paused = False
            update_paused()
        else:
            paused = True
            update_paused()
            new_window1.after(500, move_enemy)

    def update_score():
        """Updates the score in the game"""
        Label1 = Label(
            new_window1,
            text="Score:{}".format(score),
            font=("consolas", 20),
            bg="yellow",
            width=15,
        )
        Label1.grid(column=0, row=0, padx=5, pady=5)

    update_score()
    Label2 = Label(
        new_window1,
        text="Game Level:{}".format(game_level),
        font=("consolas", 20),
        bg="yellow",
    )
    Label2.grid(column=3, row=0, padx=5, pady=5)

    def update_paused():
        """update display to show that the game is paused"""
        if paused == False:
            Label3 = Label(
                new_window1,
                text="Game is paused",
                font=("consolas", 20),
                bg="yellow",
                width=20,
            )
            Label3.grid(column=5, row=0)
        else:
            Label3 = Label(
                new_window1,
                text="Game is running",
                font=("consolas", 20),
                bg="yellow",
                width=20,
            )
            Label3.grid(column=5, row=0)

    update_paused()

    ninja_star_Img = PhotoImage(file="ninja_star.png")
    ninja_star_Img_image = ninja_star_Img

    ninjaImg = PhotoImage(file="Ninja.png")
    ninja_Img = ninjaImg
    ninja = background.create_image(50, 200, image=ninjaImg)

    enemyImg1 = PhotoImage(file="Enemy.png")
    enemy_Img = enemyImg1
    enemy1 = background.create_image(500, 200, image=enemyImg1)
    enemy2 = background.create_image(500, 400, image=enemyImg1)

    def boss_key(event):
        global paused
        if paused:
            paused = False
            update_paused()
            boss()
            new_window1.wm_state("iconic")
        else:
            new_window1.state("normal")

    def freeze_enemies(event):
        global freeze
        if freeze == True:
            freeze = False
        else:
            freeze = True
            new_window1.after(500, move_enemy)

    def boss():
        newWindow4 = Toplevel(window)
        newWindow4.title("Leaderboards")
        newWindow4.configure(bg="yellow")
        newWindow4.geometry("1863x931")
        Canvas_2 = Canvas(newWindow4, height=931, width=1863)
        filename = PhotoImage(file="Background.png")
        background_label = Label(newWindow4, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        background_label.image = filename  # reference to the image
        Canvas_2.grid(row=0, column=0, rowspan=5, columnspan=3)

    def edge_Reached():
        ninja_boundary = background.bbox(ninja)
        ninja_left = ninja_boundary[0]
        ninja_top = ninja_boundary[1]
        ninja_right = ninja_boundary[2]
        ninja_bottom = ninja_boundary[3]
        if ninja_left < 0:
            background.move(ninja, 15, 0)
        if ninja_top < 0:
            background.move(ninja, 0, 15)
        if ninja_right > 600:
            background.move(ninja, -15, 0)
        if ninja_bottom > 600:
            background.move(ninja, 0, -15)

    def skip(event):
        global game_level
        game_level += 1
        new_window1.destroy()
        third_level()

    def collision1():
        global T, score, game_level
        N_star1 = background.bbox(ninja_star1)
        enmy1 = background.bbox(enemy1)
        enmy2 = background.bbox(enemy2)
        if enmy1[0] < N_star1[2] < enmy1[2] and enmy1[1] < N_star1[1] < enmy1[3]:
            background.move(enemy1, 5000, 5000)
            T = T + 1
            score = score + 100
            update_score()
        if enmy2[0] < N_star1[2] < enmy2[2] and enmy2[1] < N_star1[1] < enmy2[3]:
            background.move(enemy2, 5000, 5000)
            T = T + 1
            score = score + 100
            update_score()
        if T == 2:
            game_level += 1
            new_window1.destroy()
            third_level()

    def move_right(event):
        if paused:
            background.move(ninja, 15, 0)
            edge_Reached()

    def move_left(event):
        if paused:
            background.move(ninja, -15, 0)
            edge_Reached()

    def move_up(event):
        if paused:
            background.move(ninja, 0, -15)
            edge_Reached()

    def move_down(event):
        if paused:
            background.move(ninja, 0, 15)
            edge_Reached()

    def move_ninjastar():
        global ninja_star1, Loop
        background.move(ninja_star1, 20, 0)
        collision1()
        Loop = window.after(10, move_ninjastar)
        collision1()

    def move_enemy():
        global paused, freeze
        if paused and freeze:
            background.move(
                enemy1, random.randrange(-40, 40), (random.randrange(-40, 40))
            )
            background.move(
                enemy2, random.randrange(-40, 40), (random.randrange(-40, 40))
            )
            enemy_edge_reached()
            new_window1.after(500, move_enemy)  # reschedule event in 2 seconds

    new_window1.after(500, move_enemy)

    def enemy_edge_reached():
        enemy_boundary = background.bbox(enemy1)
        enemy_left = enemy_boundary[0]
        enemy_top = enemy_boundary[1]
        enemy_right = enemy_boundary[2]
        enemy_bottom = enemy_boundary[3]
        if enemy_left < 100:
            background.move(enemy1, 40, 0)
        if enemy_top < 0:
            background.move(enemy1, 0, 40)
        if enemy_right > 600:
            background.move(enemy1, -40, 0)
        if enemy_bottom > 600:
            background.move(enemy1, 0, -40)

        enemy_boundary1 = background.bbox(enemy2)
        enemy_left1 = enemy_boundary1[0]
        enemy_top1 = enemy_boundary1[1]
        enemy_right1 = enemy_boundary1[2]
        enemy_bottom1 = enemy_boundary1[3]
        if enemy_left1 < 100:
            background.move(enemy2, 30, 0)
        if enemy_top1 < 0:
            background.move(enemy2, 0, 30)
        if enemy_right1 > 600:
            background.move(enemy2, -30, 0)
        if enemy_bottom1 > 600:
            background.move(enemy2, 0, -30)

    def add_score(event):
        global score
        score = score + 100
        update_score()

    def shoot(event):
        global ninja_star1, Loop, score
        score = score - 10
        update_score()
        try:
            window.after_cancel(Loop)
            background.delete(ninja_star1)
            ninja1 = background.bbox(ninja)
            horizontal_middle = (ninja1[0] + ninja1[2]) / 2
            vertical_middle = (ninja1[1] + ninja1[3]) / 2
            ninja_star1 = background.create_image(
                horizontal_middle, vertical_middle, image=ninja_star_Img
            )
            move_ninjastar()
        except NameError:
            ninja1 = background.bbox(ninja)
            horizontal_middle = (ninja1[0] + ninja1[2]) / 2
            vertical_middle = (ninja1[1] + ninja1[3]) / 2
            ninja_star1 = background.create_image(
                horizontal_middle, vertical_middle, image=ninja_star_Img
            )
            move_ninjastar()

    if classic_movement == True:
        background.bind_all("<Right>", move_right)
        background.bind_all("<Left>", move_left)
        background.bind_all("<Up>", move_up)
        background.bind_all("<Down>", move_down)
        background.bind_all("<space>", shoot)
        background.bind_all("<p>", pause)
        background.bind_all("<b>", boss_key)
        background.bind_all("<k>", skip)
        background.bind_all("<c>", add_score)
        background.bind_all("<f>", freeze_enemies)
    else:
        background.bind_all("<d>", move_right)
        background.bind_all("<a>", move_left)
        background.bind_all("<w>", move_up)
        background.bind_all("<s>", move_down)
        background.bind_all("<space>", shoot)
        background.bind_all("<p>", pause)
        background.bind_all("<b>", boss_key)
        background.bind_all("<k>", skip)
        background.bind_all("<c>", add_score)
        background.bind_all("<f>", freeze_enemies)

    new_window1.mainloop()


def third_level():
    """creates the third level"""
    new_window2 = Toplevel(window)
    new_window2.title("Third level")
    new_window2.configure(bg="yellow")
    new_window2.geometry("1280x720")

    background = Canvas(new_window2, width=600, height=600, bg="orange")
    background.grid(column=1, row=2, columnspan=5)

    def save_game():
        global score, game_level, name
        name = user_input.get()
        with open("Game_file.txt", "w") as file:
            file.write(str(score) + "\n" + str(game_level) + "\n" + name)

    endSplash = Button(
        new_window2,
        text="Save Game",
        highlightbackground="yellow",
        height=2,
        bg="yellow",
        font=("Helvetica", 18),
        command=save_game,
        borderwidth=0,
        width=20,
    )
    endSplash.grid(column=6, row=0)

    def pause(event):
        global paused
        if paused:
            paused = False
            update_paused()
        else:
            paused = True
            update_paused()
            new_window2.after(500, move_enemy)

    def update_paused():
        """update display to show that the game is paused"""
        if paused == False:
            Label3 = Label(
                new_window2,
                text="Game is paused",
                font=("consolas", 20),
                bg="yellow",
                width=20,
            )
            Label3.grid(column=5, row=0)
        else:
            Label3 = Label(
                new_window2,
                text="Game is running",
                font=("consolas", 20),
                bg="yellow",
                width=20,
            )
            Label3.grid(column=5, row=0)

    update_paused()

    def update_score():
        Label1 = Label(
            new_window2,
            text="Score:{}".format(score),
            font=("consolas", 20),
            bg="yellow",
        )
        Label1.grid(column=0, row=0, padx=5, pady=5)

    update_score()
    Label2 = Label(
        new_window2,
        text="Game Level:{}".format(game_level),
        font=("consolas", 20),
        bg="yellow",
    )
    Label2.grid(column=3, row=0, padx=5, pady=5)

    ninja_star_Img = PhotoImage(file="ninja_star.png")
    ninja_star_Img_image = ninja_star_Img

    ninjaImg = PhotoImage(file="Ninja.png")
    ninja_Img = ninjaImg
    ninja = background.create_image(50, 200, image=ninjaImg)

    enemyImg3 = PhotoImage(file="Enemy.png")
    enemy_Img = enemyImg3
    enemy3 = background.create_image(500, 100, image=enemyImg3)
    enemy4 = background.create_image(500, 300, image=enemyImg3)
    enemy5 = background.create_image(500, 500, image=enemyImg3)

    def boss_key(event):
        global paused
        if paused:
            paused = False
            update_paused()
            boss()
            new_window2.wm_state("iconic")
        else:
            new_window2.state("normal")

    def boss():
        newWindow4 = Toplevel(window)
        newWindow4.title("Boss_key")
        newWindow4.configure(bg="yellow")
        newWindow4.geometry("1863x931")
        Canvas_2 = Canvas(newWindow4, height=931, width=1863)
        filename = PhotoImage(file="Background.png")
        background_label = Label(newWindow4, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        background_label.image = filename  # reference to the image
        Canvas_2.grid(row=0, column=0, rowspan=5, columnspan=3)

    def edge_Reached():
        ninja_boundary = background.bbox(ninja)
        ninja_left = ninja_boundary[0]
        ninja_top = ninja_boundary[1]
        ninja_right = ninja_boundary[2]
        ninja_bottom = ninja_boundary[3]
        if ninja_left < 0:
            background.move(ninja, 15, 0)
        if ninja_top < 0:
            background.move(ninja, 0, 15)
        if ninja_right > 600:
            background.move(ninja, -15, 0)
        if ninja_bottom > 600:
            background.move(ninja, 0, -15)

    def collision1():
        global T, score, K
        N_star1 = background.bbox(ninja_star1)
        enmy1 = background.bbox(enemy3)
        enmy2 = background.bbox(enemy4)
        enmy3 = background.bbox(enemy5)
        if enmy1[0] < N_star1[2] < enmy1[2] and enmy1[1] < N_star1[1] < enmy1[3]:
            background.move(enemy3, 5000, 5000)
            K = K + 1
            score = score + 100
            update_score()
        if enmy2[0] < N_star1[2] < enmy2[2] and enmy2[1] < N_star1[1] < enmy2[3]:
            background.move(enemy4, 5000, 5000)
            K = K + 1
            score = score + 100
            update_score()
        if enmy3[0] < N_star1[2] < enmy3[2] and enmy3[1] < N_star1[1] < enmy3[3]:
            background.move(enemy5, 5000, 5000)
            K = K + 1
            score = score + 100
            update_score()
        if K == 3:
            store_variables()
            leaderboard()
            new_window2.destroy()

    def skip(event):
        global game_level
        game_level += 1
        new_window2.destroy()
        store_variables()
        leaderboard()

    def move_right(event):
        background.move(ninja, 15, 0)
        edge_Reached()

    def move_enemy():
        global paused, freeze
        if paused and freeze:
            background.move(
                enemy3, random.randrange(-50, 50), (random.randrange(-50, 50))
            )
            background.move(
                enemy4, random.randrange(-50, 50), (random.randrange(-50, 50))
            )
            background.move(
                enemy5, random.randrange(-50, 50), (random.randrange(-50, 50))
            )
            enemy_edge_reached()
            new_window2.after(500, move_enemy)  # reschedule event in 2 seconds

    new_window2.after(500, move_enemy)

    def enemy_edge_reached():
        enemy_boundary = background.bbox(enemy3)
        enemy_left = enemy_boundary[0]
        enemy_top = enemy_boundary[1]
        enemy_right = enemy_boundary[2]
        enemy_bottom = enemy_boundary[3]

        if enemy_left < 100:
            background.move(enemy3, 50, 0)
        if enemy_top < 0:
            background.move(enemy3, 0, 50)
        if enemy_right > 600:
            background.move(enemy3, -50, 0)
        if enemy_bottom > 600:
            background.move(enemy3, 0, -50)

        enemy_boundary1 = background.bbox(enemy4)
        enemy_left1 = enemy_boundary1[0]
        enemy_top1 = enemy_boundary1[1]
        enemy_right1 = enemy_boundary1[2]
        enemy_bottom1 = enemy_boundary1[3]

        if enemy_left1 < 100:
            background.move(enemy4, 50, 0)
        if enemy_top1 < 0:
            background.move(enemy4, 0, 50)
        if enemy_right1 > 600:
            background.move(enemy4, -50, 0)
        if enemy_bottom1 > 600:
            background.move(enemy4, 0, -50)

        enemy_boundary2 = background.bbox(enemy5)
        enemy_left2 = enemy_boundary2[0]
        enemy_top2 = enemy_boundary2[1]
        enemy_right2 = enemy_boundary2[2]
        enemy_bottom2 = enemy_boundary2[3]

        if enemy_left2 < 0:
            background.move(enemy5, 30, 0)
        if enemy_top2 < 0:
            background.move(enemy5, 0, 30)
        if enemy_right2 > 600:
            background.move(enemy5, -30, 0)
        if enemy_bottom2 > 600:
            background.move(enemy5, 0, -30)

    def move_left(event):
        if paused:
            background.move(ninja, -15, 0)
            edge_Reached()

    def move_up(event):
        if paused:
            background.move(ninja, 0, -15)
            edge_Reached()

    def move_down(event):
        if paused:
            background.move(ninja, 0, 15)
            edge_Reached()

    def add_score(event):
        global score
        score = score + 100
        update_score()

    def move_ninjastar():
        global ninja_star1, Loop
        background.move(ninja_star1, 20, 0)
        collision1()
        Loop = window.after(10, move_ninjastar)
        collision1()

    def freeze_enemies(event):
        global freeze
        if freeze == True:
            freeze = False
        else:
            freeze = True
            new_window2.after(500, move_enemy)

    def shoot(event):
        global ninja_star1, Loop, score
        score = score - 10
        update_score()
        try:
            window.after_cancel(Loop)
            background.delete(ninja_star1)
            ninja1 = background.bbox(ninja)
            horizontal_middle = (ninja1[0] + ninja1[2]) / 2
            vertical_middle = (ninja1[1] + ninja1[3]) / 2
            ninja_star1 = background.create_image(
                horizontal_middle, vertical_middle, image=ninja_star_Img
            )
            move_ninjastar()
        except NameError:
            ninja1 = background.bbox(ninja)
            horizontal_middle = (ninja1[0] + ninja1[2]) / 2
            vertical_middle = (ninja1[1] + ninja1[3]) / 2
            ninja_star1 = background.create_image(
                horizontal_middle, vertical_middle, image=ninja_star_Img
            )
            move_ninjastar()

    if classic_movement == True:
        background.bind_all("<Right>", move_right)
        background.bind_all("<Left>", move_left)
        background.bind_all("<Up>", move_up)
        background.bind_all("<Down>", move_down)
        background.bind_all("<space>", shoot)
        background.bind_all("<p>", pause)
        background.bind_all("<b>", boss_key)
        background.bind_all("<k>", skip)
        background.bind_all("<c>", add_score)
        background.bind_all("<f>", freeze_enemies)
    else:
        background.bind_all("<d>", move_right)
        background.bind_all("<a>", move_left)
        background.bind_all("<w>", move_up)
        background.bind_all("<s>", move_down)
        background.bind_all("<space>", shoot)
        background.bind_all("<p>", pause)
        background.bind_all("<b>", boss_key)
        background.bind_all("<k>", skip)
        background.bind_all("<c>", add_score)
        background.bind_all("<f>", freeze_enemies)
    new_window2.mainloop()


def Instructions():
    """Gives instructions to user on how to play the game"""
    new_window1 = Toplevel(window)
    new_window1.title("How to Play")
    new_window1.configure(bg="#c8abba")
    new_window1.geometry("1280x480")
    labelText.set(
        "Welcome to Ninja Dash"
        + "\n"
        + "\n"
        + "\n"
        + "Your task is to defeat all the enemies and advance to the next level as efficiently as possible"
        + "\n"
        + "\n"
        + "To move: Depending on user selection, you can use either the arrow keys"
        + "\n"
        + "or wasd to control the movement of the character."
        + "\n"
        + "\n"
        + "To throw the shuriken, press 'space'. Be sure not to waste the shurikens as they are expensive"
        + "\n"
        + "and reduce the number of points recieved."
        + "\n"
        + "\n"
        + "Cheats: the commands to trigger the cheats are 'c', 'k' and 'f'. Each of these have a unique ability"
        + "\n"
        + "that you can discover when playing."
        + "\n"
        + "\n"
        + "Quality of life features: You can pause the game using 'p' and activite the boss key using 'b'"
        + "\n"
        + "\n"
        + "Have fun"
    )
    label_inst = Label(
        new_window1,
        textvariable=labelText,
        bg="#c8abba",
        font=("Helvetica", 18, "bold"),
        fg="black",
    )
    label_inst.pack(side=TOP)


def arrow_movement():
    """allows the character to be moved by arrow keys"""
    global classic_movement
    classic_movement = True
    window.mainloop()


def wasd_movement():
    """allows the user top move using wasd"""
    global classic_movement
    classic_movement = False
    window.mainloop()


def controls():
    """allows the user to choose the controls"""
    new_window1 = Toplevel(window)
    new_window1.title("Choose controls")
    new_window1.configure(bg="#432e55")
    new_window1.geometry("400x130")
    endSplash = Button(
        new_window1,
        text="Arrow Keys",
        highlightbackground="black",
        height=2,
        bg="#c8abba",
        font=("Helvetica", 18, "bold"),
        command=arrow_movement,
        width=20,
    )
    endSplash.pack(side=TOP, fill="x")
    endSplash = Button(
        new_window1,
        text="WASD",
        highlightbackground="black",
        height=2,
        bg="#c8abba",
        font=("Helvetica", 18, "bold"),
        command=wasd_movement,
        width=20,
    )
    endSplash.pack(side=TOP, fill="x")


def quit_game():
    """Allows the user to exit the game"""
    sys.exit()


def load_game():
    """Allows the user to load to the previous saved instance"""
    global score, game_level, name, Load
    with open("Game_file.txt") as file_in:
        for line in file_in:
            list_1.append(line)
    score = int(list_1[0])
    game_level = int(list_1[1])
    name = list_1[2]
    Load = True
    if game_level == 1:
        first_level()
    elif game_level == 2:
        second_level()
    else:
        third_level()


labelText = StringVar()
labelText1 = StringVar()
labelText1.set("Enter your 3-letter username")
labelDir = Label(
    window,
    textvariable=labelText1,
    width=25,
    bg="#c8abba",
    font=("Helvetica", 18, "bold"),
    height=2,
)
labelDir.pack(side=TOP, fill="x")
user_input = Entry(
    window,
    font=("Helvetica", 24, "bold"),
    borderwidth=0,
)
name = user_input.get()
user_input.pack(side=TOP, fill="x")
user_input.focus_set()
endSplash = Button(
    window,
    text="Play Game",
    highlightbackground="black",
    height=2,
    bg="#c8abba",
    font=("Helvetica", 18, "bold"),
    command=first_level,
    width=25,
)
endSplash.pack(side=TOP, fill="x")
endSplash = Button(
    window,
    text="How to Play",
    highlightbackground="black",
    height=2,
    bg="#c8abba",
    font=("Helvetica", 18, "bold"),
    command=Instructions,
    width=25,
)
endSplash.pack(side=TOP, fill="x")
endSplash = Button(
    window,
    text="Choose Controls",
    highlightbackground="black",
    height=2,
    bg="#c8abba",
    font=("Helvetica", 18, "bold"),
    command=controls,
    width=25,
)
endSplash.pack(side=TOP, fill="x")
endSplash = Button(
    window,
    text="Load Game",
    highlightbackground="black",
    height=2,
    bg="#c8abba",
    font=("Helvetica", 18, "bold"),
    command=load_game,
    width=25,
)
endSplash.pack(side=TOP, fill="x")
endSplash = Button(
    window,
    text="Quit Game",
    highlightbackground="black",
    height=2,
    bg="#c8abba",
    font=("Helvetica", 18, "bold"),
    command=quit_game,
    width=25,
)
endSplash.pack(side=TOP, fill="x")
window.resizable(False, False)
window.mainloop()
