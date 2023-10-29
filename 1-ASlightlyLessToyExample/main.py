import toga 
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack




def build(app):
    box_c = toga.Box()
    box_f = toga.Box()
    box = toga.Box()
    
    input_c = toga.TextInput(readonly=True)
    input_f = toga.TextInput()
    input_c.placeholder = 'celsious'
    input_f.placeholder='fahrenheit'
    
    lb_c = toga.Label('celsious', style=Pack(text_align=LEFT))
    lb_f = toga.Label('fahrenheit', style=Pack(text_align=LEFT))
    lb_join = toga.Label('é equivalente a', style=Pack(text_align=RIGHT))

    

    def calculate(widget):
        try:
            input_c.value = (float(input_f.value) - 32.0) * 5.0 / 9.0

        except ValueError:
            input_c.value = '???'

        
        
    bt = toga.Button('calcular', on_press=calculate)

    box_f.add(input_f)
    box_f.add(lb_f)

    box_c.add(lb_join)
    box_c.add(input_c)
    box_c.add(lb_c)

    box.add(box_f)
    box.add(box_c)
    box.add(bt)


    box.style.update(direction=COLUMN, padding=10)
    box_f.style.update(direction=ROW, padding=5)
    box_c.style.update(direction=ROW, padding=5)

    input_c.style.update(flex=1)
    input_f.style.update(flex=1, padding_left=210)
    lb_c.style.update(width=100, padding_left=10)
    lb_f.style.update(width=100, padding_left=10)
    lb_join.style.update(width=200, padding_left=10)

    bt.style.update(padding=15)

    return box

def main():
    return toga.App('conversor de temperatura', 'org.beware', startup=build)

    
if __name__ == '__main__':
    main().main_loop()