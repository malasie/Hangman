import pygame

def drawing(wrong):
    
    pos=[[(250,300), (250,400)],[(250,350), (300,380)],
         [(250,350), (200,380)],[(250,350), (200,380)],
         [(250,400), (300,450)],[(250,400), (200,450)]]
        
    for i in range(len(wrong)):
        if len(wrong)<6:
            color="purple"
        else:
            color="brown"
            
        if i==0:
            pygame.draw.circle(screen, color, (250,300), 30)
        else:
            pygame.draw.line(screen, color, pos[i-1][0], pos[i-1][1], 3)

    
    
    #szubienica
    
    
    pygame.draw.line(screen, color, (100,500), (350,500),3)
    pygame.draw.line(screen, color, (150,500), (150,200),3)
    pygame.draw.line(screen, color, (100,500), (150,450),3)
    pygame.draw.line(screen, color, (200,500), (150,450),3)
    pygame.draw.line(screen, color, (200,200), (150,250),3)
    pygame.draw.line(screen, color, (100,200), (300,200),3)
    pygame.draw.line(screen, color, (250,270), (250,200),3)




pygame.init()
screen = pygame.display.set_mode((500,720))
font = pygame.font.Font(pygame.font.get_default_font(), 36)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("light blue")   
    

    alphabet = ['a','b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    guessed=["c","d", "i"]
    wrong=["z"]
    
    drawing(wrong)
    
    back = (0,0,0)
    color_font = ["black", "blue", "red"]
    images = []
    for letter in alphabet:
        if letter in wrong:
            color = color_font[2]
        elif letter in guessed:
            color = color_font[1]
        else:
            color = color_font[0]
        s_image = font.render(letter, True, color)
        images.append(s_image)
    
    
    for index, image in enumerate(images):
        if index < len(images)/2:
            screen.blit(image,(20 + index*35 ,560))
            
        else:
            screen.blit(image,(20 + (index-len(images)/2)*35 ,600))


# # now print the text
#     text_surface = font.render("".join(alphabet), True, "black")
#     screen.blit(text_surface, (5,550))    

    pygame.display.flip()
        
    
pygame.quit()

