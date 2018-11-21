#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ivar at 05.11.2018


# main

from class_Worker import *
from func import *
import pickle


if __name__ == '__main__':

    def set_work(workers):
        for worker in workers:
            worker.set_otr()
            worker.set_zak()
            worker.set_sve()
            worker.set_otr_s()
            worker.set_zak_s()
            worker.set_ktu()
            worker.set_coef_f()
            worker.set_prir()
        prir_dol(workers)
        var_ent_coef.set(get_brig_coef_f(workers))


    # f = open("data.pkl", "rb")
    # workers = pickle.load(f)
    # f.close()

    root = Tk()
    root.title("КТУ")
    win = Frame(root, bg="#A9A9A9")
    win.pack(side=TOP)

    workers = []
    names = ["Denis", "Ivan", "Sasha", "Valery", "Amir", "Slava", "Yuri", "Fidel", "Gennady"]

    Label(win, text='имя', width=7, bg="#000080", fg="#FFFFFF", font=("Consolas", 14, "bold")).pack(side=LEFT)
    Label(win, text='отр', width=6, bg="#000080", fg="#FFFFFF", font=("Consolas", 14, "bold")).pack(side=LEFT)
    Label(win, text='закр', width=6, bg="#000080", fg="#FFFFFF", font=("Consolas", 14, "bold")).pack(side=LEFT)
    Label(win, text='свер', width=5, bg="#000080", fg="#FFFFFF", font=("Consolas", 14, "bold")).pack(side=LEFT)
    Label(win, text='отр.с', width=5, bg="#000080", fg="#FFFFFF", font=("Consolas", 14, "bold")).pack(side=LEFT)
    Label(win, text='зак.с', width=5, bg="#000080", fg="#FFFFFF", font=("Consolas", 14, "bold")).pack(side=LEFT)
    Label(win, text='кту', width=4, bg="#000080", fg="#FFFFFF", font=("Consolas", 14, "bold")).pack(side=LEFT)
    Label(win, text='коэф', width=4, bg="#000080", fg="#FFFFFF", font=("Consolas", 14, "bold")).pack(side=LEFT)
    #Label(win, text='прир', width=6, bg="#000080", fg="#FFFFFF", font=("Consolas", 14, "bold")).pack(side=LEFT)
    #Label(win, text='р.пр', width=6, bg="#000080", fg="#FFFFFF", font=("Consolas", 14, "bold")).pack(side=LEFT)
    Label(win, text='часы', width=6, bg="black", fg="#FFA500", font=("Consolas", 14, "bold")).pack(side=LEFT)

    win2 = Frame(root, bg="#A9A9A9")
    win2.pack()

    for name in names:
        worker = Worker(name, win2)
        workers.append(worker)

    win3 = Frame(root, bg="#000080")
    win3.pack(fill=X)
    Label(win3, text="коэффициент переработки по бригаде: ", bg="#000080", fg="#C0C0C0", font=("Consolas", 14)).pack(side=LEFT)
    var_ent_coef = StringVar()
    brig_coef = Entry(win3, width=4, textvariable=var_ent_coef, bg="#FF8C00", font=("Consolas", 14, "bold"), bd=2)
    brig_coef.pack(side=LEFT)


    Button(win3, text="старт", command=lambda:set_work(workers), font=("Consolas", 14, "bold"), bg="black", fg="#FFA500", bd=2, width=6).pack(side=RIGHT)


    root.mainloop()