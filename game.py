#%% Libraries 

import pygame
import nltk
nltk.download('words')

from nltk.corpus import words
from random import randrange

#%%%

def drawing(wrong):
    
    pos=[[(250,300), (250,400)],[(250,350), (300,380)], #human
         [(250,350), (200,380)],[(250,350), (200,380)], #human
         [(250,400), (300,450)],[(250,400), (200,450)], #human
         [(100,500), (350,500)],[(150,500), (150,200)], #gallows
         [(100,500), (150,450)],[(200,500), (150,450)], #gallows
         [(200,200), (150,250)],[(100,200), (300,200)], #gallows
         [(250,270), (250,200)]]                        #gallows   
        
    for i in range(len(wrong)):
        if i<7:
            color="purple"
        else:
            color="brown"
            
        if i==0:
            color="purple"
            pygame.draw.circle(screen, color, (250,300), 30)
        else:
            pygame.draw.line(screen, color, pos[i-1][0], pos[i-1][1], 3)
           

def check_letter(word):
    show =""
    for letter in word:
        letter = letter.lower()
        if letter in letters:
            show += letter
        else:
            show += "_ "
    
    guessed = font.render(show, True, "black")
    text_rect = guessed.get_rect(center=(250, 100))
    pygame.draw.rect(screen, "white", pygame.Rect(20, 65, 460, 70))
    screen.blit(guessed,text_rect)     
            
    return show
            
def guess(word, letter):
    letter = letter.lower()
    if len(letter)!=1 or letter.isalpha()==False:
        letter = letter + " is not a letter..."
        color="orange"
    elif letter in letters:
        print(letter + " already guessed!")
        color="yellow"
    else:
        letters.append(letter)
        color="green"
        if letter not in word:
            wrong.append(letter)
            color="red"
        check_letter(word)
    
    pygame.draw.rect(screen, "white", pygame.Rect(200, 620, 100, 50))
    text_surface = font.render(letter, True, color)
    text_rect = text_surface.get_rect(center=(250, 640))
    screen.blit(text_surface, text_rect)

def show_alphabet():
    alphabet = ['a','b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    color_font = ["black", "blue", "red"]
    images = []
    for letter in alphabet:
        if letter in letters:
            if letter in wrong:
                color = color_font[2]
            else:
                color = color_font[1]
        else:
            color = color_font[0]
        s_image = font.render(letter, True, color)
        images.append(s_image)
    
    
    for index, image in enumerate(images):
        if index < len(images)/2:
            image_rect = image.get_rect(center=(40 + index*35, 560))
        else:
            image_rect = image.get_rect(center=(40 + (index-len(images)/2)*35 ,600))
        screen.blit(image,image_rect)


def new_game():
    
    word_list = words.words()
    word = word_list[randrange(0, len(word_list), 1)]
    check_letter(word)
    show_alphabet()
    return word



#%%

pygame.init()
screen = pygame.display.set_mode((500,720))
font = pygame.font.Font(pygame.font.get_default_font(), 36)
running = True
game_over = False


letters=[]
wrong=[]
word = new_game()

letter = ""
screen.fill("light blue")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        check_letter(word)
        show_alphabet()
        if event.type ==pygame.KEYDOWN:
            if game_over==False:
                letter = str(event.unicode)
                guess(word, letter)
                drawing(wrong)
                show_alphabet()
                guessed = check_letter(word)
                if guessed == word:
                    print("YOU WIN! :D")
                    game_over = True
                elif len(wrong)==14:
                    print("YOU LOST!\nthe word was: ", word)
                    game_over = True
            else:
                screen.fill("light blue")
                letters=[]
                wrong=[]
                word = new_game()
                letter = ""
                game_over = False
                                
                
    
            
       

    
   
    

    pygame.display.flip()
    
    
pygame.quit()

