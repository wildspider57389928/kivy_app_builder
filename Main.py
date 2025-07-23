from kivy.config import Config
Config.set('graphics', 'orientation', 'portrait')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('kivy','default_font',['./Assets/B-NAZANIN.TTF','./Assets/B-NAZANIN.TTF','./Assets/B-NAZANIN.TTF','./Assets/B-NAZANIN.TTF'])
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.progressbar import ProgressBar
from kivy.uix.camera import Camera

from kivy.animation import Animation
from kivy.graphics import Color,Rectangle,Line
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

import os
from random import randint
import json
#import arabic_reshaper
#from bidi.algorithm import get_display
from jnius import autoclass
#Window.size=360,640

def convert_to_persian(text):
     reshaped_text = text#arabic_reshaper.reshape(text)
     counter = 0
     for i in range(len(reshaped_text)):
         if counter >= 40 and reshaped_text[i] == ' ':
             reshaped_text = reshaped_text[:i] + '\n' + reshaped_text[i+1:]
             counter=0
         counter += 1
     bidi_text = reshaped_text[::1]#get_display(reshaped_text)
     return bidi_text
def create_user(username):#autoclass('android.os.Environment').getExternalStorageDirectory().getAbsolutePath()
     if not os.path.exists(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/sys11209.json'):
        os.mkdir(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin')
        with open(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/sys11209.json', 'a') as data:
                json.dump({username:{}},data)
        with open(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/sys11209.json', 'r') as data:
                loaded=json.load(data)
        loaded[username]={'Isdefault':'True',
                           'Level_math':1,
                           'Level_jadval_zarb':1,
                           'Coin':100,
                           'XP':10} 
        with open(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/sys11209.json', 'w') as data:
                json.dump(loaded,data,indent=4)
def get_user():
    with open(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/sys11209.json', 'r') as data:
            loaded=json.load(data)
    for user in loaded.keys():
        if loaded[user]['Isdefault']=='True':
            return user
def data_edit(user,key,value):
    with open(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/sys11209.json', 'r') as data:
            loaded=json.load(data)
    loaded[user][key]=value
    with open(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/sys11209.json', 'w') as data:
            json.dump(loaded,data,indent=4)
def data_get(user,key):
    with open(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/sys11209.json', 'r') as data:
            loaded=json.load(data)
    return loaded[user][key]
create_user('User1')
class BlueScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 0, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
class ImageButton(FloatLayout):
    def __init__(self, source,source2,pos, size,lv, command, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        self.btn = Button(
            text=str(lv),
            color=(0,0,0,1),
            size_hint=(None, None),
            size=size,
            pos=pos,
            background_normal=source,
            background_down=source2
        )
        self.btn.bind(on_press=command)
        self.add_widget(self.btn)
class Product(Widget):
    def __init__(self,name,description,pos,size,price,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0,0,1,1)
            self.rect=Rectangle(pos=pos, size=size)
            Color(0,0,0,1)
            self.border=Line(rectangle=(pos[0],pos[1],size[0],size[1]),width=3)
        self.add_widget(Label(text=convert_to_persian(name), pos=(pos[0]+115,pos[1]+size[1]-70), font_size=40, color=(1, 1, 1, 1)))
        self.add_widget(Label(text=convert_to_persian(description), pos=(pos[0]+185,pos[1]+size[1] - 150), font_size=25, color=(1, 1, 1, 1),text_size=(250,None)))
        self.add_widget(Button(text=convert_to_persian(f'خرید با {price} '),color=(0,1,1,1),background_color=(0.831, 0.051, 0.376, 1.0),size_hint=(None, None),size=(200,50),pos=(pos[0]+158,pos[1]+1)))
        # img=ImageButton("./Assets/setting.jpg","./Assets/setting.jpg",(pos[0]+10,pos[1]+55),(80,80),'',lambda instance:'')
        # self.add_widget(img)
class Folder(Widget):
    def __init__(self,picture,pos,size,command,**kwargs):
        super().__init__(**kwargs)
        img=ImageButton(picture,picture,(pos[0],pos[1]+100),(350,150),'',lambda instance:'')
        self.add_widget(img)
        with self.canvas:
            Color(0,0,0,1)
            Line(rectangle=(pos[0],pos[1],size[0],size[1]),width=3)
        self.add_widget(Button(text=convert_to_persian('شروع'),color=(0,1,1,1),background_color=(0.831, 0.051, 0.376, 1.0),size_hint=(None, None),size=(350,100),pos=(pos[0]+1,pos[1]+1),on_press=command))
class MainApp(App):
    def build(self):
        self.layout_progress=FloatLayout()
        self.layout_progress.add_widget(BlueScreen())
        self.progress=ProgressBar(max=100,size_hint=(None,None),size=(350,200),pos=(50,100))
        self.loading=Label(text=convert_to_persian("در حال بارگزاری..."),pos=(0,-250),font_size=40)
        self.layout_progress.add_widget(Label(text=convert_to_persian('خوش آمدید'),pos=(125,300),font_size=50,text_size=(450,None)))
        self.layout_progress.add_widget(self.loading)
        self.layout_progress.add_widget(self.progress)
        self.first=True
        self.loading_loop=Clock.schedule_interval(self.loading_func,1)
        return self.layout_progress
    def loading_func(self,dt):
        if self.first:
            self.Music=SoundLoader.load('./Assets/music.mp3')
            self.Music.volume=0.5
            self.Music.loop=True
            self.startup=SoundLoader.load('./Assets/startup.mp3')
            self.wrong_sound=SoundLoader.load('./Assets/wrong.mp3')
            self.correct_sound=SoundLoader.load('./Assets/correct.mp3')
            self.wrong_sound.volume=0.5
            self.correct_sound.volume=0.5
            self.first=False
        else:
            if self.loading.text==convert_to_persian("در حال بارگزاری."):
                self.loading.text=convert_to_persian("در حال بارگزاری..")
            elif self.loading.text==convert_to_persian("در حال بارگزاری.."):
                self.loading.text=convert_to_persian("در حال بارگزاری...")
            elif self.loading.text==convert_to_persian("در حال بارگزاری..."):
                self.loading.text=convert_to_persian("در حال بارگزاری.")
            if self.progress.value==100:
                Clock.unschedule(self.loading_loop)
                self.layout_progress.clear_widgets()
                self.buil()
            else:
                self.progress.value=self.progress.value+25
    def buil(self):
        self.startup.play()
        self.Music.play()
        self.timer_loop=None
        self.timer_loop_color=None
        self.parent=FloatLayout(size=(360, 640))
        self.layout=FloatLayout(size=(460, 4080),size_hint_y=None,height=4080,pos=(0,200))
        self.tabs=FloatLayout(size=(360,200))
        self.scroll_view = ScrollView(pos=(0,100),size_hint=(1, None),height=800,do_scroll_x=False,do_scroll_y=True)
        self.layout.add_widget(BlueScreen())
        self.scroll_view.add_widget(self.layout) 
        self.parent.add_widget(self.scroll_view)
        self.parent.add_widget(self.tabs)
        self.layout.add_widget(Label(text=str(data_get(get_user(),'Coin')),pos=(140,1900),font_size=30))
        self.layout.add_widget(Label(text=str(data_get(get_user(),'XP')),pos=(-120,1920)))
        if int(data_get(get_user(),'XP')) in range(0,200):
            self.layout.add_widget(Label(pos=(-100,1900),text=convert_to_persian('مبتدی')))   
        elif int(data_get(get_user(),'XP')) in range(200,375):
            self.layout.add_widget(Label(pos=(-100,1900),text=convert_to_persian('آماتور')))     
        elif int(data_get(get_user(),'XP')) in range(375,1125):
            self.layout.add_widget(Label(pos=(-100,1900),text=convert_to_persian('نیمه حرفه ای')))   
        elif int(data_get(get_user(),'XP')) in range(1125,2000):  
            self.layout.add_widget(Label(pos=(-100,1900),text=convert_to_persian('پیشرفته')))
        elif int(data_get(get_user(),'XP')) in range(2000,3000):
            self.layout.add_widget(Label(pos=(-100,1900),text=convert_to_persian('حرفه ای'))) 
        elif int(data_get(get_user(),'XP')) >=3000 :
            self.layout.add_widget(Label(pos=(-100,1900),text=convert_to_persian('استاد بزرگ')))       
        self.layout.add_widget(Folder('./Assets/math.jpg',(50,3600),(350,250),self.math))
        self.layout.add_widget(Folder('./Assets/jadval_zarb.png',(50,3300),(350,250),self.jadval_zarb))
        self.Tabs_drawer()
        img=ImageButton("./Assets/coins.jpg","./Assets/coins.jpg",(400,3920),(50,56),'',lambda instance:'')
        self.layout.add_widget(img)
        if os.path.exists(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/user_pic.png'):
            img=ImageButton(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/user_pic.png',os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/user_pic.png',(0,3872),(80,150),'',self.user_picture)        
        else:img=ImageButton("./Assets/user.jpg","./Assets/user.jpg",(0,3920),(50,56),'',self.user_picture)
        self.layout.add_widget(img)
        self.questions_count=10
        self.correct,self.incorrect=0,0
        self.correct_color,self.incorrect_color=0,0
        self.questions_count_color=10
        self.layout_progress.add_widget(self.parent)
    def Main_build(self,instance):
        if self.timer_loop:
            Clock.unschedule(self.timer_loop)
        if self.timer_loop_color:
            Clock.unschedule(self.timer_loop_color)
        self.layout.unbind(on_touch_down=self.place)
        self.layout.clear_widgets()
        self.layout.size=(360,4080)
        self.layout.add_widget(BlueScreen())
        self.layout.add_widget(Label(text=str(data_get(get_user(),'Coin')),pos=(140,1900),font_size=30))
        self.layout.add_widget(Label(text=str(data_get(get_user(),'XP')),pos=(-120,1920)))
        if int(data_get(get_user(),'XP')) in range(0,200):
            self.layout.add_widget(Label(pos=(-100,1900),text=convert_to_persian('مبتدی')))   
        elif int(data_get(get_user(),'XP')) in range(200,375):
            self.layout.add_widget(Label(pos=(-100,1900),text=convert_to_persian('آماتور')))     
        elif int(data_get(get_user(),'XP')) in range(375,1125):
            self.layout.add_widget(Label(pos=(-100,1900),text=convert_to_persian('نیمه حرفه ای')))   
        elif int(data_get(get_user(),'XP')) in range(1125,2000):  
            self.layout.add_widget(Label(pos=(-100,1900),text=convert_to_persian('پیشرفته')))
        elif int(data_get(get_user(),'XP')) in range(2000,3000):
            self.layout.add_widget(Label(pos=(-100,1900),text=convert_to_persian('حرفه ای'))) 
        elif int(data_get(get_user(),'XP')) >=3000 :
            self.layout.add_widget(Label(pos=(-100,1900),text=convert_to_persian('استاد بزرگ')))
        self.layout.add_widget(Folder('./Assets/math.jpg',(50,3600),(350,250),self.math))
        self.layout.add_widget(Folder('./Assets/jadval_zarb.png',(50,3300),(350,250),self.jadval_zarb))
        img=ImageButton("./Assets/coins.jpg","./Assets/coins.jpg",(400,3920),(50,56),'',self.Tab3_drawer)
        self.layout.add_widget(img)
        if os.path.exists(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/user_pic.png'):
            img=ImageButton(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/user_pic.png',os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/user_pic.png',(0,3872),(80,150),'',self.user_picture)
        else:img=ImageButton("./Assets/user.jpg","./Assets/user.jpg",(0,3920),(50,56),'',self.user_picture)
        self.layout.add_widget(img)
    def jadval_zarb(self,instance):
        self.layout.clear_widgets()
        self.layout.size=(360,1000)
        self.layout.add_widget(BlueScreen())
        self.level_drawer(100,-100,'right',self.level)
        self.level_drawer(250,-100,'left',self.level)
    def level_drawer(self,x,diffrence,state,command):
        for i in range(10):
            circle_radius = 20
            circle_spacing = 30
            y = i * (2 * circle_radius + circle_spacing) 
            y -= diffrence
            if command==self.level:
             if state=='left':
                if i%2==0:
                    if data_get(get_user(),'Level_jadval_zarb')>abs(i-10):
                        img = ImageButton("./Assets/green.png","./Assets/green_down.png",(x,y),(82,76),abs(i-10),lambda instance:'') 
                    elif data_get(get_user(),'Level_jadval_zarb')==abs(i-10):
                        img = ImageButton("./Assets/blue.png","./Assets/blue_down.png",(x,y),(82,76),abs(i-10),lambda instance:self.level_preview(instance,command)) 
                    else:
                        img = ImageButton("./Assets/gray.png","./Assets/gray_down.png",(x,y),(82,76),abs(i-10),lambda instance:'') 
                    self.layout.add_widget(img)
             elif state=='right':
                if i%2!=0:
                    if data_get(get_user(),'Level_jadval_zarb')>abs(i-10):
                        img = ImageButton("./Assets/green.png","./Assets/green_down.png",(x,y),(82,76),abs(i-10),lambda instance:'') 
                    elif data_get(get_user(),'Level_jadval_zarb')==abs(i-10):
                        img = ImageButton("./Assets/blue.png","./Assets/blue_down.png",(x,y),(82,76),abs(i-10),lambda instance:self.level_preview(instance,command)) 
                    else:
                        img = ImageButton("./Assets/gray.png","./Assets/gray_down.png",(x,y),(82,76),abs(i-10),lambda instance:'') 
                    self.layout.add_widget(img)
            else:
             if state=='left':
                if i%2==0:
                    if data_get(get_user(),'Level_math')>abs(i-10):
                        img = ImageButton("./Assets/green.png","./Assets/green_down.png",(x,y),(82,76),abs(i-10),lambda instance:'') 
                    elif data_get(get_user(),'Level_math')==abs(i-10):
                        img = ImageButton("./Assets/blue.png","./Assets/blue_down.png",(x,y),(82,76),abs(i-10),lambda instance:self.level_preview(instance,command)) 
                    else:
                        img = ImageButton("./Assets/gray.png","./Assets/gray_down.png",(x,y),(82,76),abs(i-10),lambda instance:'') 
                    self.layout.add_widget(img)
             elif state=='right':
                if i%2!=0:
                    if data_get(get_user(),'Level_math')>abs(i-10):
                        img = ImageButton("./Assets/green.png","./Assets/green_down.png",(x,y),(82,76),abs(i-10),lambda instance:'') 
                    elif data_get(get_user(),'Level_math')==abs(i-10):
                        img = ImageButton("./Assets/blue.png","./Assets/blue_down.png",(x,y),(82,76),abs(i-10),lambda instance:self.level_preview(instance,command)) 
                    else:
                        img = ImageButton("./Assets/gray.png","./Assets/gray_down.png",(x,y),(82,76),abs(i-10),lambda instance:'') 
                    self.layout.add_widget(img)
    def math(self,instance):
        self.layout.clear_widgets()
        self.layout.size=(360,1000)
        self.layout.add_widget(BlueScreen())
        self.level_drawer(100,-100,'right',self.math_level)
        self.level_drawer(250,-100,'left',self.math_level)
        if data_get(get_user(),'Level_math')%2!=0:
            self.character=Image(source="./Assets/boy_standup.png",pos=(-90,330-(data_get(get_user(),'Level_math')//2*140)),size=(56,81))
            self.align='left'
        else:
            self.character=Image(source="./Assets/boy_standup_rtl.png",pos=(70,400-(data_get(get_user(),'Level_math')//2*140)),size=(56,81))
            self.align='right'
        self.layout.add_widget(self.character)
    def math_level(self,instance):
          self.preview.dismiss()
          self.layout.clear_widgets()
          self.layout.size=(360,1000)
          self.layout.add_widget(BlueScreen())
          self.create_math_question('easy')
          self.timer=Label(pos=(-180,380),text='30',font_size=30)
          self.correct_incorrect=Label(pos=(0,-250),text='',font_size=40)
          self.layout.add_widget(self.timer)
          self.layout.add_widget(self.correct_incorrect)
    def math_level_medium(self,instance):
          self.preview.dismiss()
          self.layout.clear_widgets()
          self.layout.size=(360,1000)
          self.layout.add_widget(BlueScreen())
          self.create_math_question('medium')
          self.timer=Label(pos=(-180,380),text='40',font_size=30)
          self.correct_incorrect=Label(pos=(0,-250),text='',font_size=40)
          self.layout.add_widget(self.timer)
          self.layout.add_widget(self.correct_incorrect)
    def math_level_hard(self,instance):
          self.preview.dismiss()
          self.layout.clear_widgets()
          self.layout.size=(360,1000)
          self.layout.add_widget(BlueScreen())
          self.create_math_question('hard')
          self.timer=Label(pos=(-180,380),text='60',font_size=30)
          self.correct_incorrect=Label(pos=(0,-250),text='',font_size=40)
          self.layout.add_widget(self.timer)
          self.layout.add_widget(self.correct_incorrect)
    def create_math_question(self,state):
          with open(f'./data/math_{state}.json','r',encoding='utf-8') as data:
            loaded=json.load(data)
          question_num=loaded[randint(0,19)]
          question=question_num['question']
          answers=[question_num['answer1'],question_num['answer2'],question_num['answer3'],question_num['answer4']]
          self.answer=convert_to_persian(question_num[question_num['correct_answer']])
          self.layout.add_widget(Label(pos=(0,300),text=convert_to_persian(question),halign='right',valign='top',font_size=25,color=(1,1,1,1)))
          self.btn1=Button(text=convert_to_persian(answers[0]),pos=(25,500),font_size=25,color=(1,1,1,1),size_hint=(None,None),size=(200,200),border=(1,1,1,1))
          self.btn2=Button(text=convert_to_persian(answers[1]),pos=(225,500),font_size=25,color=(1,1,1,1),size_hint=(None,None),size=(200,200),border=(1,1,1,1))
          self.btn3=Button(text=convert_to_persian(answers[2]),pos=(25,300),font_size=25,color=(1,1,1,1),size_hint=(None,None),size=(200,200),border=(1,1,1,1))
          self.btn4=Button(text=convert_to_persian(answers[3]),pos=(225,300),font_size=25,color=(1,1,1,1),size_hint=(None,None),size=(200,200),border=(1,1,1,1))
          self.btn1.bind(on_press=self.choice_math)
          self.btn2.bind(on_press=self.choice_math)
          self.btn3.bind(on_press=self.choice_math)
          self.btn4.bind(on_press=self.choice_math)
          self.layout.add_widget(self.btn1)
          self.layout.add_widget(self.btn2)
          self.layout.add_widget(self.btn3)
          self.layout.add_widget(self.btn4)
          self.timer_loop=Clock.schedule_interval(self.update_math,1)
    def choice_math(self,instance):
        if instance.text==self.answer:
            self.correct_incorrect.text=convert_to_persian('درست')
            instance.background_color=(0,1,0,1)
            self.correct_sound.play()
            self.btn1.unbind(on_press=self.choice_math)
            self.btn2.unbind(on_press=self.choice_math)
            self.btn3.unbind(on_press=self.choice_math)
            self.btn4.unbind(on_press=self.choice_math)
            Clock.unschedule(self.timer_loop)
            self.correct+=1
            self.questions_count-=1
        else:
            self.correct_incorrect.text=convert_to_persian('نادرست')
            instance.background_color=(1,0,0,1)
            self.wrong_sound.play()
            self.btn1.unbind(on_press=self.choice_math)
            self.btn2.unbind(on_press=self.choice_math)
            self.btn3.unbind(on_press=self.choice_math)
            self.btn4.unbind(on_press=self.choice_math)
            Clock.unschedule(self.timer_loop)
            self.incorrect+=1
            self.questions_count-=1
        if self.questions_count==0:
            self.layout.clear_widgets()
            self.layout.size=(360,1000)
            self.layout.add_widget(BlueScreen())
            self.layout.add_widget(Label(text=convert_to_persian('مرحله به پایان رسید'),pos=(0,300),font_size=38,color=(0,0,0,1)))
            self.layout.add_widget(Label(text=str(self.correct)+convert_to_persian('پاسخ های درست:'),pos=(0,100),font_size=25))
            self.layout.add_widget(Label(text=str(self.incorrect)+convert_to_persian('پاسخ های نادرست:'),pos=(0,50),font_size=25))
            self.layout.add_widget(Label(text=str(self.correct*3)+convert_to_persian('مقدار سکه:'),pos=(0,0),font_size=25))
            self.layout.add_widget(Label(text=str(self.correct*5)+convert_to_persian('مقدار امتیاز:'),pos=(0,-50),font_size=25))
            self.layout.add_widget(Button(text=convert_to_persian('خروج'),pos=(125,350),size_hint=(None,None),size=(200,50),font_size=25,on_press=self.math))
            data_edit(get_user(),'Coin',int(data_get(get_user(),'Coin'))+self.correct*3)
            data_edit(get_user(),'XP',int(data_get(get_user(),'XP'))+self.correct*5)
            if data_get(get_user(),'Level_math')<10:
                data_edit(get_user(),'Level_math',int(data_get(get_user(),'Level_math'))+1)
            else:
                data_edit(get_user(),'Level_math',10)
            self.correct=0
            self.incorrect=0
            self.questions_count=10
            Clock.unschedule(self.timer_loop)
        else:Clock.schedule_once(self.math_level,1)
    def update_math(self,dt):
        if self.timer.text=='1':
            Clock.unschedule(self.timer_loop)
            self.incorrect+=1
            self.btn1.unbind(on_press=self.choice_math)
            self.btn2.unbind(on_press=self.choice_math)
            self.btn3.unbind(on_press=self.choice_math)
            self.btn4.unbind(on_press=self.choice_math)
            self.questions_count-=1
            if self.questions_count==0:
                self.layout.clear_widgets()
                self.layout.size=(360,1000)
                self.layout.add_widget(BlueScreen())
                self.layout.add_widget(Label(text=convert_to_persian('مرحله به پایان رسید'),pos=(0,300),font_size=38,color=(0,0,0,1)))
                self.layout.add_widget(Label(text=str(self.correct)+convert_to_persian('پاسخ های درست:'),pos=(0,100),font_size=25))
                self.layout.add_widget(Label(text=str(self.incorrect)+convert_to_persian('پاسخ های نادرست:'),pos=(0,50),font_size=25))
                self.layout.add_widget(Label(text=str(self.correct*3)+convert_to_persian('مقدار سکه:'),pos=(0,0),font_size=25))
                self.layout.add_widget(Label(text=str(self.correct*5)+convert_to_persian('مقدار امتیاز:'),pos=(0,-50),font_size=25))
                self.layout.add_widget(Button(text=convert_to_persian('خروج'),pos=(125,350),size_hint=(None,None),size=(200,50),font_size=25,on_press=self.math))
                data_edit(get_user(),'Coin',int(data_get(get_user(),'Coin'))+self.correct*3)
                data_edit(get_user(),'XP',int(data_get(get_user(),'XP'))+self.correct*5)
                if data_get(get_user(),'Level_math')<10:
                    data_edit(get_user(),'Level_math',int(data_get(get_user(),'Level_math'))+1)
                else:
                    data_edit(get_user(),'Level_math',10)
                self.correct=0
                self.incorrect=0
                self.questions_count=10
            else:Clock.schedule_once(self.math_level,1)
        elif self.timer.text!='1':
            self.timer.text= str(int(self.timer.text)-1)
    def user_picture(self,instance): 
        content=FloatLayout()
        self.user_popup=Popup(title=convert_to_persian("تغییر عکس"), content=content, size_hint=(None, None), size=(450, 500))
        self.user_popup.open()
        content.add_widget(Label(text=convert_to_persian('عکس پروفایل خود را تغییر دهید:'),pos=(20,350),font_size=30,color=(0,0,1,1)))
        self.cam=Camera(play=True,pos=(100,250),size_hint=(None,None),size=(240,360))
        content.add_widget(self.cam)
        content.add_widget(Button(text='',color=(0,1,1,1),font_size=40,halign='center',valign='top',size_hint=(None, None),size=(50,50),pos=(395,595),on_press=self.user_popup.dismiss))
        content.add_widget(Label(text='×', pos=(211, 407), font_size=40, color=(1, 1, 1, 1)))
        content.add_widget(Button(text=convert_to_persian('ذخیره'),color=(0,1,1,1),size_hint=(None, None),size=(100,50),pos=(175,200),on_press=self.save_pic))
    def save_pic(self,instance):
        self.cam.export_to_png(os.path.expanduser('~')+'/AppData/Local/systemfilesforwin/user_pic.png')    
    def Tab2_drawer(self,instance):
        if self.timer_loop:
            Clock.unschedule(self.timer_loop)
        if self.timer_loop_color:
            Clock.unschedule(self.timer_loop_color)
        self.layout.unbind(on_touch_down=self.place)
        self.layout.clear_widgets()
        self.layout.size=(360,1500)
        self.layout.add_widget(BlueScreen())
        self.layout.add_widget(Label(text=convert_to_persian('بازی های کوچک'),pos=(0,600),font_size=60,color=(0,0,0,1)))
        with self.layout.canvas:
            Color(0, 0, 0, 1)
            Line(rectangle=(0, 900, 460, 0), width=2)
        self.layout.add_widget(Button(text=convert_to_persian('مار و پله'), color=(0, 1, 1, 1), size_hint=(None, None), size=(400, 100), pos=(25, 1200), on_press=self.snake_level))
        self.layout.add_widget(Button(text=convert_to_persian('دوز'), color=(0, 1, 1, 1), size_hint=(None, None), size=(400, 100), pos=(25, 1100), on_press=self.tic_tac_toe_level))
        self.layout.add_widget(Button(text=convert_to_persian('تشخیص رنگ'), color=(0, 1, 1, 1), size_hint=(None, None), size=(400, 100), pos=(25, 1000), on_press=self.color_level))
    def Tab3_drawer(self, instance):
        if self.timer_loop:
            Clock.unschedule(self.timer_loop)
        if self.timer_loop_color:
            Clock.unschedule(self.timer_loop_color)
        self.layout.unbind(on_touch_down=self.place)
        self.layout.clear_widgets()
        self.layout.size=(360,2000)
        self.layout.add_widget(BlueScreen())
        coins_layout=FloatLayout()
        boosters_layout=FloatLayout()
        panel=TabbedPanel(do_default_tab=False,tab_pos='top_mid',pos=(0,0),size_hint=(None, None),size=(460,1800),background_color=(0,0,1,0))
        panel.add_widget(TabbedPanelItem(text=convert_to_persian('سکه'), content=coins_layout))
        panel.add_widget(TabbedPanelItem(text=convert_to_persian('تقویت کننده \n (بزودی)'), content=boosters_layout))
        self.layout.add_widget(panel)
        self.layout.add_widget(Label(text=convert_to_persian('فروشگاه'),pos=(0,875),font_size=55,color=(0,0,0,1)))
        self.layout.add_widget(Label(text=convert_to_persian('(به زودی با درگاه پرداخت)'),pos=(0,825),font_size=55,color=(0,0,0,1)))
        coins_layout.add_widget(Product('100 امتیاز','بسته مبتدی',(50,1500),(360,200),' 100 هزار تومان '))
        coins_layout.add_widget(Product('200 امتیاز','بسته متوسط',(50,1200),(360,200),'200 هزار تومان'))
        coins_layout.add_widget(Product('300 امتیاز','بسته محبوب',(50,900),(360,200),'400 هزار تومان'))
        coins_layout.add_widget(Product('600 امتیاز','بسته شگفت انگیز',(50,600),(360,200),'600 هزار تومان'))
        boosters_layout.add_widget(Product('زمان+','پنج دقیقه زمان برای سوالات',(50,1500),(360,200),'50 سکه'))
        boosters_layout.add_widget(Product('50-50','حذف کردن دو گزینه نادرست',(50,1200),(360,200),'100 سکه'))
        boosters_layout.add_widget(Product('پرش','پرش از پنج سوال',(50,900),(360,200),'200 سکه'))
        boosters_layout.add_widget(Product('4 برابر','چهار برابر کردن امتیاز',(50,600),(360,200),'300 سکه'))
    def Tab4_drawer(self,instance):
        if self.timer_loop:
            Clock.unschedule(self.timer_loop)
        if self.timer_loop_color:
            Clock.unschedule(self.timer_loop_color)
        self.layout.unbind(on_touch_down=self.place)
        self.layout.clear_widgets()
        self.layout.size=(360,2000)
        self.layout.add_widget(BlueScreen())
        self.layout.add_widget(Label(text=convert_to_persian('مشخصات کاربر'),pos=(0,800),font_size=60,color=(0,0,0,1)))
        self.layout.add_widget(Label(text=str(data_get(get_user(),'Level_math'))+convert_to_persian('مرحله در ریاضی: '),pos=(0,700),font_size=30))
        self.layout.add_widget(Label(text=str(data_get(get_user(),'Level_jadval_zarb'))+convert_to_persian('مرحله در جدول ضرب: '),pos=(0,650),font_size=30))
        self.layout.add_widget(Label(text=str(data_get(get_user(),'XP'))+convert_to_persian('امتیاز: '),pos=(0,550),font_size=30))
        self.layout.add_widget(Label(text=str(data_get(get_user(),'Coin'))+convert_to_persian('سکه: '),pos=(0,500),font_size=30)) 
        with self.layout.canvas:
            Color(0, 0, 0, 1)
            Line(rectangle=(0, 1450, 460, 0), width=2)
        self.layout.add_widget(Label(text=convert_to_persian('تنظیمات'),pos=(0,350),font_size=60,color=(0,0,0,1)))
        self.layout.add_widget(Label(text=convert_to_persian('میزان صدای موسیقی'),pos=(0,200),font_size=30))
        self.layout.add_widget(Label(text=convert_to_persian('میزان صدای درست'),pos=(0,50),font_size=30))
        self.layout.add_widget(Label(text=convert_to_persian('میزان صدای نادرست'),pos=(0,-100),font_size=30))
        music_volume=Slider(pos=(25,1100),min=0, max=100,step=1,value=self.Music.volume*100,size=(400,50),size_hint=(None,None))
        correct_volume=Slider(pos=(25,950),min=0, max=100,step=1,value=self.correct_sound.volume*100,size=(400,50),size_hint=(None,None))
        wrong_volume=Slider(pos=(25,800),min=0, max=100,step=1,value=self.wrong_sound.volume*100,size=(400,50),size_hint=(None,None))
        music_volume.bind(value=lambda instance,value: setattr(self.Music,"volume",value / 100))
        correct_volume.bind(value=lambda instance,value: setattr(self.correct_sound,"volume",value / 100))
        wrong_volume.bind(value=lambda  instance,value: setattr(self.wrong_sound,"volume",value / 100))
        self.layout.add_widget(music_volume)
        self.layout.add_widget(correct_volume)
        self.layout.add_widget(wrong_volume)
        with self.layout.canvas:
            Color(0, 0, 0, 1)
            Line(rectangle=(0, 750, 460, 0), width=2)
        self.layout.add_widget(Label(text=convert_to_persian('مدیریت کاربران (بزودی)'),pos=(0,-300),font_size=60,color=(0,0,0,1)))
        choose=Spinner(text=convert_to_persian('انتخاب کاربر پیشفرض'),pos=(25,400),size_hint=(None,None),size=(300,100))
        entry=TextInput(hint_text=convert_to_persian('نام کاربر'), size_hint=(None, None), size=(300, 100), pos=(25, 500))
        self.layout.add_widget(entry)
        self.layout.add_widget(Button(text=convert_to_persian('اضافه کردن'),color=(0, 1, 1, 1), size_hint=(None, None), size=(100, 50), pos=(325, 550)))
        self.layout.add_widget(Button(text=convert_to_persian('حذف کردن'),color=(0, 1, 1, 1), size_hint=(None, None), size=(100, 50), pos=(325, 500)))
        self.layout.add_widget(choose)
    def Tabs_drawer(self):
        img=ImageButton("./Assets/level.jpg","./Assets/level.jpg",(0,0),(150,99),'',self.Main_build)
        self.tabs.add_widget(img)
        img=ImageButton("./Assets/game.png","./Assets/game.png",(150,0),(101,99),'',self.Tab2_drawer)
        self.tabs.add_widget(img)
        img=ImageButton("./Assets/shop.jpg","./Assets/shop.jpg",(251,0),(99,99),'',self.Tab3_drawer)
        self.tabs.add_widget(img)
        img=ImageButton("./Assets/setting.jpg","./Assets/setting.jpg",(350,0),(99,99),'',self.Tab4_drawer)
        self.tabs.add_widget(img)
    def level_preview(self,instance,command):
          content=FloatLayout()
          original_levels=[1,4,7,10,13,16,19,22,25,28,31,34,37,40,43,46,49]
          speed_levels=[2,5,8,11,14,17,20,23,26,29,32,35,38,41,44,47,50]
          challenge_levels=[3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51]
          if command==self.level:
            if data_get(get_user(),'Level_jadval_zarb') in original_levels:
                self.preview=Popup(title=convert_to_persian('(مرحله معمولی)')+str(data_get(get_user(),'Level_jadval_zarb'))+convert_to_persian('مرحله '),title_size='25',content=content, size_hint=(None, None), size=(450, 500))
                content.add_widget(Button(text=convert_to_persian('شروع'),font_size=30,color=(0,1,1,1),size_hint=(None, None),size=(400,50),pos=(25,200),on_press=self.level))
            elif data_get(get_user(),'Level_jadval_zarb') in speed_levels:
                self.preview=Popup(title=convert_to_persian('(مرحله سرعتی)')+str(data_get(get_user(),'Level_jadval_zarb'))+convert_to_persian('مرحله '), content=content, size_hint=(None, None), size=(450, 500))
                content.add_widget(Button(text=convert_to_persian('شروع'),font_size=30,color=(0,1,1,1),size_hint=(None, None),size=(400,50),pos=(25,200),on_press=self.speed_level))
            elif data_get(get_user(),'Level_jadval_zarb') in challenge_levels:
                self.preview=Popup(title=convert_to_persian('(مرحله چالشی)')+str(data_get(get_user(),'Level_jadval_zarb'))+convert_to_persian('مرحله '), content=content, size_hint=(None, None), size=(450, 500))
                content.add_widget(Button(text=convert_to_persian('شروع'),font_size=30,color=(0,1,1,1),size_hint=(None, None),size=(400,50),pos=(25,200),on_press=self.challenge_level))
          elif command==self.math_level:
            if data_get(get_user(),'Level_math') in original_levels:
                self.preview=Popup(title=convert_to_persian('(مرحله آسان)')+str(data_get(get_user(),'Level_math'))+convert_to_persian('مرحله '),title_size='25',content=content, size_hint=(None, None), size=(450, 500))
                content.add_widget(Button(text=convert_to_persian('شروع'),font_size=30,color=(0,1,1,1),size_hint=(None, None),size=(400,50),pos=(25,200),on_press=self.math_level))
            elif data_get(get_user(),'Level_math') in speed_levels:
                self.preview=Popup(title=convert_to_persian('(مرحله متوسط)')+str(data_get(get_user(),'Level_math'))+convert_to_persian('مرحله '), content=content, size_hint=(None, None), size=(450, 500))
                content.add_widget(Button(text=convert_to_persian('شروع'),font_size=30,color=(0,1,1,1),size_hint=(None, None),size=(400,50),pos=(25,200),on_press=self.math_level_medium))
            elif data_get(get_user(),'Level_math') in challenge_levels:
                self.preview=Popup(title=convert_to_persian('(مرحله دشوار)')+str(data_get(get_user(),'Level_math'))+convert_to_persian('مرحله '), content=content, size_hint=(None, None), size=(450, 500))
                content.add_widget(Button(text=convert_to_persian('شروع'),font_size=30,color=(0,1,1,1),size_hint=(None, None),size=(400,50),pos=(25,200),on_press=self.math_level_hard))
          self.preview.open()
          content.add_widget(Label(text=convert_to_persian('تقویت کننده ها (بزودی):'),pos=(20,350),font_size=30,color=(1,1,1,1)))
          content.add_widget(ToggleButton(text=convert_to_persian('زمان+'),color=(1,1,1,1),size_hint=(None, None),size=(400,50),pos=(25,450),on_press=lambda instance:''))
          content.add_widget(ToggleButton(text=convert_to_persian('50-50'),color=(1,1,1,1),size_hint=(None, None),size=(400,50),pos=(25,400),on_press=lambda instance:''))
          content.add_widget(ToggleButton(text=convert_to_persian('پرش'),color=(1,1,1,1),size_hint=(None, None),size=(400,50),pos=(25,350),on_press=lambda instance:''))
          content.add_widget(ToggleButton(text=convert_to_persian('4 برابر'),color=(1,1,1,1),size_hint=(None, None),size=(400,50),pos=(25,300),on_press=lambda instance:''))
          content.add_widget(Button(text='',font_size=40,halign='center',valign='top',size_hint=(None, None),size=(50,50),pos=(395,595),on_press=self.preview.dismiss))
          content.add_widget(Label(text='X', pos=(211, 407),font_name='Arial', font_size=40, color=(1, 1, 1, 1)))
    def create_question(self,command):
          numbers=[self.num1,self.num2,self.num1*self.num2]
          rand=randint(1,3)
          if rand==1:
             self.layout.add_widget(Label(pos=(0,300),text='[] * '+str(numbers[1])+' = '+str(numbers[2]),font_size=60,color=(0,0,0,1)))
             self.ans=numbers[0]
          elif rand==2:
             self.layout.add_widget(Label(pos=(0,300),text=str(numbers[0])+' * [] = '+str(numbers[2]),font_size=60,color=(0,0,0,1)))
             self.ans=numbers[1]
          elif rand==3:
             self.layout.add_widget(Label(pos=(0,300),text=str(numbers[0])+' * '+str(numbers[1])+' = []',font_size=60,color=(0,0,0,1)))
             self.ans=numbers[2]
          rand=randint(1,3) 
          self.instancebtn=lambda instance:self.choice(instance,command)
          if rand==1:
             while True:
                 self.txt1num=str(self.ans)
                 self.btn1=Button(text=self.txt1num,pos=(75,500),font_size=50,color=(0,0,0,1),size_hint=(None,None),size=(100,100))
                 self.btn1.bind(on_press=self.instancebtn)
                 self.layout.add_widget(self.btn1)
                 self.txt2num=str(randint(0,10))
                 if self.txt2num!=self.txt1num:
                    self.btn2=Button(text=self.txt2num,pos=(175,500),font_size=50,color=(0,0,0,1),size_hint=(None,None),size=(100,100))
                    self.btn2.bind(on_press=self.instancebtn)
                    self.layout.add_widget(self.btn2)
                    self.txt3num=str(randint(0,10))
                 else:continue
                 if self.txt3num!=self.txt2num and self.txt3num!=self.txt1num:
                    self.btn3=Button(text=self.txt3num,pos=(275,500),font_size=50,color=(0,0,0,1),size_hint=(None,None),size=(100,100))
                    self.btn3.bind(on_press=self.instancebtn)
                    self.layout.add_widget(self.btn3)
                    break
                 else:continue 
          elif rand==2:
             while True:
                 self.txt2num=str(self.ans)
                 self.btn2=Button(text=self.txt2num,pos=(175,500),font_size=50,color=(0,0,0,1),size_hint=(None,None),size=(100,100))
                 self.btn2.bind(on_press=self.instancebtn)
                 self.layout.add_widget(self.btn2)
                 self.txt1num=str(randint(0,10))
                 if self.txt1num!=self.txt2num:
                    self.btn1=Button(text=self.txt1num,pos=(75,500),font_size=50,color=(0,0,0,1),size_hint=(None,None),size=(100,100))
                    self.btn1.bind(on_press=self.instancebtn)
                    self.layout.add_widget(self.btn1)
                    self.txt3num=str(randint(0,10))
                 else:continue
                 if self.txt3num!=self.txt2num and self.txt3num!=self.txt1num:
                    self.btn3=Button(text=self.txt3num,pos=(275,500),font_size=50,color=(0,0,0,1),size_hint=(None,None),size=(100,100))
                    self.btn3.bind(on_press=self.instancebtn)
                    self.layout.add_widget(self.btn3)
                    break
                 else:continue 
          elif rand==3:
             while True:
                 self.txt3num=str(self.ans)
                 self.btn3=Button(text=self.txt3num,pos=(275,500),font_size=50,color=(0,0,0,1),size_hint=(None,None),size=(100,100))
                 self.btn3.bind(on_press=self.instancebtn)
                 self.layout.add_widget(self.btn3)
                 self.txt2num=str(randint(0,10))
                 if self.txt2num!=self.txt3num:
                    self.btn2=Button(text=self.txt2num,pos=(175,500),font_size=50,color=(0,0,0,1),size_hint=(None,None),size=(100,100))
                    self.btn2.bind(on_press=self.instancebtn)
                    self.layout.add_widget(self.btn2)
                    self.txt1num=str(randint(0,10))
                 else:continue 
                 if self.txt1num!=self.txt2num and self.txt1num!=self.txt3num:
                    self.btn1=Button(text=self.txt1num,pos=(75,500),font_size=50,color=(0,0,0,1),size_hint=(None,None),size=(100,100))
                    self.btn1.bind(on_press=self.instancebtn)
                    self.layout.add_widget(self.btn1)
                    break
                 else:continue
    def level(self,instance):
          self.preview.dismiss()
          self.layout.clear_widgets()
          self.layout.size=(360,1000)
          self.num1=randint(1,10)
          self.num2=randint(1,10)
          self.layout.add_widget(BlueScreen())
          self.create_question(self.level)
          self.timer=Label(pos=(-180,380),text='5',font_size=30)
          self.correct_incorrect=Label(pos=(0,-100),text='',font_size=40)
          self.layout.add_widget(self.timer)
          self.layout.add_widget(self.correct_incorrect)
          self.timer_loop=Clock.schedule_interval(lambda dt:self.update_timer(dt,self.level),1)
    def speed_level(self,instance):
          self.preview.dismiss() 
          self.layout.clear_widgets()
          self.layout.size=(360,1000)
          self.layout.add_widget(BlueScreen())
          self.num1=randint(1,10)
          self.num2=randint(1,10)
          self.create_question(self.speed_level)
          self.timer=Label(pos=(-180,380),text='3',font_size=30)
          self.correct_incorrect=Label(pos=(0,-100),text='',font_size=40)
          self.layout.add_widget(self.timer)
          self.layout.add_widget(self.correct_incorrect)
          self.timer_loop=Clock.schedule_interval(lambda dt:self.update_timer(dt,self.speed_level),1)
    def challenge_level(self,instance):
          self.preview.dismiss()
          self.layout.clear_widgets()
          self.layout.size=(360,1000)
          self.layout.add_widget(BlueScreen())
          self.num1=randint(10,15)
          self.num2=randint(10,15)
          self.create_question(self.challenge_level)
          self.timer=Label(pos=(-180,380),text='15',font_size=30)
          self.correct_incorrect=Label(pos=(0,-100),text='',font_size=40)
          self.layout.add_widget(self.timer)
          self.layout.add_widget(self.correct_incorrect)
          self.timer_loop=Clock.schedule_interval(lambda dt:self.update_timer(dt,self.challenge_level),1)
    def snake_level(self, instance):
        self.layout.clear_widgets()
        self.layout.size = (360, 1000)
        self.layout.add_widget(BlueScreen())
        img = Image(source='./Assets/snakes-and-ladders.jpg', pos=(0, 355), size_hint=(None, None), size=(450, 640))
        self.player1=Image(source='./Assets/Player1.png', pos=(10,447), size_hint=(None, None), size=(29, 66))
        self.player2=Image(source='./Assets/Player2.png', pos=(20,447), size_hint=(None, None), size=(29, 66))
        self.button = Button(text=convert_to_persian('تاس بنداز!') , color=(0, 1, 1, 1), size_hint=(None, None), size=(300, 50), pos=(75, 200), on_press=self.turn_changer)
        self.turn = Label(text=convert_to_persian('نوبت: بازیکن اول'), pos=(0, -200), font_size=40, color=(0, 0, 0, 1), markup=True)
        self.layout.add_widget(img)
        self.layout.add_widget(self.player1)
        self.layout.add_widget(self.player2)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.turn)
    def turn_changer(self,instance):
        dicen=randint(1,6)
        if self.player1.pos[0]<=10 and self.player1.pos[1]==834:return True
        elif self.player2.pos[0]<=20 and self.player2.pos[1]==834:return True
        self.button.unbind(on_press=self.turn_changer)
        Clock.schedule_once(lambda dt:self.button.bind(on_press=self.turn_changer),0.3*dicen)
        with self.layout.canvas:
            Color(0,0,1,1)
            Rectangle(pos=(170,320),size=(100,100))
        img=Image(source=f'./Assets/dice{dicen}.png', pos=(170,320), size_hint=(None, None), size=(10,10))
        self.layout.add_widget(img)
        anim=Animation(size=(100,100),duration=0.5)
        anim.start(img)
        up_positions_player1={(397,447):(397,490),(10,490):(10,533),(397,533):(397,576),(10,576):(10,619),(397,619):(397,662),(10,662):(10,705),(397,705):(397,748),(10,748):(10,791),(397,791):(397,834)}  
        ladder_positions_player1={(96,447):(53,533),(397,447):(354,533),(182,533):(225,619),(397,619):(354,705),(53,662):(96,834),(139,705):(182,791)}
        snake_positions_player1={(311,533):(354,447),(53,619):(182,490),(311,619):(225,490),(225,705):(96,662),(354,834):(354,748),(268,834):(311,705)}#(311,834):(354,705),(268,533):(354,447),(10,619):(182,490),(268,619):(225,490),(182,705):(96,662),(397,834):(354,748)}
        right_positions=(447,533,619,705,791,877,963)
        up_positions_player2 = {(407, 447): (407, 490),(20, 490): (20, 533),(407, 533): (407, 576),(20, 576): (20, 619),(407, 619): (407, 662),(20, 662): (20, 705),(407, 705): (407, 748),(20, 748): (20, 791),(407, 791): (407, 834)}
        ladder_positions_player2 = {(106, 447): (63, 533),(407, 447): (364, 533),(192, 533): (235, 619),(407, 619): (364, 705),(63, 662): (106, 834),(149, 705): (192, 791)}
        snake_positions_player2 = {(321, 533): (364, 447),(63, 619): (192, 490),(321, 619): (235, 490),(235, 705): (106, 662),(364, 834): (364, 748),(278, 834): (321, 705)}
        if self.turn.text==convert_to_persian('نوبت: بازیکن اول'):
            def move_step(i):
                if self.player1.pos[0]<=10 and self.player1.pos[1]==834:return True
                elif self.player2.pos[0]<=20 and self.player2.pos[1]==834:return True
                if i >= dicen:
                    for key, value in ladder_positions_player1.items():
                        if list(self.player1.pos) == [key[0], key[1]]:
                            Animation(pos=value, duration=0.2).start(self.player1)
                    for key, value in snake_positions_player1.items():
                        if list(self.player1.pos) == [key[0], key[1]]:
                            Animation(pos=value, duration=0.2).start(self.player1)
                    return
                for key, value in up_positions_player1.items():
                    if list(self.player1.pos) == [key[0], key[1]]:
                        anim = Animation(pos=value, duration=0.2)
                        anim.bind(on_complete=lambda *a: move_step(i+1))
                        anim.start(self.player1)
                        return
                if self.player1.pos[1] in right_positions:
                    new_pos = (self.player1.pos[0]+43, self.player1.pos[1])
                else:
                    new_pos = (self.player1.pos[0]-43, self.player1.pos[1])
                anim = Animation(pos=new_pos, duration=0.2)
                anim.bind(on_complete=lambda *a: move_step(i+1))
                anim.start(self.player1)
            move_step(0)
        else:
            def move_step(i):
                if self.player1.pos[0]<=10 and self.player1.pos[1]==834:return True
                elif self.player2.pos[0]<=20 and self.player2.pos[1]==834:return True
                if i >= dicen:
                    for key, value in ladder_positions_player2.items():
                        if list(self.player2.pos) == [key[0], key[1]]:
                            Animation(pos=value, duration=0.2).start(self.player2)
                    for key, value in snake_positions_player2.items():
                        if list(self.player2.pos) == [key[0], key[1]]:
                            Animation(pos=value, duration=0.2).start(self.player2)
                    return
                for key, value in up_positions_player2.items():
                    if list(self.player2.pos) == [key[0], key[1]]:
                        anim = Animation(pos=value, duration=0.2)
                        anim.bind(on_complete=lambda *a: move_step(i+1))
                        anim.start(self.player2)
                        return
                if self.player2.pos[1] in right_positions:
                    new_pos = (self.player2.pos[0]+43, self.player2.pos[1])
                else:
                    new_pos = (self.player2.pos[0]-43, self.player2.pos[1])
                anim = Animation(pos=new_pos, duration=0.2)
                anim.bind(on_complete=lambda *a: move_step(i+1))
                anim.start(self.player2)
            move_step(0)
        if dicen!=6:
            self.turn.text = convert_to_persian('نوبت: بازیکن دوم') if self.turn.text == convert_to_persian('نوبت: بازیکن اول') else convert_to_persian('نوبت: بازیکن اول')
    def tic_tac_toe_level(self, instance):
        self.layout.clear_widgets()
        self.layout.size = (360, 1000)
        self.layout.add_widget(BlueScreen())
        img = Image(source='./Assets/Tic-tac-toe-Game-Board.jpg', pos=(0, 480), size_hint=(None, None), size=(450, 400))
        self.layout.add_widget(img)
        self.layout.bind(on_touch_down=self.place)
        self.turn_x_o=Label(text=convert_to_persian('نوبت: بازیکن اول'),pos=(0,-200),font_size=40)
        self.layout.add_widget(self.turn_x_o)
        self.unavailable_positions_o=[]
        self.unavailable_positions_x=[]
        self.end=False
    def place(self, instance, touch):
     if self.end==False:
        marker=None
        cell_width = 120
        cell_height = 120
        x_offset = 60
        y_offset = 500
        for row in range(3):
            for col in range(3):
               x_min = x_offset + col * cell_width
               x_max = x_min + cell_width
               y_min = y_offset + (2 - row) * cell_height
               y_max = y_min + cell_height
               if x_min <= touch.pos[0] <= x_max and y_min <= touch.pos[1] <= y_max:
                if (row,col) not in self.unavailable_positions_x and (row,col) not in self.unavailable_positions_o:
                    if self.turn_x_o.text == convert_to_persian('نوبت: بازیکن اول'):
                        self.unavailable_positions_x.append((row,col))
                        marker = Label(
                        text='X',
                        pos=(x_min + cell_width // 2 - 80, y_min + cell_height // 2 - 80),
                        size_hint=(None, None),
                        size=(cell_width, cell_height),
                        font_size=50,
                        color=(1, 0, 0, 1),
                        halign='center',
                        valign='middle',
                        font_name='Arial'
                        )
                    else:
                        self.unavailable_positions_o.append((row,col))
                        marker = Label(
                        text='O', 
                        pos=(x_min + cell_width // 2 - 80, y_min + cell_height // 2 - 80),
                        size_hint=(None, None),
                        size=(cell_width, cell_height),
                        font_size=50,
                        color=(1, 0, 0, 1),
                        halign='center',
                        valign='middle',
                        font_name='Arial'
                        )
                    marker.text_size = (cell_width, cell_height)
                    self.layout.add_widget(marker)
                    self.turn_x_o.text = convert_to_persian('نوبت: بازیکن دوم') if self.turn_x_o.text == convert_to_persian('نوبت: بازیکن اول') else convert_to_persian('نوبت: بازیکن اول')
        if (2,0) in self.unavailable_positions_x and (1,1) in self.unavailable_positions_x and (0,2) in self.unavailable_positions_x:
            self.turn_x_o.text=convert_to_persian('بازیکن اول برنده شد')
            self.end=True
            return True
        elif (2,2) in self.unavailable_positions_x and (1,1) in self.unavailable_positions_x and (0,0) in self.unavailable_positions_x:
            self.turn_x_o.text=convert_to_persian('بازیکن اول برنده شد')
            self.end=True
            return True
        elif (2,0) in self.unavailable_positions_x and (1,0) in self.unavailable_positions_x and (0,0) in self.unavailable_positions_x:
            self.turn_x_o.text=convert_to_persian('بازیکن اول برنده شد')
            self.end=True
            return True
        elif (2,0) in self.unavailable_positions_x and (2,1) in self.unavailable_positions_x and (2,2) in self.unavailable_positions_x:
            self.turn_x_o.text=convert_to_persian('بازیکن اول برنده شد')
            self.end=True
            return True
        elif (2,2) in self.unavailable_positions_x and (1,2) in self.unavailable_positions_x and (0,2) in self.unavailable_positions_x:
            self.turn_x_o.text=convert_to_persian('بازیکن اول برنده شد')
            self.end=True
            return True
        elif (0,0) in self.unavailable_positions_x and (0,1) in self.unavailable_positions_x and (0,2) in self.unavailable_positions_x:
            self.turn_x_o.text=convert_to_persian('بازیکن اول برنده شد')
            self.end=True
            return True
        elif (2,1) in self.unavailable_positions_x and (1,1) in self.unavailable_positions_x and (0,1) in self.unavailable_positions_x:
            self.turn_x_o.text=convert_to_persian('بازیکن اول برنده شد')
            self.end=True
            return True
        elif (1,0) in self.unavailable_positions_x and (1,1) in self.unavailable_positions_x and (1,2) in self.unavailable_positions_x:
            self.turn_x_o.text=convert_to_persian('بازیکن اول برنده شد')
            self.end=True
            return True
        
        elif (2,0) in self.unavailable_positions_o and (1,1) in self.unavailable_positions_o and (0,2) in self.unavailable_positions_o:
            self.turn_x_o.text=convert_to_persian('بازیکن دوم برنده شد')
            self.end=True
            return True
        elif (2,2) in self.unavailable_positions_o and (1,1) in self.unavailable_positions_o and (0,0) in self.unavailable_positions_o:
            self.turn_x_o.text=convert_to_persian('بازیکن دوم برنده شد')
            self.end=True
            return True
        elif (2,0) in self.unavailable_positions_o and (1,0) in self.unavailable_positions_o and (0,0) in self.unavailable_positions_o:
            self.turn_x_o.text=convert_to_persian('بازیکن دوم برنده شد')
            self.end=True
            return True
        elif (2,0) in self.unavailable_positions_o and (2,1) in self.unavailable_positions_o and (2,2) in self.unavailable_positions_o:
            self.turn_x_o.text=convert_to_persian('بازیکن دوم برنده شد')
            self.end=True
            return True
        elif (2,2) in self.unavailable_positions_o and (1,2) in self.unavailable_positions_o and (0,2) in self.unavailable_positions_o:
            self.turn_x_o.text=convert_to_persian('بازیکن دوم برنده شد')
            self.end=True
            return True
        elif (0,0) in self.unavailable_positions_o and (0,1) in self.unavailable_positions_o and (0,2) in self.unavailable_positions_o:
            self.turn_x_o.text=convert_to_persian('بازیکن دوم برنده شد')
            self.end=True
            return True
        elif (2,1) in self.unavailable_positions_o and (1,1) in self.unavailable_positions_o and (0,1) in self.unavailable_positions_o:
            self.turn_x_o.text=convert_to_persian('بازیکن دوم برنده شد')
            self.end=True
            return True
        elif (1,0) in self.unavailable_positions_o and (1,1) in self.unavailable_positions_o and (1,2) in self.unavailable_positions_o:
            self.turn_x_o.text=convert_to_persian('بازیکن دوم برنده شد')
            self.end=True
            return True
        if len(self.unavailable_positions_x)+len(self.unavailable_positions_o) ==9:
            self.turn_x_o.text=convert_to_persian('مساوی')
            self.end=True
    def color_level(self,instance):
        self.layout.clear_widgets()
        self.layout.size=(360,1000)
        self.layout.add_widget(BlueScreen())
        colors = [
            (0, 0, 0, 1),      
            (1, 1, 1, 1),      
            (1, 0, 0, 1),      
            (0, 1, 0, 1),      
            (1, 1, 0, 1),      
            (0, 1, 1, 1),      
            (1, 0, 1, 1),      
            (0.5, 0.5, 0.5, 1),
            (1, 0.5, 0, 1)     
        ]
        colors_names = [
        'مشکی',
        'سفید',
        'قرمز',
        'سبز',
        'زرد',
        'فیروزه‌ای',
        'ارغوانی',
        'خاکستری',
        'نارنجی'
        ]
        while True:
            rand=randint(0,8)
            with self.layout.canvas:
                Color(*colors[rand])
                Rectangle(pos=(70,600),size=(300,200))
            rand2=randint(0,8)
            rand3=randint(0,8)
            self.name_color=Label(pos=(0,200), text=convert_to_persian(colors_names[rand2]), font_size=50, color=colors[rand3])
            if rand==rand3:continue
            else:break
        self.state_color=convert_to_persian("بله") if rand==rand2 else convert_to_persian("نه")
        self.btn1_color=Button(text=convert_to_persian("بله"),pos=(70,500),font_size=50,color=(0,0,0,1),size_hint=(None,None),size=(100,100))
        self.btn1_color.bind(on_press=self.choice_color)
        self.layout.add_widget(self.btn1_color)
        self.btn2_color=Button(text=convert_to_persian("نه"),pos=(270,500),font_size=50,color=(0,0,0,1),size_hint=(None,None),size=(100,100))
        self.btn2_color.bind(on_press=self.choice_color)
        self.layout.add_widget(self.btn2_color)
        self.timer_color=Label(pos=(-180,370),text='3',font_size=30)
        self.layout.add_widget(self.timer_color)
        self.timer_loop_color=Clock.schedule_interval(self.update_color, 1)
        self.correct_incorrect=Label(pos=(0,-100),text='',font_size=40)
        self.layout.add_widget(self.correct_incorrect)
        self.layout.add_widget(self.name_color)
    def update_color(self, dt):
        if self.timer_color.text=='1':
            Clock.unschedule(self.timer_loop_color)
            self.incorrect_color+=1
            self.questions_count_color-=1
            if self.questions_count_color==0:
                self.layout.clear_widgets()
                self.layout.size=(360,1000)
                self.layout.add_widget(BlueScreen())
                self.layout.add_widget(Label(text=convert_to_persian('مرحله به پایان رسید'),pos=(0,300),font_size=38,color=(0,0,0,1)))
                self.layout.add_widget(Label(text=str(self.correct_color)+convert_to_persian('پاسخ های درست:'),pos=(0,100),font_size=25))
                self.layout.add_widget(Label(text=str(self.incorrect_color)+convert_to_persian('پاسخ های نادرست:'),pos=(0,50),font_size=25))
                self.layout.add_widget(Label(text=str(self.correct_color*3)+convert_to_persian('مقدار سکه:'),pos=(0,0),font_size=25))
                self.layout.add_widget(Label(text=str(self.correct_color*5)+convert_to_persian('مقدار امتیاز:'),pos=(0,-50),font_size=25))
                self.layout.add_widget(Button(text=convert_to_persian('خروج'),pos=(125,350),size_hint=(None,None),size=(200,50),font_size=25,on_press=self.Tab2_drawer))
                data_edit(get_user(),'Coin',int(data_get(get_user(),'Coin'))+self.correct_color*3)
                data_edit(get_user(),'XP',int(data_get(get_user(),'XP'))+self.correct_color*5)
                self.correct_color=0
                self.incorrect_color=0
                self.questions_count_color=10
            else:
                self.btn1_color.unbind(on_press=self.choice_color)
                self.btn2_color.unbind(on_press=self.choice_color)
                Clock.unschedule(self.timer_loop_color)
                Clock.schedule_once(self.color_level,1)
        elif self.timer_color.text!='1':
            self.timer_color.text= str(int(self.timer_color.text)-1)    
    def choice_color(self,instance):
        if self.state_color==instance.text:
            self.correct_incorrect.text=convert_to_persian('درست')
            instance.background_color=(0,1,0,1)
            self.correct_sound.play()
            self.btn1_color.unbind(on_press=self.choice_color)
            self.btn2_color.unbind(on_press=self.choice_color)
            Clock.unschedule(self.timer_loop_color)
            self.correct_color+=1
            self.questions_count_color-=1
        else:
            self.correct_incorrect.text=convert_to_persian('نادرست')
            instance.background_color=(1,0,0,1)
            self.wrong_sound.play()
            self.btn1_color.unbind(on_press=self.choice_color)
            self.btn2_color.unbind(on_press=self.choice_color)
            Clock.unschedule(self.timer_loop_color)
            self.incorrect_color+=1
            self.questions_count_color-=1
        if self.questions_count_color==0:
            self.layout.clear_widgets()
            self.layout.size=(360,1000)
            self.layout.add_widget(BlueScreen())
            self.layout.add_widget(Label(text=convert_to_persian('مرحله به پایان رسید'),pos=(0,300),font_size=38,color=(0,0,0,1)))
            self.layout.add_widget(Label(text=str(self.correct_color)+convert_to_persian('پاسخ های درست:'),pos=(0,100),font_size=25))
            self.layout.add_widget(Label(text=str(self.incorrect_color)+convert_to_persian('پاسخ های نادرست:'),pos=(0,50),font_size=25))
            self.layout.add_widget(Label(text=str(self.correct_color*3)+convert_to_persian('مقدار سکه:'),pos=(0,0),font_size=25))
            self.layout.add_widget(Label(text=str(self.correct_color*5)+convert_to_persian('مقدار امتیاز:'),pos=(0,-50),font_size=25))
            self.layout.add_widget(Button(text=convert_to_persian('خروج'),pos=(125,350),size_hint=(None,None),size=(200,50),font_size=25,on_press=self.Tab2_drawer))
            data_edit(get_user(),'Coin',int(data_get(get_user(),'Coin'))+self.correct_color*3)
            data_edit(get_user(),'XP',int(data_get(get_user(),'XP'))+self.correct_color*5)
            self.correct_color=0
            self.incorrect_color=0
            self.questions_count_color=10
            Clock.unschedule(self.timer_loop_color)
        else:
            Clock.unschedule(self.timer_loop_color)
            Clock.schedule_once(self.color_level,1)
    def update_timer(self,dt,command): 
        if self.timer.text=='1':
            Clock.unschedule(self.timer_loop)
            self.incorrect+=1
            self.btn1.unbind(on_press=self.instancebtn)
            self.btn2.unbind(on_press=self.instancebtn)
            self.btn3.unbind(on_press=self.instancebtn)
            self.questions_count-=1
            if self.questions_count==0:
                self.layout.clear_widgets()
                self.layout.size=(360,1000)
                self.layout.add_widget(BlueScreen())
                self.layout.add_widget(Label(text=convert_to_persian('مرحله به پایان رسید'),pos=(0,300),font_size=38,color=(0,0,0,1)))
                self.layout.add_widget(Label(text=str(self.correct)+convert_to_persian('پاسخ های درست:'),pos=(0,100),font_size=25))
                self.layout.add_widget(Label(text=str(self.incorrect)+convert_to_persian('پاسخ های نادرست:'),pos=(0,50),font_size=25))
                self.layout.add_widget(Label(text=str(self.correct*3)+convert_to_persian('مقدار سکه:'),pos=(0,0),font_size=25))
                self.layout.add_widget(Label(text=str(self.correct*5)+convert_to_persian('مقدار امتیاز:'),pos=(0,-50),font_size=25))
                self.layout.add_widget(Button(text=convert_to_persian('خروج'),pos=(125,350),size_hint=(None,None),size=(200,50),font_size=25,on_press=self.jadval_zarb))
                data_edit(get_user(),'Coin',int(data_get(get_user(),'Coin'))+self.correct*3)
                data_edit(get_user(),'XP',int(data_get(get_user(),'XP'))+self.correct*5)
                if data_get(get_user(),'Level_jadval_zarb')<10:
                    data_edit(get_user(),'Level_jadval_zarb',int(data_get(get_user(),'Level_jadval_zarb'))+1)
                self.correct=0
                self.incorrect=0
                self.questions_count=10
                Clock.unschedule(self.timer_loop)
            else:Clock.schedule_once(command,1)
        elif self.timer.text!='1':
            self.timer.text= str(int(self.timer.text)-1)
    def choice(self,instance,command):
        if instance.text==str(self.ans):
            self.correct_incorrect.text=convert_to_persian('درست')
            instance.background_color=(0,1,0,1)
            self.correct_sound.play()
            self.btn1.unbind(on_press=self.instancebtn)
            self.btn2.unbind(on_press=self.instancebtn)
            self.btn3.unbind(on_press=self.instancebtn)
            Clock.unschedule(self.timer_loop)
            self.correct+=1
            self.questions_count-=1
        else:
            self.correct_incorrect.text=convert_to_persian('نادرست')
            instance.background_color=(1,0,0,1)
            self.wrong_sound.play()
            self.btn1.unbind(on_press=self.instancebtn)
            self.btn2.unbind(on_press=self.instancebtn)
            self.btn3.unbind(on_press=self.instancebtn)  
            Clock.unschedule(self.timer_loop)
            self.incorrect+=1
            self.questions_count-=1
        if self.questions_count==0:
            self.layout.clear_widgets()
            self.layout.size=(360,1000)
            self.layout.add_widget(BlueScreen())
            self.layout.add_widget(Label(text=convert_to_persian('مرحله به پایان رسید'),pos=(0,300),font_size=38,color=(0,0,0,1)))
            self.layout.add_widget(Label(text=str(self.correct)+convert_to_persian('پاسخ های درست:'),pos=(0,100),font_size=25))
            self.layout.add_widget(Label(text=str(self.incorrect)+convert_to_persian('پاسخ های نادرست:'),pos=(0,50),font_size=25))
            self.layout.add_widget(Label(text=str(self.correct*3)+convert_to_persian('مقدار سکه:'),pos=(0,0),font_size=25))
            self.layout.add_widget(Label(text=str(self.correct*5)+convert_to_persian('مقدار امتیاز:'),pos=(0,-50),font_size=25))
            self.layout.add_widget(Button(text=convert_to_persian('خروج'),pos=(125,350),size_hint=(None,None),size=(200,50),font_size=25,on_press=self.jadval_zarb))
            data_edit(get_user(),'Coin',int(data_get(get_user(),'Coin'))+self.correct*3)
            data_edit(get_user(),'XP',int(data_get(get_user(),'XP'))+self.correct*5)
            if data_get(get_user(),'Level_jadval_zarb')<10:
                data_edit(get_user(),'Level_jadval_zarb',int(data_get(get_user(),'Level_jadval_zarb'))+1)
            self.correct=0
            self.incorrect=0
            self.questions_count=10
            Clock.unschedule(self.timer_loop)
        else:Clock.schedule_once(command,1)
if __name__ == '__main__':
    MainApp().run()
