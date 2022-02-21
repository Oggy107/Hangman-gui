import pygame
import Engine
import colorama
import os
import webbrowser

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 450
BGCOLOR = (77, 171, 14)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DEBUG = False
FPS = 20

def search(query):
    url = "https://www.google.com/search?q=" + query
    chromePath = "C:\\Program File\\Google\\Chrome\\Application\\chrome.exe"

    if os.path.exists(chromePath):
        webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chromePath), preferred = True)
    else:
        chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chromePath):
            webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chromePath), preferred = True)
        else:
            pass

    controller = webbrowser.get()
    controller.open(url)

class wordSection:
    _WORDSECTION_WINDOW_WIDTH = WINDOW_WIDTH // 2
    _WORDSECIION_WINDOW_HEIGHT = WINDOW_HEIGHT

    def __init__(self):
        self.showDescription()
        self.showQues()
        self.showRemainingLetters(start.engine.getQues().count('-'))
        self.showInstruction()

    def showDescription(self):

        welcome_font = pygame.font.Font("freesansbold.ttf", 25)
        welcome = welcome_font.render("Welcome", True, WHITE)
        welcome_rect = welcome.get_rect()

        welcome_rect.center = wordSection._WORDSECTION_WINDOW_WIDTH // 2, 35

        game._mainSurface.blit(welcome, welcome_rect)

        desc_font = pygame.font.Font("freesansbold.ttf", 15)
        desc = desc_font.render("Guess the letters from the given", True, WHITE)
        desc_rect = desc.get_rect()

        desc_rect.center = wordSection._WORDSECTION_WINDOW_WIDTH // 2, 75

        game._mainSurface.blit(desc, desc_rect)

        desc2_font = pygame.font.Font("freesansbold.ttf", 15)
        desc2 = desc2_font.render("word before the man hangs", True, WHITE)
        desc2_rect = desc2.get_rect()

        desc2_rect.center = wordSection._WORDSECTION_WINDOW_WIDTH // 2, 95

        game._mainSurface.blit(desc2, desc2_rect)

    def showInstruction(self):
        font = pygame.font.Font("freesansbold.ttf", 21)
        text = font.render("Press Enter to restart", True, WHITE)
        text_rect = text.get_rect()

        text_rect.center = wordSection._WORDSECTION_WINDOW_WIDTH // 2, wordSection._WORDSECIION_WINDOW_HEIGHT - 30

        game._mainSurface.blit(text, text_rect)

    def showQues(self, reset = False):
        font = pygame.font.Font("freesansbold.ttf", 25)
        text = font.render(start.engine.getQues(), True, WHITE)
        text_rect = text.get_rect()

        text_rect.center = wordSection._WORDSECTION_WINDOW_WIDTH // 2, wordSection._WORDSECIION_WINDOW_HEIGHT // 2

        if reset:
            self.resetText(text_rect)

        game._mainSurface.blit(text, text_rect)

    def showRemainingLetters(self, value):
        font = pygame.font.Font("freesansbold.ttf", 21)
        text = font.render(f"  {value} letters to go  ", True, WHITE)
        text_rect = text.get_rect()

        text_rect.center = wordSection._WORDSECTION_WINDOW_WIDTH // 2, 135

        self.resetText(text_rect)

        game._mainSurface.blit(text, text_rect)

    def showAns(self):
        ans = start.engine.getAns()

        font = pygame.font.Font("freesansbold.ttf", 18)
        text = font.render(f"The answer was {ans}", True, WHITE)
        text_rect = text.get_rect()

        text_rect.center = wordSection._WORDSECTION_WINDOW_WIDTH // 2, wordSection._WORDSECIION_WINDOW_HEIGHT - 75

        game._mainSurface.blit(text, text_rect)

    def showStatus(self, status):
        font = pygame.font.Font("freesansbold.ttf", 25)

        if status == "right":
            text = font.render("      Nice Job      ", True, WHITE)

        elif status == "wrong":
            text = font.render("Ops! Try Again", True, WHITE)
            
        elif status == "won":
            text = font.render("      You Won        ", True, WHITE)

        elif status == "lost":
            text = font.render("      You Lost       ", True, WHITE)

        text_rect = text.get_rect()
        text_rect.center = wordSection._WORDSECTION_WINDOW_WIDTH // 2, wordSection._WORDSECIION_WINDOW_HEIGHT - 125

        self.resetText(text_rect)

        game._mainSurface.blit(text, text_rect)               

    def resetText(self, rect):
        game._mainSurface.fill(BGCOLOR, rect)
        pygame.display.update(rect)

class hangmanSection:
    def __init__(self):
        self.drawStand()

    def drawStand(self):
        start_pos_poll = WINDOW_WIDTH - 60, 30
        end_pos_poll = WINDOW_WIDTH - 60, WINDOW_HEIGHT - 80
        pygame.draw.line(game._mainSurface, WHITE, start_pos_poll, end_pos_poll, 4)

        start_pos_bottom = start_pos_poll[0] - 25, end_pos_poll[1]
        end_pos_bottom = start_pos_poll[0] + 25, end_pos_poll[1]
        pygame.draw.line(game._mainSurface, WHITE, start_pos_bottom, end_pos_bottom, 6)

        start_pos_arm = start_pos_poll[0] - 100, start_pos_poll[1]
        end_pos_arm = start_pos_poll[0], start_pos_poll[1]
        pygame.draw.line(game._mainSurface, WHITE, start_pos_arm, end_pos_arm, 4)

        start_pos_head = start_pos_arm[0], start_pos_arm[1]
        end_pos_head = start_pos_arm[0], start_pos_arm[1] + 70
        pygame.draw.line(game._mainSurface, WHITE, start_pos_head, end_pos_head, 4)

    def drawBodypart(self):
        retries = start.engine.getRetries()
        
        if retries == 5:
            pygame.draw.circle(game._mainSurface, WHITE, (341, 115), 14)               #Head
        elif retries == 4:
            pygame.draw.line(game._mainSurface, WHITE, (341, 115), (341, 250), 2)      #Body
        elif retries == 3:
            pygame.draw.line(game._mainSurface, WHITE, (341, 150), (300, 170), 2)      #LeftArm
        elif retries == 2:
            pygame.draw.line(game._mainSurface, WHITE, (341, 150), (382, 170), 2)      #RightArm
        elif retries == 1:
            pygame.draw.line(game._mainSurface, WHITE, (341, 250), (300, 270), 2)      #LeftLeg
        elif retries == 0:
            pygame.draw.line(game._mainSurface, WHITE, (341, 250), (382, 270), 2)      #RightLeg

    @staticmethod
    def showHowToquery():
        font = pygame.font.Font("freesansbold.ttf", 16)
        text = font.render("Press shift to search word", True, WHITE)
        text_rect = text.get_rect()

        text_rect.center = 375, 420

        game._mainSurface.blit(text, text_rect)
        
class game:
    _mainSurface = None
    DEBUG = False

    def __init__(self, debug = False):
        game._mainSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        game._mainSurface.fill(BGCOLOR)

        pygame.display.set_caption("Hang Man")
        icon = pygame.image.load("resources/icon.png")
        pygame.display.set_icon(icon)
        
        self.makeSection()
        self.clock = pygame.time.Clock()

        if debug:
            colorama.init(autoreset = True)
            os.system("cls")
            game.DEBUG = True

            print("\n \033[31;42m#####      DEBUG MODE      #####\n")
            print(f"{colorama.Cursor.POS(1, 16)} \033[31;1mYour guess                \033[32mNULL")

        #game.bgMusic()

    def init(self):
        self.engine = Engine.engine()
        self.word_section = wordSection()
        self.hangman_section = hangmanSection()

    @staticmethod
    def bgMusic():
        pygame.mixer.music.load("resources/bg_music.mp3")
        pygame.mixer.music.play()

    @staticmethod
    def sound(src):
        sound = pygame.mixer.Sound(src)
        pygame.mixer.Sound.play(sound)

    def makeSection(self):
        start_pos = WINDOW_WIDTH // 2, 0
        end_pos = WINDOW_WIDTH // 2, WINDOW_HEIGHT

        pygame.draw.line(game._mainSurface, WHITE, start_pos, end_pos, 2)

    def reset(self):
        del self.engine
        del self.word_section
        del self.hangman_section

        game._mainSurface.fill(BGCOLOR)

        self.makeSection()

        self.engine = Engine.engine()
        self.word_section = wordSection()
        self.hangman_section = hangmanSection()

    def showDebugData(self, won = False, lost = False):
        print(f"{colorama.Cursor.POS(1, 4)} \033[91;1mFps                       \033[32m{self.clock.get_fps()}")
        print(f"{colorama.Cursor.POS(1, 6)} \033[91;1mMouse postion             \033[32m{pygame.mouse.get_pos()}    ")
        print(f"{colorama.Cursor.POS(1, 18)} \033[31;1mRetries left              \033[32m{self.engine.getRetries()}")
        print(f"{colorama.Cursor.POS(1, 20)} \033[31;1mWon                       \033[32m{won}")
        print(f"{colorama.Cursor.POS(1, 22)} \033[31;1mLost                      \033[32m{lost}")

    def run(self):
        running = True
        lost = False
        won = False

        while running:
            pygame.display.flip()
            
            events = pygame.event.get()
            self.clock.tick(FPS)

            if game.DEBUG:
                self.showDebugData()

            for event in events:
                #print(pygame.event.event_name(event.type))
                if game.DEBUG:
                    print(f"{colorama.Cursor.POS(1, 8)} \033[91;1mCurrent Event             \033[32m{pygame.event.event_name(event.type)}           ")
                    print(f"{colorama.Cursor.POS(1, 10)} \033[91;1mQuestion                  \033[32m{self.engine.getQues()}")
                    print(f"{colorama.Cursor.POS(1, 12)} \033[91;1mAnwer                     \033[32m{self.engine.getAns()}")
                    print(f"{colorama.Cursor.POS(1, 14)} \033[91;1mAnsDic                    \033[32m{self.engine.getAnsDic()}                    ")

                if event.type == pygame.QUIT:
                    if game.DEBUG:
                        print('\n\n\n\n\n\n\n')

                    running = False

                elif event.type == pygame.KEYDOWN:
                    if lost:
                        if event.key == pygame.K_LSHIFT:
                            search(self.engine.getAns())

                    if event.key == pygame.K_RETURN:
                        won = False
                        lost = False
                        self.reset()

                    elif not won and not lost:
                        guess = event.unicode

                        if guess:
                            status = self.engine.evaluate(guess)

                            if status == "won":
                                if game.DEBUG:
                                    self.showDebugData(lost = True)

                                won = True

                            if status == "right":
                                game.sound("resources/correct.mp3")

                            if status == "wrong":
                                game.sound("resources/wrong.mp3")

                            self.word_section.showQues(True)
                            self.word_section.showStatus(status)
                            self.word_section.showRemainingLetters(self.engine.getQues().count('-'))
                            self.hangman_section.drawBodypart()
                            
                            if game.DEBUG:
                                print(f"{colorama.Cursor.POS(1, 16)} \033[31;1mYour guess                \033[32m{guess}    ")

                        if won:
                            #pygame.mixer.music.unload()
                            game.sound("resources/win.mp3")

                        elif not self.engine.getRetries():
                            status = "lost"
                            self.word_section.showStatus(status)
                            self.word_section.showAns()
                            hangmanSection.showHowToquery()
                            #pygame.mixer.music.unload()
                            game.sound("resources/lost.mp3")

                            if game.DEBUG:
                                self.showDebugData(lost = True)
                            lost = True
                            
if __name__ == "__main__":
    pygame.init()
    start = game()
    start.init()
    start.run()