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
        self.cols = 1

        #Create second grid layout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        #Add widgets
        self.top_grid.add_widget(Label(text = "Name: "))
        self.name = TextInput(multiline = False)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text = "Favorite Pizza: "))
        self.pizza = TextInput(multiline = False)
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text = "Favorite Color: "))
        self.color = TextInput(multiline = False)
        self.top_grid.add_widget(self.color)

        #adding top grid widget
        self.add_widget(self.top_grid)

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
