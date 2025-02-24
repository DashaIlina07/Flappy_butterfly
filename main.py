import pygame
import sys
import random


class Button:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None,
                 sound_path=None, text_color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color

        self.image = pygame.image.load(f"{image_path}")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(f"{hover_image_path}")
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(f"{sound_path}")
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))

pygame.init()
width, height = 1366, 768
fps = 60
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flappy Animals')

main_sound = pygame.mixer.Sound("Feel-Good(chosic.com).mp3")
bg_sound = pygame.mixer.Sound("level1.mp3")
main_music, bg_music = True, True
main_note, bg_note = True, True
clock = pygame.time.Clock()

difficulty = "Легко"
selected_character = "Птица"
score = 0

player_images = {
    "Птица": [pygame.image.load("птицы 1.png"), pygame.image.load("птицы 2.png"),
              pygame.image.load("птицы 3.png"), pygame.image.load("птицы death.png")],
    "Бабочка": [pygame.image.load("бабочки 1.png"), pygame.image.load("бабочки 2.png"),
                pygame.image.load("бабочки 3.png"), pygame.image.load("бабочки death.png")],
    "Пчела": [pygame.image.load("пчелы1.png"), pygame.image.load("пчелы 2.png"),
              pygame.image.load("пчелы 3.png"), pygame.image.load("пчелы dead.png")]
}
obstacle_image = pygame.image.load("obstacle.png")

def save_result_to_txt(player_name, score, difficulty, character):
    """Сохраняет результаты игры в txt файл."""
    try:
        with open("results.txt", "a", encoding='utf-8') as f:
            f.write(f"Имя игрока: {player_name}, Счет: {score}, Сложность: {difficulty}, Персонаж: {character}\n")
        print("Результаты сохранены в results.txt")
    except Exception as e:
        print(f"Ошибка при сохранении результатов: {e}")


def main_meno():
    global main_music, bg_music, main_note, bg_note
    if main_note or bg_note:
        sound_path = "click.mp3"
    else:
        sound_path = ""
    start_button = Button(380, 400, 650, 150, "", "play.png",
                          "play_hover.png", sound_path)
    quit_button = Button(380, 600, 650, 150, "", "quit.png",
                         "quit_hover.png", sound_path)
    options_button = Button(1200, 40, 150, 150, "", "settings.png",
                            "settings.png", sound_path)
    running = True
    if main_music and not pygame.mixer.get_busy():
        main_sound.play(-1)

    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load("background.jpg"), (0, 0))

        image = pygame.image.load("f-no-bg-preview (carve.photos)_N.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (40, 40))
        image = pygame.image.load("L-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (100, 40))
        image = pygame.image.load("a-fotor-bg-remover-2025021222143.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (160, 40))
        image = pygame.image.load("P-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (220, 40))
        image = pygame.image.load("P-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (280, 40))
        image = pygame.image.load("Y-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (340, 40))
        image = pygame.image.load("a-fotor-bg-remover-2025021222143.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (160, 140))
        image = pygame.image.load("n.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (220, 140))
        image = pygame.image.load("i-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (280, 140))
        image = pygame.image.load("m.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (340, 140))
        image = pygame.image.load("a-fotor-bg-remover-2025021222143.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (400, 140))
        image = pygame.image.load("L-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (460, 140))
        image = pygame.image.load("s.png").convert_alpha()
        new_image = pygame.transform.scale(image, (60, 100))
        screen.blit(new_image, (520, 140))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                character_select_meno()
            elif event.type == pygame.USEREVENT and event.button == quit_button:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.USEREVENT and event.button == options_button:
                setting_meno()

            start_button.handle_event(event)
            options_button.handle_event(event)
            quit_button.handle_event(event)

        start_button.check_hover(pygame.mouse.get_pos())
        options_button.check_hover(pygame.mouse.get_pos())
        quit_button.check_hover(pygame.mouse.get_pos())
        start_button.draw(screen)
        options_button.draw(screen)
        quit_button.draw(screen)
        pygame.display.flip()

def dead(score):
    global main_music, bg_music, main_note, bg_note
    if main_note or bg_note:
        sound_path = "click.mp3"
    else:
        sound_path = ""
    setting_button = Button(10, 40, 150, 150, "", "settings.png",
                          "settings.png", sound_path)
    meno_button = Button(1200, 40, 150, 150, "", "дом-edited-free (carve,photos)_enhanced.png",
                         "дом-edited-free (carve,photos)_enhanced.png", sound_path)
    retr_button = Button(550, 480, 250, 250, "", "back.png",
                            "back.png", "")

    running = True
    if main_music and not pygame.mixer.get_busy():
        main_sound.play(-1)

    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load("background.jpg"), (0, 0))
        image = pygame.image.load("f-no-bg-preview (carve.photos)_N.png").convert_alpha()
        new_image = pygame.transform.scale(image, (100, 140))
        screen.blit(new_image, (340, 150))
        image = pygame.image.load("L-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (100, 140))
        screen.blit(new_image, (640, 150))
        image = pygame.image.load("a-fotor-bg-remover-2025021222143.png").convert_alpha()
        new_image = pygame.transform.scale(image, (100, 140))
        screen.blit(new_image, (440, 150))
        image = pygame.image.load("e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (100, 140))
        screen.blit(new_image, (740, 150))
        image = pygame.image.load("i-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (100, 140))
        screen.blit(new_image, (540, 150))
        image = pygame.image.load("d-no-bg-preview (carve,photos)_e.png").convert_alpha()
        new_image = pygame.transform.scale(image, (100, 140))
        screen.blit(new_image, (840, 150))
        font = pygame.font.Font(None, 60)
        difficulty_text = font.render(f"Score:        {score}", True, (0, 0, 0))
        screen.blit(difficulty_text, (450, 360))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == setting_button:
                setting_meno()
            elif event.type == pygame.USEREVENT and event.button == meno_button:
                main_meno()
            elif event.type == pygame.USEREVENT and event.button == retr_button:
                character_select_meno()

            setting_button.handle_event(event)
            meno_button.handle_event(event)
            retr_button.handle_event(event)

        setting_button.check_hover(pygame.mouse.get_pos())
        meno_button.check_hover(pygame.mouse.get_pos())
        retr_button.check_hover(pygame.mouse.get_pos())
        setting_button.draw(screen)
        meno_button.draw(screen)
        retr_button.draw(screen)
        pygame.display.flip()


    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load("background.jpg"), (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        pygame.display.flip()

def setting_meno():
    global main_music, bg_music, main_note, bg_note
    if main_note or bg_note:
        sound_path = "click.mp3"
    else:
        sound_path = ""
    left_button = Button(100, 530, 180, 180, "",
                         "back.png",
                         "back.png",
                         "")
    music_button = Button(350, 250, 300, 200, "Music: On" if main_music else "Music: Off",
                          "музыка-edited-free (carve,photos)_enhanced.png",
                          "музыка-edited-free (carve,photos)_enhanced.png",
                          sound_path, text_color=(0,0,0))
    note_button = Button(700, 250, 300, 200, "Sound: On" if main_note else "Sound: Off" ,
                            "звук.png",
                            "звук.png",
                            sound_path, text_color=(0,0,0))

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load("background.jpg"), (-300, 0))
        # image = pygame.image.load("assets/подкнопки в настройках.png").convert_alpha()
        # new_image = pygame.transform.scale(image, (1000, 600))
        # screen.blit(new_image, (200, 50))
        font = pygame.font.SysFont('bookworm', 80)
        text = font.render("Settings", True, (0, 0, 0))
        screen.blit(text, (550, 155))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == left_button:
               main_meno()

            if event.type == pygame.USEREVENT and event.button == music_button:
                music_button.text = "Music: Off" if main_music else "Music: On"
                if main_music == True or bg_music == True:
                    main_sound.stop()
                    main_music, bg_music = False, False
                else:
                    main_sound.play()
                    main_music, bg_music = True, True
                    
            if event.type == pygame.USEREVENT and event.button == note_button:
                note_button.text = "Sound: Off" if main_note else "Sound: On"
                if main_note == True or bg_note == True:
                    main_note, bg_note = False, False
                else:
                    main_note, bg_note = True, True

            left_button.handle_event(event)
            music_button.handle_event(event)
            note_button.handle_event(event)

        music_button.check_hover(pygame.mouse.get_pos())
        note_button.check_hover(pygame.mouse.get_pos())
        left_button.check_hover(pygame.mouse.get_pos())
        music_button.draw(screen)
        note_button.draw(screen)
        left_button.draw(screen)
        pygame.display.flip()


def character_select_meno():
    global difficulty, selected_character
    sound_path = "click.mp3"
    if main_note == False or bg_note == False:
        sound_path = ""
    left_button = Button(100, 530, 180, 180, "",
                         "back.png",
                         "back.png",
                         "")

    difficulty_easy_button = Button(400, 200, 200, 70, "",
                                    "level1.png", "level1.png", sound_path, text_color=(0,0,0))
    difficulty_medium_button = Button(400, 300, 200, 70, "", "level2.png",
                                      "level2.png", sound_path, text_color=(0,0,0))
    difficulty_hard_button = Button(400, 400, 200, 70, "", "level3.png", "level3.png",
                                    sound_path, text_color=(0,0,0))

    character_butterfly_button = Button(700, 200, 120, 80, "", "бабочки 1.png", "бабочки 2.png",
                                        sound_path, text_color=(0,0,0))
    character_bee_button = Button(700, 300, 120, 80, "", "пчелы1.png", "пчелы 2.png", sound_path,
                                  text_color=(0,0,0))
    character_bird_button = Button(700, 400, 120, 80, "", "птицы 1.png", "птицы 2.png", sound_path,
                                   text_color=(0,0,0))

    start_level_button = Button(width // 2 - 150, 600, 300, 100, "", "play.png",
                                "play_hover.png", sound_path)
    running = True
    
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load("background.jpg"), (-300, 0))

        font = pygame.font.Font(None, 28)
        difficulty_text = font.render("Choose the difficulty:", True, (0, 0, 0))
        screen.blit(difficulty_text, (350, 100))
        character_text = font.render("Choose a character:", True, (0, 0, 0))
        screen.blit(character_text, (650, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT:
                if event.button == left_button:
                    running = False
                elif event.button == difficulty_easy_button:
                    difficulty = "Легко"
                    print(f"Сложность выбрана: {difficulty}")
                elif event.button == difficulty_medium_button:
                    difficulty = "Средне"
                    print(f"Сложность выбрана: {difficulty}")
                elif event.button == difficulty_hard_button:
                    difficulty = "Сложно"
                    print(f"Сложность выбрана: {difficulty}")
                elif event.button == character_butterfly_button:
                    selected_character = "Бабочка"
                    print(f"Персонаж выбран: {selected_character}")
                elif event.button == character_bee_button:
                    selected_character = "Пчела"
                    print(f"Персонаж выбран: {selected_character}")
                elif event.button == character_bird_button:
                    selected_character = "Птица"
                    print(f"Персонаж выбран: {selected_character}")
                elif event.button == start_level_button:
                    if difficulty == "Легко":
                        level_1()
                    elif difficulty == "Средне":
                        level_2()
                    elif difficulty == "Сложно":
                        level_3()
                    running = False


            left_button.handle_event(event)
            difficulty_easy_button.handle_event(event)
            difficulty_medium_button.handle_event(event)
            difficulty_hard_button.handle_event(event)
            character_butterfly_button.handle_event(event)
            character_bee_button.handle_event(event)
            character_bird_button.handle_event(event)
            start_level_button.handle_event(event)


        left_button.check_hover(pygame.mouse.get_pos())
        left_button.draw(screen)

        difficulty_easy_button.check_hover(pygame.mouse.get_pos())
        difficulty_easy_button.draw(screen)
        difficulty_medium_button.check_hover(pygame.mouse.get_pos())
        difficulty_medium_button.draw(screen)
        difficulty_hard_button.check_hover(pygame.mouse.get_pos())
        difficulty_hard_button.draw(screen)

        character_butterfly_button.check_hover(pygame.mouse.get_pos())
        character_butterfly_button.draw(screen)
        character_bee_button.check_hover(pygame.mouse.get_pos())
        character_bee_button.draw(screen)
        character_bird_button.check_hover(pygame.mouse.get_pos())
        character_bird_button.draw(screen)

        start_level_button.check_hover(pygame.mouse.get_pos())
        start_level_button.draw(screen)

        pygame.display.flip()


class Level:
    def __init__(self, level_number, screen, width, height, player_images, obstacle_image,
                 main_sound, bg_sound, difficulty, selected_character, bg_music, save_result_to_txt,
                 main_meno, dead, main_note, bg_note, score):
        self.level_number = level_number
        self.screen = screen
        self.width = width
        self.height = height
        self.player_images = player_images
        self.obstacle_image = obstacle_image
        self.main_sound = main_sound
        self.bg_sound = bg_sound
        self.difficulty = difficulty
        self.selected_character = selected_character
        self.bg_music = bg_music
        self.save_result_to_txt = save_result_to_txt
        self.main_meno = main_meno
        self.dead = dead
        self.main_note = main_note
        self.bg_note = bg_note

        self.bg_x = 0
        self.player_y = height // 4
        self.player_x = 100
        self.player_speed_y = 0
        self.gravity = 0.015
        self.obstacle_width = 80
        self.obstacle_image_scaled = pygame.transform.scale(obstacle_image, (self.obstacle_width, obstacle_image.get_height()))
        self.obstacle_height = self.obstacle_image_scaled.get_height()
        self.obstacle_passed = False
        self.score = score
        self.player_height = 64
        self.player_width = 64
        self.min_obstacle_height = 80
        self.obstacle_horizontal_spacing = -500
        self.max_obstacle_height = height - 250 - self.min_obstacle_height - 100 # Default obstacle_gap
        self.conflict = [
                    pygame.image.load("взрыв1.png"),
                    pygame.image.load("взрыв2.png"),
                    pygame.image.load("взрыв2.5.png"),
                    pygame.image.load("взрыв3.png"),
                    pygame.image.load("взрыв4.png"),
                    pygame.image.load("взрыв5.png"),
                    pygame.image.load("взрыв6.png"),
                    pygame.image.load("взрыв7.png"),
                    pygame.image.load("взрыв8.png"),
                ]
        self.clock = pygame.time.Clock()

        if self.bg_music:
            self.main_sound.stop()
            self.bg_sound.play(-1)

        self.fon = pygame.image.load('level1_background.png') # Assuming same background for all levels
        self.player_images = player_images[selected_character]
        self.player_image = pygame.transform.scale(self.player_images[2], (self.player_width, self.player_height))
        self.obstacle_x = width

        self.obstacle_upper_rect = self.obstacle_image_scaled.get_rect(topleft=(self.obstacle_x, 0))
        self.obstacle_lower_rect = self.obstacle_image_scaled.get_rect() # Position will be set in run method
        self.name = self.player_images[2]
        self.t = 0


    def initialize_level_parameters(self):
        if self.level_number == 1:
            self.obstacle_speed = 1
            self.obstacle_gap = 250
        elif self.level_number == 2:
            self.obstacle_speed = 2
            self.obstacle_gap = 200
        elif self.level_number == 3:
            self.obstacle_speed = 3
            self.obstacle_gap = 150

        self.max_obstacle_height = self.height - self.obstacle_gap - self.min_obstacle_height - 100

    def reset_obstacle_position(self):
        self.obstacle_x = self.width
        upper_obstacle_height = random.randint(self.min_obstacle_height, self.max_obstacle_height)
        lower_obstacle_height = self.height - upper_obstacle_height - self.obstacle_gap

        self.obstacle_upper_rect.height = upper_obstacle_height
        self.obstacle_lower_rect.height = lower_obstacle_height
        self.obstacle_lower_rect.top = self.obstacle_upper_rect.bottom + self.obstacle_gap


    def run(self):
        self.initialize_level_parameters()
        self.reset_obstacle_position()
        running = True
        while running:
            self.t += 1
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.fon, (self.bg_x, 0))
            self.screen.blit(self.fon, (self.bg_x + 1900, 0))

            self.bg_x = 0 # Background is static in provided code
            if self.bg_x == -1900:
                self.bg_x = 0

            if self.name == self.player_images[0] and self.t > 30:
                self.player_image = pygame.transform.scale(self.player_images[2],
                                                           (self.player_width, self.player_height))
                self.name = self.player_images[2]
            elif self.name == self.player_images[0] and self.t > 15:
                self.player_image = pygame.transform.scale(self.player_images[1],
                                                           (self.player_width, self.player_height))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player_speed_y = -1.1
                        self.player_image = pygame.transform.scale(self.player_images[0],
                                                                   (self.player_width, self.player_height))
                        self.name = self.player_images[0]
                        self.t = 0
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        self.main_meno() # Call main_meno from the class instance
                    if event.key == pygame.K_s:
                        self.save_result_to_txt("Игрок", self.score, self.difficulty, self.selected_character) # Call save_result_to_txt


            self.player_speed_y += self.gravity
            self.player_y += self.player_speed_y

            if self.player_y < 0 or self.player_y > self.height - self.player_height:
                print("Столкновение с верхом или низом!")
                self.bg_sound.stop()
                if main_note or bg_note:
                    colid = pygame.mixer.Sound("звук падения.mp3")
                    colid.play(-1)
                for i in self.conflict:
                    self.screen.fill((0, 0, 0))
                    self.screen.blit(self.fon, (self.bg_x, 0))
                    self.screen.blit(self.fon, (self.bg_x + 1900, 0))
                    image = pygame.transform.scale(self.player_images[3],
                                                                   (self.player_width, self.player_height))
                    self.screen.blit(image, (self.player_x, self.player_y))

                    self.bg_x = 0  # Background is static in provided code
                    if self.bg_x == -1900:
                        self.bg_x = 0
                    new_image = pygame.transform.scale(i, (150, 120))
                    screen.blit(new_image, (self.player_x, self.player_y))
                    pygame.display.flip()
                    clock.tick(20)
                if main_note or bg_note:
                    colid.stop()
                self.save_result_to_txt("Игрок", self.score, self.difficulty, self.selected_character)
                running = False
                self.dead(self.score)

            self.obstacle_x -= self.obstacle_speed
            self.obstacle_upper_rect.x = self.obstacle_x
            self.obstacle_lower_rect.x = self.obstacle_x


            if self.obstacle_x < -self.obstacle_width:
                self.reset_obstacle_position()
                self.obstacle_passed = False

            player_rect = self.player_image.get_rect(topleft=(self.player_x, self.player_y))
            if player_rect.colliderect(self.obstacle_upper_rect) or player_rect.colliderect(self.obstacle_lower_rect):
                self.bg_sound.stop()
                if main_note or bg_note:
                    colid = pygame.mixer.Sound("звук падения.mp3")
                    colid.play(-1)
                for i in self.conflict:
                    self.screen.fill((0, 0, 0))
                    self.screen.blit(self.fon, (self.bg_x, 0))
                    self.screen.blit(self.fon, (self.bg_x + 1900, 0))
                    image = pygame.transform.scale(self.player_images[3],
                                                   (self.player_width, self.player_height))
                    self.screen.blit(image, (self.player_x, self.player_y))

                    self.bg_x = 0  # Background is static in provided code
                    if self.bg_x == -1900:
                        self.bg_x = 0
                    new_image = pygame.transform.scale(i, (150, 120))
                    screen.blit(new_image, (self.player_x, self.player_y))
                    pygame.display.flip()
                    clock.tick(20)
                if main_note or bg_note:
                    colid.stop()
                self.save_result_to_txt("Игрок", self.score, self.difficulty, self.selected_character)
                running = False
                self.dead(self.score)

            if self.obstacle_x + self.obstacle_width < self.player_x and not self.obstacle_passed:
                self.score += 1
                self.obstacle_passed = True
                print(f"Счет: {self.score}")

            self.screen.blit(self.player_image, (self.player_x, self.player_y))

            scaled_upper_obstacle = pygame.transform.scale(self.obstacle_image, (self.obstacle_width, self.obstacle_upper_rect.height))
            scaled_upper_obstacle_flipped = pygame.transform.flip(scaled_upper_obstacle, False, True)
            self.screen.blit(scaled_upper_obstacle_flipped, self.obstacle_upper_rect)

            scaled_lower_obstacle = pygame.transform.scale(self.obstacle_image, (self.obstacle_width, self.obstacle_lower_rect.height))
            self.screen.blit(scaled_lower_obstacle, self.obstacle_lower_rect)

            font = pygame.font.Font(None, 60)
            score_text = font.render(f"Score:          {self.score}", True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()


def run_level(level_num):
    global screen, width, height, player_images, obstacle_image, main_sound, bg_sound,
    difficulty, selected_character, bg_music, save_result_to_txt, main_meno, dead, main_note, bg_note, score
    level_instance = Level(level_num, screen, width, height, player_images, obstacle_image, main_sound, bg_sound,
                           difficulty, selected_character, bg_music, save_result_to_txt,
                           main_meno, dead, main_note, bg_note, score)
    level_instance.run()

def level_1():
    run_level(1)

def level_2():
    run_level(2)

def level_3():
    run_level(3)


if __name__ == "__main__":
    main_meno()
