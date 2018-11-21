#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ivar at 04.11.2018

# Class Worker

from tkinter import *


class Worker:
    """данные о рабочем"""
    # инициализация, не требует обязательных аргументов
    def __init__(self, name="Unknown worker", parent=None):
        self.frame = Frame(parent)  # рамка
        self.frame.pack()

        self.name = str(name)   # имя
        self.lbl_name = Label(self.frame, text=self.name, width=7, bg="#000080", fg='#C0C0C0', font=("Consolas", 14, "bold"))
        self.lbl_name.pack(side=LEFT)

        self.otr = 0    # отработанные часы
        self.var_otr = StringVar()
        self.ent_otr = Entry(self.frame, textvariable=self.var_otr, width=6, bg="#FFA500", bd=2, font=("Consolas", 14, "bold"))
        self.ent_otr.pack(side=LEFT)

        self.zak = 0    # закрытые часы
        self.var_zak = StringVar()
        self.ent_zak = Entry(self.frame, textvariable=self.var_zak, width=6, bg="#FFA500", bd=2, font=("Consolas", 14, "bold"))
        self.ent_zak.pack(side=LEFT)

        self.sve = 0    # сверхурочные
        self.var_sve = StringVar()
        self.ent_sve = Entry(self.frame, textvariable=self.var_sve, width=5, bg="#FFA500", bd=2, font=("Consolas", 14, "bold"))
        self.ent_sve.pack(side=LEFT)

        self.otr_s = 0  # отработанные субботы (часы)
        self.var_otr_s = StringVar()
        self.ent_otr_s = Entry(self.frame, textvariable=self.var_otr_s, width=5, bg="#FFA500", bd=2, font=("Consolas", 14, "bold"))
        self.ent_otr_s.pack(side=LEFT)

        self.zak_s = 0  # закрытые часы за субботы
        self.var_zak_s = StringVar()
        self.ent_zak_s = Entry(self.frame, textvariable=self.var_zak_s, width=5, bg="#FFA500", bd=2, font=("Consolas", 14, "bold"))
        self.ent_zak_s.pack(side=LEFT)

        self.ktu = 0    # кту
        self.var_ktu = StringVar()
        self.ent_ktu = Entry(self.frame, textvariable=self.var_ktu, width=4, bg="#FFA500", bd=2, font=("Consolas", 14, "bold"))
        self.ent_ktu.pack(side=LEFT)

        self.coef = 0   # коэффициент переработки без суббот
        self.var_coef = StringVar()

        self.coef_s = 0 # коэф за субботы
        self.var_coef_s = StringVar()

        self.coef_f = 0 # общий коэф
        self.var_coef_f = StringVar()
        self.ent_coef_f = Entry(self.frame, textvariable=self.var_coef_f, width=4, bg="#FF8C00", bd=2, font=("Consolas", 14, "bold"))
        self.ent_coef_f.pack(side=LEFT)

        self.prir_d = 0 # приработок по кту(должен быть)
        self.var_prir_d = StringVar()
        self.ent_prir_d = Entry(self.frame, textvariable=self.var_prir_d, width=6, bg="#FFA500", bd=2, font=("Consolas", 14, "bold"))
        #self.ent_prir_d.pack(side=LEFT)

        self.prir = 0   # реальный приработок
        self.var_prir = StringVar()
        self.ent_prir = Entry(self.frame, textvariable=self.var_prir, width=6, bg="#FFA500", bd=2, font=("Consolas", 14, "bold"))
        #self.ent_prir.pack(side=LEFT)

        self.prir_r = 0  # разница приработок
        self.var_prir_r = StringVar()
        self.ent_prir_r = Entry(self.frame, textvariable=self.var_prir_r, width=6, bg="#FF8C00", bd=2, font=("Consolas", 14, "bold"))
        self.ent_prir_r.pack(side=LEFT)


        self.ktu_r = 0  # реальный кту
        self.var_ktu_r = StringVar()

        self.otr_o = 0  # общие отраб часы
        self.var_otr_o = StringVar()



    # функции для внесения параметров===========================================

    # проверка внесенных данных
    @staticmethod
    def err(num):
        try:
            if type(num) == str:
                num = num.replace(",", ".")
            if num != '0':
                num = float(num)
                num = round(num, 2)
            else:
                num = 0
        except ValueError:
            num = 0

        return num

    # отработанные
    def set_otr(self):
        otr = self.var_otr.get()
        self.otr = Worker.err(otr)
        self.var_otr.set(self.otr)

    # закрытые
    def set_zak(self):
        zak = self.var_zak.get()
        self.zak = Worker.err(zak)
        self.var_zak.set(self.zak)

    # сверхурочные
    def set_sve(self):
        sve = self.var_sve.get()
        self.sve = Worker.err(sve)
        self.var_sve.set(self.sve)

    # кту
    def set_ktu(self):
        ktu = self.var_ktu.get()
        self.ktu = Worker.err(ktu)
        self.var_ktu.set(self.ktu)

    # реальный кту
    def set_ktu_r(self, ktu_r=0):
        self.ktu_r = Worker.err(ktu_r)

    # отработанные субботы
    def set_otr_s(self):
        otr_s = self.var_otr_s.get()
        self.otr_s = Worker.err(otr_s)
        self.var_otr_s.set(self.otr_s)

    # закрытые субботы
    def set_zak_s(self):
        zak_s = self.var_zak_s.get()
        self.zak_s = Worker.err(zak_s)
        self.var_zak_s.set(self.zak_s)

    # коэф без суббот
    def set_coef(self):
        if (self.otr + self.sve) != 0 and self.zak:
            self.coef = self.zak / (self.otr + self.sve)
        else:
            self.coef = 0

    # коэф с субботами
    def set_coef_s(self):
        if self.otr_s and self.zak_s:
            self.coef_s = self.zak_s / self.otr_s
        else:
            self.otr_s = 0

    # общий коэф
    def set_coef_f(self):
        if self.otr == 0 and self.sve == 0:
            self.zak = 0
        if self.zak == 0:
            self.otr = 0
            self.sve = 0
        if self.otr_s == 0:
            self.zak_s = 0
        if self.zak_s == 0:
            self.otr_s = 0
        if(self.otr + self.otr_s + self.sve) != 0:
            self.coef_f = (self.zak + self.zak_s) / (self.otr + self.otr_s + self.sve)
        else:
            self.coef_f = 0
        self.var_coef_f.set(Worker.err(self.coef_f))

    # приработок
    def set_prir(self):
        self.prir = (self.zak+self.zak_s) - (self.otr+self.otr_s+self.sve)
        self.prir = Worker.err(self.prir)
        self.var_prir.set(self.prir)

    # должен быть приработок
    def set_prir_d(self, prir_d):
        self.prir_d = Worker.err(prir_d)
        self.var_prir_d.set(self.prir_d)

    # должен быть приработок
    def set_prir_r(self):
        d = self.prir - self.prir_d
        self.var_prir_r.set(Worker.err(d))


    # ==========================================================================

    # функции возвращающие параметры
    # имя
    def get_name(self):
        return self.name

    # отработанные
    def get_otr(self):
        return self.otr

    # закрытые
    def get_zak(self):
        return self.zak

    # сверхурочные
    def get_sve(self):
        return self.sve

    # кту
    def get_ktu(self):
        return self.ktu

    # реальный кту
    def get_ktu_r(self):
        self.ktu_r = round(self.ktu_r, 2)
        return self.ktu_r

    # отработанные субботы
    def get_otr_s(self):
        return self.otr_s

    # закрытые субботы
    def get_zak_s(self):
        return self.zak_s

    # коэф без суббоt
    def get_coef(self):
        self.coef = round(self.coef, 2)
        return self.coef

    # коэф с субботами
    def get_coef_s(self):
        self.coef_s = round(self.coef_s, 2)
        return self.coef_s

    # общий коэф
    def get_coef_f(self):
        self.coef_f = round(self.coef_f, 2)
        return self.coef_f

    # приработок
    def get_prir(self):
        return self.prir

    # приработок по кту
    def get_prir_r(self):
        return self.prir


    # общие отработанные
    def get_otr_o(self):
        self.otr_o = self.otr+self.otr_s+self.sve
        self.otr_o = round(self.otr_o, 2)
        return self.otr_o
    # ==========================================================================

    # выводим в stdout полную инфу о рабочем
    def __str__(self):
        return ("рабочий:     {}\n"
                "отработано:  {}\n"
                "закрыто:     {}\n"
                "сверхурочн:  {}\n"
                "субботы отр: {}\n"
                "субботы зак: {}\n"
                "приработок:  {}\n"
                "коэф без сб: {}\n"
                "коэф за суб: {}\n"
                "коэф общий:  {}\n"
                "КТУ:         {}\n"
                "реал. КТУ:   {}".format(self.get_name(),
                                         self.get_otr(),
                                         self.get_zak(),
                                         self.get_sve(),
                                         self.get_otr_s(),
                                         self.get_zak_s(),
                                         self.get_prir(),
                                         self.get_coef(),
                                         self.get_coef_s(),
                                         self.get_coef_f(),
                                         self.get_ktu(),
                                         self.get_ktu_r()))


if __name__ == '__main__':
    # выведем все атрибуты класса
    worker = Worker()

    worker.set_otr(220)
    worker.set_zak(300)
    worker.set_sve(20)
    worker.set_otr_s(12)
    worker.set_zak_s(18)

    worker.set_coef()
    worker.set_coef_s()
    worker.set_coef_f()
    print(worker.get_coef(), worker.get_coef_s(), worker.get_coef_f())
