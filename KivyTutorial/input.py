import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #Initialize Infinite keywords
    def __init__(self, **kwargs):
        #Call grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)

        #Set Columns
        self.cols = 2

        #Add widgets
        self.add_widget(Label(text = "Name: "))
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)

        self.add_widget(Label(text = "Favorite Pizza: "))
        self.pizza = TextInput(multiline = False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text = "Favorite Color: "))
        self.color = TextInput(multiline = False)
        self.add_widget(self.color)

        #Create a submit button
        self.submit = Button(text = "Submit", font_size = 32)
        #bind the button
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        self.add_widget(Label(text = f"hello {name}, you like {pizza} and your favoite color is {color}"))

        #Clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()
