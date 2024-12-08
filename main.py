import pandas as pd
import random
import tkinter as tk
from tkinter import messagebox

# 读取Excel表格数据
def load_data(file_path):
    try:
        data = pd.read_excel(file_path)
        return data.to_dict(orient="records")
    except Exception as e:
        messagebox.showerror("错误", f"无法加载数据：{e}")
        return []

# 随机生成题目
def generate_question(verbs):
    question = random.choice(verbs)
    verb_forms = ["V-ます形", "原形", "て/た", "意志", "命令", "假定", "可能", "被动", "未然", "使役"]
    target_form = random.choice(verb_forms)  # 随机选取一种变形形式
    correct_form = question[target_form]
    options = [correct_form]
    while len(options) < 4:
        option = random.choice(verbs)[target_form]
        if option not in options:
            options.append(option)
    random.shuffle(options)
    return question['原形'], target_form, correct_form, options

# 检查答案
def check_answer(selected, correct):
    if selected == correct:
        messagebox.showinfo("答题结果", "正确！")
    else:
        messagebox.showinfo("答题结果", f"错误！正确答案是：{correct}")
    new_question()

# 更新题目
def new_question():
    global correct_answer
    if verbs:
        verb, target_form, correct_answer, options = generate_question(verbs)
        label_question.config(text=f"请将『{verb}』变为『{target_form}』：")
        for i, option in enumerate(options):
            buttons[i].config(text=option, command=lambda opt=option: check_answer(opt, correct_answer))
    else:
        label_question.config(text="没有可用的题目，请检查数据文件！")

# 主程序
file_path = "verbs.xlsx"
verbs = load_data(file_path)

# 创建界面
root = tk.Tk()
root.title("日语动词变形练习")

label_question = tk.Label(root, text="", font=("Arial", 14))
label_question.pack(pady=20)

buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 12), width=20)
    btn.pack(pady=5)
    buttons.append(btn)

new_question()

root.mainloop()
