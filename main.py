import pi, keyboard, os, pygame, sys
from playsound import playsound

#timer

#PYGAME INIT
pygame.init()
with open('startdigit.txt') as f: 
    starting = int(f.read())

#assets
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 64])
base_font = pygame.font.Font(None, 32)
input_rect = pygame.Rect(0, 0, 600, 32)
score_rect = pygame.Rect(0, 32, 600, 64)
color2 = pygame.Color('green')
color = pygame.Color('black')
pi_array = [char for char in pi.value]
jumpscare = pygame.mixer.Sound("sound.mp3")

#startup
user_text = '3.'
num = starting
error = 0 
deno = len(pi.value)
n = 0
for x in range(num):
    user_text += pi_array[x]

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE or event.key == 113:
                pygame.quit()
                sys.exit()
            elif event.key == 114:
                for x in range(5): print(pi_array[num+x], end='')
                print()
                #startup
                user_text = '3.'
                num = starting
                error = 0 
                deno = len(pi.value)
                n = 0
                for x in range(num):
                    user_text += pi_array[x]
            elif event.key >=48 and event.key <=57:
                if event.key == ord(pi_array[num]):
                    num+=1
                    user_text += event.unicode
                else:
                    jumpscare.play()
                    error+=1

      
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, color, input_rect)
    pygame.draw.rect(screen, color, score_rect)

    text_surface = base_font.render(user_text, True, (255, 255, 255))

    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

    screen.blit(base_font.render(f'SCORE: {num}', True, (255,0,0)), (10, 38))
    screen.blit(base_font.render(f'ERRORS: {error}', True, (255,0,0)), (300, 38))


    input_rect.w = max(100, text_surface.get_width()+10)
    input_rect.x = -1*max(100, text_surface.get_width())+590

    pygame.display.flip()

    clock.tick(60)

# while True:
#     event = keyboard.read_event()
#     if event.event_type == keyboard.KEY_DOWN:
#         key = event.name
#         if key == 'q':
#             break
#         if key == pi_array[num]:
#             print(pi_array[num])
#             num+=1
#         elif ord(key) >=48 and ord(key) <=57:
#             error+=1
#             playsound('sound.mp3')
#             #os.system("start Chrome.exe \"https://youtu.be/MpC4v4CecBA\"")


# if num > 499:
#     print("Only Jessie")
# elif num > 199:
#     print("Go get some bitches!")
# elif num > 99:
#     print("GRR!")
# else:
#     print(f'Only {num}! I have seen better!')

# print(f'Score: {num}\tErrors: {error}')