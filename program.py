import tkinter as tk

# валидаторы прописать
def validate_int(input_string, arg):
    return True

# очистка форм
def clear():                            
    arg1.delete(0, tk.END)
    arg2.delete(0, tk.END)
    plus.config(state="disabled")

# переключатель отображения при смене режима
def update_buttons():
    arg1.delete(0, tk.END)
    arg2.delete(0, tk.END)

    if str(mode.get()) == "Калькулятор":
        square_frame.grid_forget()
        calc_frame.grid(row=4, column=0)
    else:
        calc_frame.grid_forget()
        square_frame.grid(row=4)

# свапаем переменные           
def swap_args():
    temp = str(arg1.get())
    
    arg1.delete(0, tk.END)
    arg1.insert(0, arg2.get())

    arg2.delete(0, tk.END)
    arg2.insert(0, temp)

def operation(mode, op):
    if mode == "calc":
        match op:
            case "+":
                tk.Label(calc_frame, text = str(int(arg1.get()) + int(arg2.get()))).grid(row=0, column=1, sticky="we")
            case "-":
                tk.Label(calc_frame, text = str(int(arg1.get()) - int(arg2.get()))).grid(row=1, column=1, sticky="we")
            case "*":
                tk.Label(calc_frame, text = str(int(arg1.get()) * int(arg2.get()))).grid(row=2, column=1, sticky="we")
            case "/":
                if arg2.get():
                    res = str(int(arg1.get()) / int(arg2.get()))
                else:
                    res = "На ноль делить нельзя"
                tk.Label(calc_frame, text = res).grid(row=3, column=1, sticky="we")
    else:
        match op:
            case "perimeter":
                tk.Label(app, text = str((int(arg1.get()) + int(arg2.get())) * 2)).grid(row=4, column=1, rowspan=2, sticky="w")
            case "square":
                tk.Label(app, text = str(int(arg1.get()) * int(arg2.get()))).grid(row=6, column=1, rowspan=2, sticky="w")


        
app = tk.Tk()
app.title("Калькулятор")
app.geometry("267x250")
app.minsize(267,250)
app.maxsize(350,350)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# главная надпись
main_label = tk.Label(app, text = "Введите числа").grid(row=0, column=0, columnspan=2, sticky="we")

# переменные
arg1_var = tk.StringVar(value="")
arg1 = tk.Entry(app, width=10, textvariable=arg1_var, validate="key", validatecommand=(app.register(lambda input_string: validate_int(input_string, arg1)), "%S"))
arg1.grid(row=1, column=0)
arg2_var = tk.StringVar(value="")
arg2 = tk.Entry(app, width=10, textvariable=arg2_var, validate="key", validatecommand=(app.register(lambda input_string: validate_int(input_string, arg2)), "%S"))
arg2.grid(row=1, column=1)



# кнопка для свопа
swap_btn = tk.Button(app, text = "Поменять местами", command=swap_args).grid(row=2, columnspan=2, pady=3)

# режимы работы
mode = tk.StringVar(value="Калькулятор")

# режим калькулятора
calc_frame = tk.Frame(app)

plus = tk.Checkbutton(calc_frame, text="Cложение", command=lambda: operation("calc", "+")).grid(row=0, column=0, sticky="w")
minus = tk.Checkbutton(calc_frame, text="Вычитание", command=lambda: operation("calc", "-")).grid(row=1, column=0, sticky="w")
mul = tk.Checkbutton(calc_frame, text="Умножение", command=lambda: operation("calc", "*")).grid(row=2, column=0, sticky="w")
div = tk.Checkbutton(calc_frame, text="Деление", command=lambda: operation("calc", "/")).grid(row=3, column=0, sticky="w")


calc_frame.grid(row=4, columnspan=2, sticky="wn", padx=15)          # отображение при запуске
calc_frame.grid_columnconfigure(0, weight=2)

# режим прямоугольника
square_frame = tk.Frame(app)
square_calc_frame = tk.Frame(app)

perimetr = tk.Checkbutton(square_frame, text="Периметр").grid(row=0, rowspan=2, sticky="w")
square = tk.Checkbutton(square_frame, text="Площадь").grid(row=2, rowspan=2, sticky="w")

app.grid_rowconfigure(7, weight=1)

square_calc_frame.grid_forget()
square_frame.grid_forget()      # скрыть при запуске


# селектор переключения
calc = tk.Radiobutton(app, text="Калькулятор", value="Калькулятор", variable=mode, command=update_buttons).grid(row=3, column=0)
square = tk.Radiobutton(app, text="Прямоугольник", value="Прямоугольник", variable=mode, command=update_buttons).grid(row=3, column=1)




# действия



clear_btn = tk.Button(app, text = "Очистить форму", command=clear, width=10).grid(row=8, column=0, pady=7)


quit_btn = tk.Button(app, text = "Выйти", command=lambda: app.destroy()).grid(row=8, column=1, pady=7)



# иконка
#photo = tk.PhotoImage(file="path") 
#app.iconphoto(False, photo)



app.mainloop()