import pygame
import sys
import random

pygame.init()
screen=pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Jeu du pendu")
font=pygame.font.Font(None,35)
button_text= font.render("Jouer",True,(255,255,255))
button_rect= button_text.get_rect(center=(500,350))
button_rect.width += 50
button_rect.height += 20
text_rect=pygame.Rect(225, 400,600,50)

user_text= ''
input_active=False


pygame.display.flip()
mot=[]

with open("mots.txt","r")as file:
    for i in file:
        mot.append(i.rstrip("\n"))

def message(message,message_rectangle,color):
    message = font.render(message,False,color)
    screen.blit(message,message_rectangle)    

tiret="-"   
mot_a_deviner = "Pendu"  # Remplacez cela par le mot à deviner
tentatives = set()  # Pour stocker les lettres déjà essayées
random_word=""
hide_word=""
score=0
game=True
start_screen=True
while game:   
    while start_screen == True:
        for event in pygame.event.get():
            text_jouer=pygame.Rect(225,300,600,50)
            screen.fill((0,0,255))
            screen.blit(button_text, (button_rect.centerx -29 , button_rect.centery -10))
            pygame.draw.rect(screen, (0,0,0), button_rect, 2)
                        
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    start_screen=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si l'utilisateur clique dans la zone de texte, activez l'entrée de texte
                if text_rect.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        with open("mots.txt","a") as file:
                            file.write(user_text+"\n")
                        print(user_text)  # Affiche le texte lorsque l'utilisateur appuie sur Entrée
                        user_text = ''  # Efface le texte après avoir appuyé sur Entrée
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]  # Supprime le dernier caractère
                    else:
                        user_text += event.unicode  # Ajoute le texte saisi par l'utilisateur
        pygame.draw.rect(screen, (0,0,0), text_rect, 2)
        #etape pour afficher le texte que l'utilisateur ecrit
        text_surface = font.render(user_text, True,(0,0,0))
        screen.blit(text_surface, (text_rect.x + 5, text_rect.y + 5))

        pygame.display.flip()

    for event in pygame.event.get():
        message(hide_word,(450, 300,600,50),(0,0,0))
        text_tentatives = font.render("Tentatives: " + ", ".join(sorted(tentatives)), True, (0, 0, 0))
        screen.blit(text_tentatives, (50, 50))
        if event.type == pygame.QUIT:
            sys.exit()    
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha() and event.unicode.upper() not in tentatives:
                tentatives.add(event.unicode.upper())
                if event.unicode.upper() in random_word.upper():
                    hide_word = "".join([char if char.upper() in tentatives else "-" for char in random_word])

        screen.fill((0,255,255))   
        
        message("Appuyez sur échap pour (re)commencer une partie",(225, 50,600,50),(0,0,0))        
        message(hide_word,(450, 300,600,50),(0,0,0))
        pygame.display.flip()    
        

pygame.quit()
sys.exit()