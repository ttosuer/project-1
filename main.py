#!/usr/bin/env python
# coding: utf-8

# In[2]:


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import pyttsx3
from threading import Thread


def align_text(instance, value):
    instance.text_size = (instance.width * 0.9, None)
    instance.padding_x = (instance.width - instance.texture_size[0]) / 2
    instance.padding_y = (instance.height - instance.texture_size[1]) / 2

class TimerStopwatchApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine = pyttsx3.init()

    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.timer_status = Label(text='', font_size='40sp')
        layout.add_widget(self.timer_status)

        self.label = Label(text='00:00:00', font_size='40sp')
        layout.add_widget(self.label)

        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)

        timer_layout = BoxLayout(orientation='horizontal')
        self.input_hour = TextInput(text='', multiline=False, size_hint_x=0.15, halign='center')
        self.input_hour.bind(on_text=align_text)
        timer_layout.add_widget(self.input_hour)
        timer_layout.add_widget(Label(text='h', size_hint_x=0.05, font_size='20sp'))
        self.input_minute = TextInput(text='', multiline=False, size_hint_x=0.15, halign='center')
        self.input_minute.bind(on_text=align_text)
        timer_layout.add_widget(self.input_minute)
        timer_layout.add_widget(Label(text='m', size_hint_x=0.05, font_size='20sp'))
        self.input_second = TextInput(text='', multiline=False, size_hint_x=0.15, halign='center')
        self.input_second.bind(on_text=align_text)
        timer_layout.add_widget(self.input_second)
        timer_layout.add_widget(Label(text='s', size_hint_x=0.05, font_size='20sp'))
        self.start_timer_button = Button(text='Start Timer', on_press=self.start_timer, size_hint_x=0.25)
        timer_layout.add_widget(self.start_timer_button)

        self.stop_button = Button(text='Stop', on_press=self.stop, disabled=True, size_hint_x=0.25)
        self.reset_button = Button(text='Reset', on_press=self.reset, disabled=True, size_hint_x=0.25)

        button_layout.add_widget(timer_layout)
        button_layout.add_widget(self.stop_button)
        button_layout.add_widget(self.reset_button)
        layout.add_widget(button_layout)

        # 추가된 부분: 시간, 분, 초 입력받는 칸
        time_input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        self.input_hour_2 = TextInput(text='', multiline=False, size_hint_x=0.15, halign='center')
        self.input_hour_2.bind(on_text=align_text)
        time_input_layout.add_widget(self.input_hour_2)
        time_input_layout.add_widget(Label(text='h', size_hint_x=0.05, font_size='20sp'))
        self.input_minute_2 = TextInput(text='', multiline=False, size_hint_x=0.15, halign='center')
        self.input_minute_2.bind(on_text=align_text)
        time_input_layout.add_widget(self.input_minute_2)
        time_input_layout.add_widget(Label(text='m', size_hint_x=0.05, font_size='20sp'))
        self.input_second_2 = TextInput(text='', multiline=False, size_hint_x=0.15, halign='center')
        self.input_second_2.bind(on_text=align_text)
        time_input_layout.add_widget(self.input_second_2)
        time_input_layout.add_widget(Label(text='s', size_hint_x=0.05, font_size='20sp'))
        layout.add_widget(time_input_layout)
        
        
        time_input_layout3 = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        self.input_hour_3 = TextInput(text='', multiline=False, size_hint_x=0.15, halign='center')
        self.input_hour_3.bind(on_text=align_text)
        time_input_layout3.add_widget(self.input_hour_3) # 수정된 부분
        time_input_layout3.add_widget(Label(text='h', size_hint_x=0.05, font_size='20sp'))
        self.input_minute_3 = TextInput(text='', multiline=False, size_hint_x=0.15, halign='center')
        self.input_minute_3.bind(on_text=align_text)
        time_input_layout3.add_widget(self.input_minute_3) # 수정된 부분
        time_input_layout3.add_widget(Label(text='m', size_hint_x=0.05, font_size='20sp'))
        self.input_second_3 = TextInput(text='', multiline=False, size_hint_x=0.15, halign='center')
        self.input_second_3.bind(on_text=align_text)
        time_input_layout3.add_widget(self.input_second_3) # 수정된 부분
        time_input_layout3.add_widget(Label(text='s', size_hint_x=0.05, font_size='20sp'))
        layout.add_widget(time_input_layout3)
        
        
        time_input_layout4 = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        self.input_hour_4 = TextInput(text='', multiline=False, size_hint_x=0.15, halign='center')
        self.input_hour_4.bind(on_text=align_text)
        time_input_layout4.add_widget(self.input_hour_4) 
        time_input_layout4.add_widget(Label(text='h', size_hint_x=0.05, font_size='20sp'))
        self.input_minute_4 = TextInput(text='', multiline=False, size_hint_x=0.15, halign='center')
        self.input_minute_4.bind(on_text=align_text)
        time_input_layout4.add_widget(self.input_minute_4)
        time_input_layout4.add_widget(Label(text='m', size_hint_x=0.05, font_size='20sp'))
        self.input_second_4 = TextInput(text='', multiline=False, size_hint_x=0.15, halign='center')
        self.input_second_4.bind(on_text=align_text)
        time_input_layout4.add_widget(self.input_second_4)
        time_input_layout4.add_widget(Label(text='s', size_hint_x=0.05, font_size='20sp'))
        layout.add_widget(time_input_layout4)



        self.seconds = 0
        self.timer_seconds = 0
        return layout

    def start_timer(self, instance):
        hours = int(self.input_hour.text) if self.input_hour.text else 0
        minutes = int(self.input_minute.text) if self.input_minute.text else 0
        seconds = int(self.input_second.text) if self.input_second.text else 0
        self.timer_seconds = hours * 3600 + minutes * 60 + seconds
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)
        self.stopwatch_event = Clock.schedule_interval(self.update_stopwatch, 1)
        self.timer_status.text = ''
        self.stop_button.disabled = False
        self.reset_button.disabled = False

    def stop(self, instance):
        self.timer_event.cancel()
        self.stopwatch_event.cancel()
        self.stop_button.disabled = True

    def reset(self, instance):
        self.seconds = 0
        self.label.text = '00:00:00'
        self.timer_status.text = ''
        self.stop_button.disabled = True

    def update_stopwatch(self, instance):
        self.seconds += 1
        self.label.text = "{hours:02d}:{minutes:02d}:{seconds:02d}".format(hours=self.seconds // 3600, minutes=(self.seconds // 60) % 60, seconds=self.seconds % 60)

    def update_timer(self, instance):
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.timer_status.text = "{hours:02d}:{minutes:02d}:{seconds:02d}".format(hours=self.timer_seconds // 3600, minutes=(self.timer_seconds // 60) % 60, seconds=self.timer_seconds % 60)
            hours = self.timer_seconds // 3600
            minutes = (self.timer_seconds // 60) % 60
            seconds = self.timer_seconds % 60

            alert_hours = int(self.input_hour_2.text) if self.input_hour_2.text else 0
            alert_minutes = int(self.input_minute_2.text) if self.input_minute_2.text else 0
            alert_seconds = int(self.input_second_2.text) if self.input_second_2.text else 0
            alert_time = alert_hours * 3600 + alert_minutes * 60 + alert_seconds
            
            alert_hours3 = int(self.input_hour_3.text) if self.input_hour_3.text else 0
            alert_minutes3 = int(self.input_minute_3.text) if self.input_minute_3.text else 0
            alert_seconds3 = int(self.input_second_3.text) if self.input_second_3.text else 0
            alert_time3 = alert_hours3 * 3600 + alert_minutes3 * 60 + alert_seconds3
            
            alert_hours4 = int(self.input_hour_4.text) if self.input_hour_4.text else 0
            alert_minutes4 = int(self.input_minute_4.text) if self.input_minute_4.text else 0
            alert_seconds4 = int(self.input_second_4.text) if self.input_second_4.text else 0
            alert_time4 = alert_hours4 * 3600 + alert_minutes4 * 60 + alert_seconds4

            if self.timer_seconds == alert_time or self.timer_seconds == alert_time3 or self.timer_seconds == alert_time4:
                self.speak_time(hours, minutes, seconds)

        else:
            self.timer_event.cancel()
            self.stopwatch_event.cancel()
            self.timer_status.text = 'Time is up!'
            self.stop_button.disabled = True
            Thread(target=self._speak, args=("시험이 종료되었습니다.",)).start()


    def speak_time(self, hours, minutes, seconds):
        if hours is None or hours == 0:
            if minutes is None or minutes == 0:
                time_text = "{seconds}초 남았습니다.".format(seconds=seconds)
            else:
                time_text = "{minutes}분 {seconds}초 남았습니다.".format(minutes=minutes, seconds=seconds)
        else:
            if minutes is None or minutes == 0:
                if seconds is None or seconds == 0:
                    time_text = "{hours}시간 남았습니다.".format(hours=hours)
                else:
                    time_text = "{hours}시간 {seconds}초 남았습니다.".format(hours=hours, seconds=seconds)
            else:
                if seconds is None or seconds == 0:
                    time_text = "{hours}시간 {minutes}분 남았습니다.".format(hours=hours, minutes=minutes)
                else:
                    time_text = "{hours}시간 {minutes}분 {seconds}초 남았습니다.".format(hours=hours, minutes=minutes, seconds=seconds)
        Thread(target=self._speak, args=(time_text,)).start()


    def _speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    TimerStopwatchApp().run()


# In[ ]:




