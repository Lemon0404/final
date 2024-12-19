import pyxel
import random

class Start:
    def __init__(self):
        self.page=0
        self.x=0
        self.y=50
        self.i=-1
        self.f=1
        self.n_x=1
        self.time=0
        self.previous_time=0
        self.first=True

    def update(self):
        self.time+=1
        if self.time%6==0:
            self.f=-self.f

        if self.page==0:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.page+=1
        if self.page==1:
            if ((121<=pyxel.mouse_x<=125 and 170<=pyxel.mouse_y<=174) and (pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT))) or \
                pyxel.btnp(pyxel.KEY_RIGHT):
                self.page=2
                self.previous_time=self.time
        if self.page==2:
            if ((75<=pyxel.mouse_x<=79 and 170<=pyxel.mouse_y<=174) and (pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT))) or\
                pyxel.btnr(pyxel.KEY_LEFT):
                if (self.time-self.previous_time)>=30:
                    self.page=1
                    self.previous_time=self.time
            if ((121<=pyxel.mouse_x<=125 and 170<=pyxel.mouse_y<=174) and (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT))) or \
                pyxel.btnr(pyxel.KEY_RIGHT):
                if (self.time-self.previous_time)>=30:
                    self.page=3
                    self.previous_time=self.time
        if self.page==3:
            if ((75<=pyxel.mouse_x<=79 and 170<=pyxel.mouse_y<=174) and (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT))) or\
                pyxel.btnp(pyxel.KEY_LEFT):
                if (self.time-self.previous_time)>=30:
                    self.page=2
                    self.previous_time=self.time
            if ((121<=pyxel.mouse_x<=125 and 170<=pyxel.mouse_y<=174) and (pyxel.btn(pyxel.MOUSE_BUTTON_LEFT))) or \
                pyxel.btnp(pyxel.KEY_RIGHT):
                if (self.time-self.previous_time)>=30:
                    self.page=4
        if self.page==4:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.page=5

    def draw(self):
        if self.page==0:
            pyxel.load('start.pyxres')
            pyxel.cls(0)
            pyxel.bltm(38,38,0,0,0,128,128,0)
            pyxel.text(120,190,"Thanks to HOYOVERSE",7)
            pyxel.line(10,10,10,190,7)
            pyxel.line(10,10,190,10,7)
            pyxel.line(190,10,190,185,7)
            pyxel.line(10,190,115,190,7)
            if self.f>=0:
                pyxel.text(70,140,"Press SPACE key",7)
        else:
            pyxel.mouse(True)
            if self.first:
                pyxel.cls(0)
            else:
                pyxel.rect(10,10,180,180,0)
            pyxel.line(10,10,10,190,7)
            pyxel.line(10,10,190,10,7)
            pyxel.line(190,10,190,190,7)
            pyxel.line(10,190,190,190,7)
            pyxel.text(75,20,"How to Play "+str(self.page),7)
            if self.page==1:
                pyxel.text(121,170,">",7)
                pyxel.text(115,176,"NEXT",7)
                pyxel.load("start.pyxres")
                pyxel.text(20,40,"1.Move",7)
                pyxel.text(120,45,"Move charactor",7)
                pyxel.text(120,55,"with W/A/S/D KEY",7)
                pyxel.bltm(20,20,0,0,128,160,160,0)
                pyxel.text(20,80,"2.Atack",7)
                pyxel.text(120,85,"Atack wiht",7)
                pyxel.text(120,95,"MOUSE Click",7)
                pyxel.text(20,120,"3.Skill",7)
                pyxel.text(100,125,"When the gauge is full",7)
                pyxel.text(120,135,"press SPACE",7)
                pyxel.text(110,145,"to use your skill",7)
            if self.page==2:
                pyxel.text(75,170,"<",7)
                pyxel.text(69,176,"BACK",7)
                pyxel.text(121,170,">",7)
                pyxel.text(115,176,"NEXT",7)
            if self.page==3:
                pyxel.text(75,170,"<",7)
                pyxel.text(69,176,"BACK",7)
                pyxel.text(121,170,">",7)
                pyxel.text(115,176,"NEXT",7)
            if self.page==4:
                if self.f>=0:
                    if self.first:
                        pyxel.text(60,80,"Press SPACE to START!!",7)
                    else:
                        pyxel.text(30,80,"Press SPACE to go back to Game!!",7)

class Player:
    def __init__(self):
        self.x=30
        self.y=180
        self.w=16
        self.h=16
        self.n_x=1
        self.n_y=1
        self.direct=1
        self.damage_flag=False
        self.player_hp=5
        self.condition=0#プレイヤーの状態を分ける
        self.num=0
        self.get_num=-1

    def move(self):
        if pyxel.btn(pyxel.KEY_D):
            self.x+=1.5
            self.direct=1
        if pyxel.btn(pyxel.KEY_A):
            self.x-=1.5
            self.direct=2
        if pyxel.btn(pyxel.KEY_S):
            self.y+=1.5
            self.direct=3
        if pyxel.btn(pyxel.KEY_W):
            self.y-=1.5
            self.direct=4

        #プレイヤーの二つの絵を切り替える関数の更新
        if self.x%4==0:
            self.n_x=-self.n_x
        if self.y%4==0:
            self.n_y=-self.n_y

    def is_damage(self,enemy):
        if enemy.flag:
            return self.x-(enemy.w-1)<=enemy.x<=self.x+(self.w-1) and self.y-(enemy.h-1)<=enemy.y<=self.y+(self.h-1)
        return False
    
    def damage(self,enemy):
        self.damage_flag=self.is_damage(enemy)
        pyxel.sounds[1].set(notes='A2F2', tones='TT', volumes='33', effects='NN', speed=10)
        if enemy.flag:
            if self.is_damage(enemy):
                if enemy.d==0:
                    pyxel.play(0, 1)
                    self.player_hp-=1
                enemy.d+=1
                self.num+=1
                if enemy.d>=27:
                    enemy.d=0
            else:
                enemy.d=0
                self.num=0


    def draw(self):
        pyxel.load('my_resource.pyxres')
        #ダメージを受けていなかった場合
        if self.damage_flag==False:
            if self.condition==0:
                if self.direct==1:
                    if self.n_x>0:
                        pyxel.blt(self.x,self.y,0,32,0,self.w,self.h,11)
                    else:
                        pyxel.blt(self.x,self.y,0,48,0,self.w,self.h,11)
                if self.direct==2:
                    if self.n_x>0:
                        pyxel.blt(self.x,self.y,0,0,0,self.w,self.h,11)
                    else:
                        pyxel.blt(self.x,self.y,0,16,0,self.w,self.h,11)
                if self.direct==3:
                    if self.n_y>0:
                        pyxel.blt(self.x,self.y,0,0,16,self.w,self.h,11)
                    else:
                        pyxel.blt(self.x,self.y,0,16,16,self.w,self.h,11)
                if self.direct==4:
                    if self.n_y>0:
                        pyxel.blt(self.x,self.y,0,32,16,self.w,self.h,11)
                    else:
                        pyxel.blt(self.x,self.y,0,48,16,self.w,self.h,11)
            if self.condition==1:
                if self.direct==1 or self.direct==2:
                    if self.n_x>0:
                        pyxel.blt(self.x,self.y,0,32,64,self.w,self.h,11)
                    else:
                        pyxel.blt(self.x,self.y,0,48,64,self.w,self.h,11)
                elif self.direct==3 or self.direct==4:
                    if self.n_y>0:
                        pyxel.blt(self.x,self.y,0,32,64,self.w,self.h,11)
                    else:
                        pyxel.blt(self.x,self.y,0,48,64,self.w,self.h,11)
    #ダメージを受けていた場合
        else: 
            if self.num%2==0 and self.num>0:
                if self.condition==0:
                    if self.direct==1:
                        pyxel.blt(self.x,self.y,0,16,48,self.w,self.h,11)
                    if self.direct==2:
                        pyxel.blt(self.x,self.y,0,0,48,self.w,self.h,11)
                    if self.direct==3:
                        pyxel.blt(self.x,self.y,0,32,48,self.w,self.h,11)
                    if self.direct==4:
                        pyxel.blt(self.x,self.y,0,48,48,self.w,self.h,11)
                else:
                    pyxel.blt(self.x,self.y,0,0,64,self.w,self.h,11)

class Attack:
    def __init__(self):
        self.x=0
        self.y=0
        self.is_skill=False

    def move(self,player): 
            if player.direct==1:
                self.x=player.x+player.w
                self.y=player.y
            if player.direct==2:
                self.x=player.x-4
                self.y=player.y
            if player.direct==3:
                self.x=player.x
                self.y=player.y+player.h
            if player.direct==4:
                self.x=player.x
                self.y=player.y-4

    def attack_draw(self,player):
        pyxel.load('effect.pyxres')
        if player.direct==1:
            pyxel.load('effect.pyxres')
            pyxel.blt(self.x,self.y,0,0,0,4,16,11)
            pyxel.load('my_resource.pyxres')
            pyxel.blt(player.x,player.y,0,16,32,16,16,11)
        if player.direct==2:
            pyxel.load('effect.pyxres')
            pyxel.blt(self.x,self.y,0,8,0,4,16,11)
            pyxel.load('my_resource.pyxres')
            pyxel.blt(player.x,player.y,0,0,32,16,16,11)
        if player.direct==3:
            pyxel.load('effect.pyxres')
            pyxel.blt(self.x,self.y,0,16,0,16,4,11)
            pyxel.load('my_resource.pyxres')
            pyxel.blt(player.x,player.y,0,32,32,16,16,11)
        if player.direct==4:
            pyxel.load('effect.pyxres')
            pyxel.blt(self.x,self.y,0,16,8,16,4,11)
            pyxel.load('my_resource.pyxres')
            pyxel.blt(player.x,player.y,0,48,32,16,16,11)

class Arrows:
    def __init__(self,player):
        self.x=player.x+7
        self.y=player.y-7
        self.flag=True
        self.is_skill=False

    def move(self):
        self.y-=2
        if self.y<0:
            self.flag=False
    
    def arrows_draw(self):
        if self.flag:
            pyxel.load('effect.pyxres')
            pyxel.blt(self.x,self.y,0,34,0,3,7,11)

    def skill_draw(self):
        if self.flag:
            pyxel.load('effect.pyxres')
            pyxel.blt(self.x,self.y,0,42,0,3,8,11)



class Enemy:
    def __init__(self):
        self.type=random.randint(1,2)
        self.x=100
        self.y=0
        self.w=13
        if self.type==1:
            self.h=13
        if self.type==2:
            self.h=11
        self.e_y=1
        self.flag=True
        self.kill_flag=False
        self.n=0
        self.d=0
        self.give_damage=False

    def move(self,player):
        #エネミーが画面下から出た場合
        if self.y>200 and self.flag==True:
            self.x=random.randint(10,187)
            self.type=random.randint(1,2)
            self.y=0
            if self.type==1:
                self.h=13
            if self.type==2:
                self.h=11
        #範囲に生存している場合
        elif self.y<=200 and self.flag==True:
            self.y+=1
            if self.x<player.x:
                self.x+=0.2
            elif self.x>player.x:
                self.x-=0.2
        #倒された場合
        else:
            self.n+=1
        
        #エネミーの二つの絵を切り替える関数の更新
        if self.y%4==0:
            self.e_y=-self.e_y

    def is_kill(self,player,attack,arrows):
    # プレイヤーとエネミーの当たり判定を確認
        if player.condition==0: 
            if player.direct == 1:  # 右向き
                return self.x-3<=attack.x<=self.x+self.w-4 and self.y-player.h+3<=attack.y<=self.y+self.h-3
            elif player.direct == 2:  # 左向き
                return self.x<=attack.x<=self.x+self.w-1 and self.y-player.h+3<=attack.y<=self.y+self.h-3
            elif player.direct == 3:  # 下向き
                return self.x-player.w+3<=attack.x<=self.x+self.w-3 and self.y-3<=attack.y<=self.y+self.h-4
            elif player.direct == 4:  # 上向き
                return self.x-player.w+3<=attack.x<=self.x+self.w-3 and self.y<=attack.y<=self.y+self.h-1
        if player.condition==1:
            for i in range(len(arrows)):
                if self.x-1<=arrows[i].x<=self.x+self.w and self.y<=arrows[i].y<=self.y+self.h:
                    arrows[i].flag=False
                    return True
        return False

    def kill(self, player,attack,arrows):
        # pyxel.sounds[0].set(notes='C3F3', tones='TT', volumes='33', effects='NN', speed=10)
        # pyxel.sounds[2].set(notes='C2', tones='T', volumes='33', effects='N', speed=10)
    #クリックされていて当たり判定がtrueなら効果音とtrueを返す  
        if player.condition==0:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if self.flag and self.is_kill(player,attack,arrows):
                    # pyxel.play(0, 0)
                    self.kill_flag=True
                    self.flag=False
                # else:
                #     pyxel.play(0, 2)

        if player.condition==1:
            if self.flag and self.is_kill(player,attack,arrows):
                # pyxel.play(0, 0)
                self.kill_flag=True
                self.flag=False
            # if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            #     pyxel.play(0, 2)

        if self.n>0:
            self.kill_flag=False            
        if self.n>=4:
            self.x=random.randint(10,187)
            self.type=random.randint(1,2)
            self.y=0 
            self.flag=True
            self.n=0   
            if self.type==1:
                self.h=13
            if self.type==2:
                self.h=11

    def draw(self):
        pyxel.load('enemy.pyxres')
        #倒されていない場合
        if self.flag==True:
            if self.type==1:
                if self.e_y>0:
                    pyxel.blt(self.x,self.y,0,0,0,self.w,self.h,11)
                else:
                    pyxel.blt(self.x,self.y,0,16,0,self.w,self.h,11)
            if self.type==2:
                if self.e_y>0:
                    pyxel.blt(self.x,self.y,0,32,0,self.w,self.h,11)
                else:
                    pyxel.blt(self.x,self.y,0,48,0,self.w,self.h,11)
        #倒された場合
        else:
            if self.type==1:
                pyxel.blt(self.x,self.y,0,0,16,self.w,self.h,11)
            if self.type==2:
                pyxel.blt(self.x,self.y,0,32,16,self.w,self.h,11)
    
class Items:
    def __init__(self):
        self.type=random.randint(0,2)
        self.x=random.randint(0,187)
        self.y=0
        if self.type==0:
            self.w=14
            self.h=14
        if self.type==1:
            self.w=14
            self.h=12
        if self.type==2:
            self.w=12
            self.h=13
        self.get_whale=0
        self.flag=True
        self.previous_time=0
        self.go_time=random.randint(self.previous_time,self.previous_time+800)

    def move(self,time):
        #エネミーが画面下から出た場合
        if self.y>200 or self.flag==False:
            self.get_whale=0
            self.previous_time=time
            self.x=random.randint(0,187)
            self.type=random.randint(0,2)
            self.y=0
            self.go_time=random.randint(self.previous_time,self.previous_time+800)
        #範囲に生存している場合
        elif self.y<=200 and self.flag==True:
            if time>=self.go_time:
                self.y+=1

    def draw(self,time):
        pyxel.load('items.pyxres')
        #獲得されていない場合
        if self.flag==True:
            if time>=self.go_time:
                pyxel.blt(self.x,self.y,0,16*self.type,0,self.w,self.h,11)
    
    def is_get(self,player):
        if not player.damage_flag and self.flag:
            return player.x-(self.w-1)<=self.x<=player.x+player.w+(self.w-1) and player.y-(self.h-1)<=self.y<=player.y+player.h+(self.h-1)
            
    def get(self,player,time):
        if time>=self.go_time:
            if self.is_get(player):
                self.flag=False
                if self.type==0:
                    player.get_num=self.type
                    player.condition=1
                if self.type==1:
                    player.get_num=self.type
                    self.get_whale=1
                if self.type==2:
                    player.get_num=self.type
                    if player.player_hp<5:
                        player.player_hp+=1
            
            else:
                player.get_num=-1


class App:
    def __init__(self):
        pyxel.init(200,200,fps=20)
        pyxel.sounds[0].set(notes='C3F3', tones='TT', volumes='33', effects='NN', speed=10)
        pyxel.sounds[1].set(notes='A2F2', tones='TT', volumes='33', effects='NN', speed=10)
        pyxel.sounds[2].set(notes='C2', tones='T', volumes='33', effects='N', speed=10)
        pyxel.sounds[3].set(notes='G3F#3F3E3', tones='TTTT', volumes='33', effects='NNNN', speed=100)
        self.resetvalues()
        pyxel.run(self.update,self.draw)

    def update(self):
        if self.start.page<5:
            self.start.update()
        else:
            if not self.GameOver:

                #Tabが押されたらポーズ/ゲームに戻る
                if pyxel.btnp(pyxel.KEY_TAB):
                    if self.pause_flag==False:
                        self.pause_flag=True
                    else:
                        self.pause_flag=False

                #ポーズ中の更新
                if self.pause_flag:
                    if (70<=pyxel.mouse_x<=140 and 60<=pyxel.mouse_y<=100):
                        self.pause_y=80
                    if (70<=pyxel.mouse_x<=140 and 100<pyxel.mouse_y<=140):
                        self.pause_y=120

                    if (142<=pyxel.mouse_x<=149 and 55<=pyxel.mouse_y<=62) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                        self.pause_y=0
                        self.pause_flag=False

                    if self.pause_y==80 and (pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.KEY_KP_ENTER)):
                        self.start.page=0
                        self.resetvalues()
                    if self.pause_y==120 and (pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.KEY_KP_ENTER)):
                        self.start.first=False
                        self.start.page=1

                #ポーズしていない場合
                else:
                    self.time+=1
                    self.previos_point=self.point
                    self.player.move()

                    #アイテムの更新
                    for i in range(self.item_num):
                        self.items[i].move(self.time)
                        self.items[i].get(self.player,self.time)
                        if self.items[i].get_whale==1:
                            self.skill_gauge+=2

                    #プレイヤーの状態の更新
                    if self.player.get_num==0:
                        self.previous_time=self.time
                    if self.time-self.previous_time>=40:
                        self.player.condition=0

                    if self.player.condition==1:
                        if self.skill_gauge>=12:
                            if pyxel.btnp(pyxel.KEY_SPACE):
                                self.skill_arrow.flag=True
                    if self.skill_arrow.flag:
                        self.skill_arrow.move(self.player)


                    for i in range(len(self.enemies)):       
                        self.enemies[i].move(self.player)#エネミーの更新処理 
                        self.player.damage(self.enemies[i])#プレイヤーのダメージ判定
                        self.enemies[i].kill(self.player,self.attack,self.arrows)#エネミーのキル判定

                        #敵を倒した時の更新
                        pyxel.sounds[0].set(notes='C3F3', tones='TT', volumes='33', effects='NN', speed=10)
                        pyxel.sounds[2].set(notes='C2', tones='T', volumes='33', effects='N', speed=10)#入れないとならない...?
                        if self.enemies[i].kill_flag:
                            pyxel.play(0,0)    
                            self.point+=10
                            self.combo+=1
                            if self.skill_gauge<12:
                                self.skill_gauge+=1
                            if self.fever_gauge<42:
                                if self.combo<10:
                                    self.fever_gauge+=1
                                else:
                                    self.fever_gauge+=2
                        else:
                            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                                if self.player.condition==0:
                                    pyxel.play(0,2)
                        if self.player.damage_flag:
                            if self.enemies[i].d==0:
                                self.combo=0
                        

                    #攻撃
                    pyxel.sounds[2].set(notes='C2', tones='T', volumes='33', effects='N', speed=10)#入れないとならない...?
                    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                        if self.player.condition==0:
                            # pyxel.play(0,2)
                            # self.arrows.clear()
                            self.attack.move(self.player)
                        if self.player.condition==1:
                            if self.arrows==[]:
                                pyxel.play(0,2)
                                self.arrows.append(Arrows(self.player))
                            elif self.arrows[-1].y<=self.player.y-40:
                                pyxel.play(0,2)
                                self.arrows.append(Arrows(self.player))
                            
                    for i in range(len(self.arrows)):
                        if self.arrows[i].flag:
                            self.arrows[i].move()
                        if self.arrows[i].flag==False:
                            del self.arrows[i]
                            break
                    
                    #ステージの更新
                    if self.point!=0 and self.point==self.stage*50 and self.previous_point!=self.point:
                        self.stage+=1
                        if len(self.enemies)<10:
                            self.enemies.append(Enemy())

                        
            pyxel.sounds[3].set(notes='G3F#3F3E3', tones='TTTT', volumes='33', effects='NNNN', speed=100)
            if self.player.player_hp<=0:
                if self.GameOver==False:
                    self.GameOver=True
                    pyxel.play(0,3)
            

    def draw(self):
        if self.start.page<5:
            self.start.draw()
        else:
            pyxel.cls(5)

            #プレイヤーの描画
            self.player.draw()
            for i in range(3):
                self.items[i].draw(self.time)
            
                    
            #攻撃モーション
            if self.pause_flag==False:
                if self.player.condition==0:
                    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                        self.attack.attack_draw(self.player)
                # if self.player.condition==1:
                for i in range(len(self.arrows)):
                    if self.arrows[i].flag==True:
                        self.arrows[i].arrows_draw()

            if self.skill.flag:
                if self.player.condition==1:
                    self.skill_arrow.skill_draw()
            
            #敵の描画
            for i in range(len(self.enemies)):
                self.enemies[i].draw()

            #ポイントの表示
            pyxel.text(5,3,"Point: "+str(self.point),0)

            pyxel.text(5,10,str(self.time),0)

            #コンボの表示
            if self.combo>0:
                pyxel.text(5,17,str(self.combo)+"Combo!!",0)
            
            #hpゲージの描画
            pyxel.load('effect.pyxres')
            for i in range(5):
                pyxel.blt(149+i*10,3,0,0,16,9,9,11)
            for i in range(self.player.player_hp):
                pyxel.blt(149+i*10,3,0,16,16,9,9,11)

            #スキルゲージの描画
            pyxel.load('effect.pyxres')
            pyxel.blt(170,170,0,0,96,24,24,11)
            for i in range(int(self.skill_gauge/2)):
                pyxel.blt(170,193-4*(i+1),0,24,119-4*(i+1),24,4,11)
            if self.skill_gauge>=12:
                pyxel.blt(169,169,0,48,96,26,26,11)

            #フィーバーゲージの描画
            pyxel.load('effect.pyxres')
            pyxel.blt(137,12,0,2,48,13,13,11)
            pyxel.blt(152,16,0,17,51,46,7,11)
            for i in range(int(self.fever_gauge)):
                pyxel.blt(154+i,16,0,19+i,67,1,7,11)
            if self.fever_gauge>=42:
                pyxel.blt(137,13,0,2,80,13,14,11)
                pyxel.blt(152,16,0,17,83,46,7,11)

            if self.skill_gauge>=12:
                if self.time%2==0:
                    pyxel.text(50,190,"press SPACE to use skill!!",7)
            if self.fever_gauge>=42:
                if self.time%2!=0:
                    pyxel.text(50,80,"press ENTER to fever!!",7)

            #ゲームオーバーの場合の表示
            if self.GameOver:
                pyxel.text(77,90,"Game Over...",0)

            

            #ポーズ中の描画
            if self.pause_flag:
                pyxel.mouse(True)
                pyxel.load("effect.pyxres")
                pyxel.rect(50,50,100,100,0)
                pyxel.line(50,50,50,150,7)
                pyxel.line(50,150,150,150,7)
                pyxel.line(150,150,150,50,7)
                pyxel.line(150,50,50,50,7)
                pyxel.text(70,80,"Back to the title",7)
                pyxel.text(70,120,"View manual",7)
                if self.pause_y>0:
                    pyxel.blt(self.pause_x,self.pause_y,0,0,32,3,5,11)
                pyxel.blt(142,55,0,8,32,7,7,11)
            else:
                pyxel.mouse(False)

    #再スタートの処理を行う関数
    def resetvalues(self):
        pyxel.sounds[0].set(notes='C3F3', tones='TT', volumes='33', effects='NN', speed=10)
        pyxel.sounds[1].set(notes='A2F2', tones='TT', volumes='33', effects='NN', speed=10)
        pyxel.sounds[2].set(notes='C2', tones='T', volumes='33', effects='N', speed=10)
        pyxel.sounds[3].set(notes='G3F#3F3E3', tones='TTTT', volumes='33', effects='NNNN', speed=100)
        self.time=0
        self.previous_time=0
        self.point=0
        self.previous_point=0
        self.GameOver=False
        self.pause_flag=False
        self.pause_x=60
        self.pause_y=80
        self.player=Player()
        self.enemies=[]
        self.stage=1
        self.enemies.append(Enemy())
        self.combo=0
        self.start=Start()
        self.fever_gauge=0#MAX42
        self.skill_gauge=0#MAX12
        self.skill_arrow=Arrows(self.player)
        self.skill_arrow.flag=False
        self.skill_arrow.is_skill=True
        self.items=[]
        self.attack=Attack()
        self.arrows=[]
        self.item_num=5
        for _ in range(self.item_num):
            self.items.append(Items())


App()