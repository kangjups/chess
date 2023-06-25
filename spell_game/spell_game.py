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

class cls_character:
    def __init__(self,img,name,position):
        self.img = pygame.image.load(img)
        self.name = name
        self.position = position
        
        self.RED = (255,0,0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        
        self.font = pygame.font.SysFont(None,30)
 #       self.hp_img = self.font.render(str(self.hp),True,self.BLACK)
        self.name_img = self.font.render(str(self.name),True,self.BLACK)

class chess_text:
    def __init__(self,img,name):
        self.img = pygame.image.load(img)
        self.name = name
       # self.sound = pygame.mixer.Sound(mp3)
        self.word_list = ["about","across",
                          " actor" ,"afternoon" 
                          ,"again" ,"age" ,"ago" ,"air" ,"airplane" ,"airport" 
                          ,"album" ,"always" ,"among" ,"an" ,"angry" ,"animal" ,"answer","apple","arrive"] 
        self.word = random.choice(self.word_list)
        
        self.RED = (255,0,0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        
        self.font = pygame.font.SysFont(None,100)
        
    def re_word(self):
        self.word = random.choice(self.word_list)
       
    
    def move(self,tiles,player,enemy):
        
        if self.name == "pon": 
            player.position += 8
            if player.position >= len(tiles):
                player.position -= 8
            return re_tiles(player,enemy),player.position,enemy.position
        
        if self.name == "bishop": 
            player.position += 9
            if player.position >= len(tiles):
                 player.position -= 9
            return re_tiles(player,enemy),player.position,enemy.position
        
    def screen(self,screen,x,y):
        screen.blit(self.font.render(str(self.word),True,self.BLACK),(x,y))

        
def re_tiles(player,enemy):
    tiles = ["0","1","0","1","0","1","0","1",
             "1","0","1","0","1","0","1","0",
             "0","1","0","1","0","1","0","1",
             "1","0","1","0","1","0","1","0",
             "0","1","0","1","0","1","0","1",
             "1","0","1","0","1","0","1","0",
             "0","1","0","1","0","1","0","1",
             "1","0","1","0","1","0","1","0"] 
    
    tiles[player.position] = player.name
    tiles[enemy.position] = enemy.name
    
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
    nagagi = pygame.image.load("나가기.png")
    
    player = cls_character("폰.png","player",3)
    enemy = cls_character("블랙폰.png","enemy",60)
    
    spell_ba = pygame.image.load("글자바.png")
    
    pon_text = chess_text("폰_text.png","pon")
    bishop = chess_text("비숍_text.png","bishop")
    
    text_list = [pon_text,bishop]
    text_1 =pon_text
    text_2 =bishop
    text_3 =pon_text
    text_3.re_word()
    # 새로운 객체로 만들어야 
    
    my_text_list = [text_1,text_2,text_3]
    
    
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
    
    tiles[player.position] = player.name
    tiles[enemy.position] = enemy.name
 
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
                
                    if x_p > 1600 and x_p < 1800 and y_p > 50 and y_p < 400:
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
                
                if event.key == pygame.K_RETURN:
                
                    # 캐릭터 움직임     
                    for i in range(len(spell)):
                        word += spell[i]
                    spell.clear() 
                  
                    for i in range(len(my_text_list)):
                        if word == "/" + my_text_list[i].word :
                            tiles,player.position,enemy.position = my_text_list[i].move(tiles,player,enemy)
                            my_text_list[i].re_word()
                    word = "/"
                
                if event.key == pygame.K_BACKSPACE:
                    if len(spell) >= 1:
                        del(spell[len(spell)-1])
                    
        # 글자가 제한을 넘었을때    
        if len(spell) > 8 :
            for i in range(len(spell)):
                word += spell[i]
            spell.clear() 
            
          #  for i in range(len(my_text_list)):
           #     if word == "/" + my_text_list[i].word :
            #        tiles,player.position = my_text_list[i].move(player.position)
            
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
                    screen.blit(player.img,(tile_x,tile_y))
                
                if tiles[i] == "enemy":
                    screen.blit(enemy.img,(tile_x,tile_y))
                 
                
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
            my_text_list[i].screen(screen, 180,(140+(120*i)))
        screen.blit(nagagi,(1600,50))
        pygame.display.update()
    
    pygame.quit()
if __name__ == "__main__":       
    fn_fight()






