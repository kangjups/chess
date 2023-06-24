# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 19:40:37 2023

@author: angel
"""


# 1920 - 800 = 1120 /2 = 560
# 1080 - 800 = 280 / 2 = 140 
# 70 // 160 - 100 60 30/30 
# 체스판 x = 560 체스판 y  770 


import pygame
import random

class chess_text:
    def __init__(self,img):
        self.img = pygame.image.load(img)
       # self.sound = pygame.mixer.Sound(mp3)
        self.word_list = ["aaa","www","sss"] 
        self.word = random.choice(self.word_list)
        
        self.RED = (255,0,0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        
        self.font = pygame.font.SysFont(None,130)
        
    def re_word(self):
        self.word = random.choice(self.word_list)
       
    
    def move(self):
        pass
        return
    
    def screen(self,screen,x,y):
        screen.blit(self.font.render(str(self.word),True,self.BLACK),(x,y))
    
        
def tiles_init(position):
    tiles = ["0","1","0","1","0","1","0","1",
             "1","0","1","0","1","0","1","0",
             "0","1","0","1","0","1","0","1",
             "1","0","1","0","1","0","1","0",
             "0","1","0","1","0","1","0","1",
             "1","0","1","0","1","0","1","0",
             "0","1","0","1","0","1","0","1",
             "1","0","1","0","1","0","1","0"] 
    tiles[position] = "player"
    return tiles

def fn_fight():
    
    #파이썬 기본 설정
    pygame.init()
    
    screen_width = 1920
    screen_height = 1080
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # 파이썬 이미지 불러오기
    back = pygame.image.load("배경.png")
    tile_blue = pygame.image.load("파란타일.png")
    tile_black = pygame.image.load("검은타일.png")
    tile_blue_shades = pygame.image.load("파란타일그림자.png")
    tile_black_shades = pygame.image.load("검은타일그림자.png")
    
    player = pygame.image.load("폰.png")
    position = 4
    
    spell_ba = pygame.image.load("글자바.png")
    
    pon_text = chess_text("폰_text.png")
    
    text_list = [pon_text]
    my_text_list = [pon_text]
    
    
    spell_text = pygame.image.load("글자텍스트.png")
    
    
    # 타일 리스트에 넣기
    tiles = ["0","1","0","1","0","1","0","1",
             "1","0","1","0","1","0","1","0",
             "0","1","0","1","0","1","0","1",
             "1","0","1","0","1","0","1","0",
             "0","1","0","1","0","1","0","1",
             "1","0","1","0","1","0","1","0",
             "0","1","0","1","0","1","0","1",
             "1","0","1","0","1","0","1","0"]
    tiles[position] = "player"
    tiles_shades = [tile_blue_shades,tile_black_shades,tile_blue_shades,tile_black_shades,tile_blue_shades,tile_black_shades,tile_blue_shades,tile_black_shades]
    
    
    
    floor = 8 # 타일 수
    spell = [] # 영어 스펠링
    word = "/" # 단어
    
    RED = (255,0,0)
    BLUE = (0, 0, 255)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    
    font = pygame.font.SysFont(None,130)
    #screen.blit(font.render(str(card_time),True,BLACK),(x,y))
    running = True
    while running:
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                
            if event.type == pygame.MOUSEMOTION:
                pass
            
            if event.type == pygame.MOUSEBUTTONDOWN: # 마우스의 어떤 버튼을 눌렀을때
                if event.button == 1:  # 마우스 왼쪽 클릭시
                    x_p, y_p = pygame.mouse.get_pos()    
                
                    if x_p > 1200 and x_p < 1800 and y_p > 10 and y_p < 400:
                        running = False
                    
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_q:
                    spell.append("q")
                if event.key == pygame.K_w:
                    spell.append("w")
                if event.key == pygame.K_e:
                    spell.append("e")
                if event.key == pygame.K_r:
                    spell.append("r")
                if event.key == pygame.K_t:
                    spell.append("t")
                if event.key == pygame.K_y:
                    spell.append("y")
                if event.key == pygame.K_u:
                    spell.append("u")
                if event.key == pygame.K_i:
                    spell.append("i")
                if event.key == pygame.K_o:
                    spell.append("o")
                if event.key == pygame.K_p:
                    spell.append("p")
                    
                    
                if event.key == pygame.K_a:
                    spell.append("a")
                if event.key == pygame.K_s:
                    spell.append("s")
                if event.key == pygame.K_d:
                    spell.append("d")
                if event.key == pygame.K_f:
                    spell.append("f")
                if event.key == pygame.K_g:
                    spell.append("g")
                if event.key == pygame.K_h:
                    spell.append("h")
                if event.key == pygame.K_j:
                    spell.append("j")
                if event.key == pygame.K_k:
                    spell.append("k")
                if event.key == pygame.K_l:
                    spell.append("l")
                    
                    
                if event.key == pygame.K_z:
                    spell.append("z")
                if event.key == pygame.K_x:
                    spell.append("x")
                if event.key == pygame.K_c:
                    spell.append("c")
                if event.key == pygame.K_v:
                    spell.append("v")
                if event.key == pygame.K_b:
                    spell.append("b")
                if event.key == pygame.K_n:
                    spell.append("n")
                if event.key == pygame.K_m:
                    spell.append("m")
                
               # print(spell)
                
                if event.key == pygame.K_SPACE:
                # 캐릭터 움직임     
                    for i in range(len(spell)):
                        word += spell[i]
                    spell.clear() 
                  #  print(word)
                    
                    if word == "/" + "go" :
                        position += 8
                        tiles = tiles_init(position)
                       
                        
                        
                        
                    elif word == "/" + "back" :
                        print("뒤로")

                    elif word == "/" + "to" :
                        print("가다")
               
                    else :
                        print("그런 단어는 없어")
                    
                    word = "/"
        
        if len(spell) > 8 :
            for i in range(len(spell)):
                word += spell[i]
            spell.clear() 
          
            
            if word == "/" + "go" :
                print("가다")
                
            elif word == "/" + "back" :
                print("뒤로")

            elif word == "/" + "to" :
                print("가다")
        
            
            else :
                print("그런 단어는 없어")
            
            word = "/"
            
        screen.blit(back,(0,0))            
        
        # 체스 타일
        for i in range(len(tiles)):
            if i == floor:
                floor += 8
            if i < floor :
                tile_x = 560 + (100*(i-(floor-8)))  # 길이 
                tile_y = 880 - (100*(floor/8))  # 높이 
                
                if tiles[i] == "0" :
                    screen.blit(tile_blue,(tile_x,tile_y))
                
                if tiles[i] == "1" :     
                    screen.blit(tile_black,(tile_x,tile_y))
                
                if tiles[i] == "player":
                    screen.blit(player,(tile_x,tile_y))
                
            if i == len(tiles)-1:
                floor = 8
                
        # 체스 타일 그림자
        for i in range(len(tiles_shades)):
            
            if tiles_shades[i] == tile_blue_shades:    
                screen.blit(tile_blue_shades, (560+(100*i), 880))
            
            if tiles_shades[i] == tile_black_shades:    
                screen.blit(tile_black_shades, (560+(100*i), 880))
        
        # 글자 적는 부분
        screen.blit(spell_ba,(560,930))
        
        # 글자 나오는 부분
        for i in range(len(spell)):
            screen.blit(font.render((spell[i]),True,BLACK),(560+(100*i+25),935))
        
        # 스킬 / 영단어 나오는 부분
        for i in range(len(my_text_list)):
            screen.blit(my_text_list[i].img,(50,(120+(120*i))))
            my_text_list[i].screen(screen, 150,(120+(120*i)))
        
        #행동 글자 
        #screen.blit(spell_text,(50,120))  
     #   screen.blit(spell_text,(50,240))
      #  screen.blit(spell_text,(50,360))
     #   screen.blit(spell_text,(50,480))
       # screen.blit(spell_text,(50,600))
        
        pygame.display.update()
    
    pygame.quit()
        
fn_fight()





