from tkinter import *
from tkinter import messagebox


def create_window():
    app = Tk()
    app.title('Калькулятор ИМТ')
    app.geometry('400x300')

    main_frame = Frame(app, padx=10, pady=10)
    main_frame.pack(expand=True)

    height_label = Label(main_frame, text="Введите рост (см):")
    height_label.grid(row=0, column=0)

    weight_label = Label(main_frame, text="Введите вес (кг):")
    weight_label.grid(row=1, column=0)

    height_entry = Entry(main_frame)
    height_entry.grid(row=0, column=1, pady=5)

    weight_entry = Entry(main_frame)
    weight_entry.grid(row=1, column=1, pady=5)

    calculate_button = Button(main_frame, text='Рассчитать ИМТ',
                              command=lambda: calculate_bmi(height_entry.get(), weight_entry.get()))
    calculate_button.grid(row=2, column=1)

    app.mainloop()


def calculate_bmi(height_str, weight_str):
    try:
        weight_kg = int(weight_str)
        height_m = int(height_str) / 100
        bmi_value = weight_kg / (height_m ** 2)
        bmi_value = round(bmi_value, 1)

        if bmi_value < 18.5:
            messagebox.showinfo('Результат', f'ИМТ = {bmi_value} соответствует недостаточному весу.')
        elif 18.5 <= bmi_value < 24.9:
            messagebox.showinfo('Результат', f'ИМТ = {bmi_value} соответствует нормальному весу.')
        elif 24.9 <= bmi_value < 29.9:
            messagebox.showinfo('Результат', f'ИМТ = {bmi_value} соответствует избыточному весу.')
        else:
            messagebox.showinfo('Результат', f'ИМТ = {bmi_value} соответствует ожирению.')
    except ValueError:
        messagebox.showerror('Ошибка', 'Пожалуйста, введите корректные данные.')


# Запуск приложения
create_window()





