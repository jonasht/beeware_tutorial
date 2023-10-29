"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import httpx

def greeting(name):
    if name:
        if name == "Brutus":
            return "BeeWare the IDEs of Python!"
        else:
            return f"Hello, {name}"
    else:
        return "Hello, stranger"
class HelloWorld(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        lb_name = toga.Label('seu nome:',
                             style=Pack(padding=(0, 5)),
                             )
        self.input_name = toga.TextInput(style=Pack(flex=1))

        box_name = toga.Box(style=Pack(direction=ROW, padding=5))
        box_name.add(lb_name)
        box_name.add(self.input_name)

        bt = toga.Button(
            'diz oi',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )
        
        bt2 = toga.Button(
            'diz oi 2', 
            on_press=self.say_hello2,
            style=Pack(padding=5)
        )
        
        main_box.add(box_name)
        main_box.add(bt)
        main_box.add(bt2)


        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()



    def say_hello(self, widget):
        # print(f'oi/hello, {self.input_name.value}')
        self.main_window.info_dialog(
            greeting(self.input_name.value),
            'hi there'
        )
        
    async def say_hello2(self, widget):
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/posts/42")

        payload = response.json()

        self.main_window.info_dialog(
            greeting(self.input_name.value),
            payload["body"],
    )
        

def main():
    return HelloWorld()
