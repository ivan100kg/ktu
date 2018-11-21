#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ivar at 05.11.2018

# функции


# общие бригадные отработанные часы
def get_brig_otr(workers):
    hours = 0
    for worker in workers:
        hours += worker.get_otr()
    hours = round(hours, 2)
    return hours


# общие бригадные отработанные субботние часы
def get_brig_otr_s(workers):
    hours = 0
    for worker in workers:
        hours += worker.get_otr_s()
    hours = round(hours, 2)
    return hours


# общие бригадные сверхурочные
def get_brig_sve(workers):
    hours = 0
    for worker in workers:
        hours += worker.get_sve()
    hours = round(hours, 2)
    return hours


# общие бригадные закрытые часы
def get_brig_zak(workers):
    hours = 0
    for worker in workers:
        hours += worker.get_zak()
    hours = round(hours, 2)
    return hours


# общие бригадные закрытые субботние часы
def get_brig_zak_s(workers):
    hours = 0
    for worker in workers:
        hours += worker.get_zak_s()
    hours = round(hours, 2)
    return hours


# общий бригадный коэф переработки без суббот
def get_brig_coef(workers):
    otr = get_brig_otr(workers)
    zak = get_brig_zak(workers)
    sve = get_brig_sve(workers)
    coef = 0
    if (otr + sve) != 0 and zak:
        coef = zak / (otr + sve)
        coef = round(coef, 2)    
    return coef

        
# общий бригадный коэф переработки за субботы
def get_brig_coef_s(workers):
    otr = get_brig_otr_s(workers)
    zak = get_brig_zak_s(workers)    
    coef = 0
    if otr and zak:
        coef = zak / otr
        coef = round(coef, 2)
    return coef


# общий бригадный коэф переработки с субботами
def get_brig_coef_f(workers):
    otr = get_brig_otr(workers)
    zak = get_brig_zak(workers)
    sve = get_brig_sve(workers)
    otr_s = get_brig_otr_s(workers)
    zak_s = get_brig_zak_s(workers)
    coef = 0
    if otr == 0 and sve == 0:
        zak = 0
    if zak == 0:
        otr = 0
        sve = 0
    if otr_s == 0:
        zak_s = 0
    if zak_s == 0:
        otr_s = 0
    if (otr + otr_s + sve) != 0:
        coef = (zak + zak_s) / (otr + otr_s + sve)
        coef = round(coef, 2)
    return coef


# выводит в терминал бригадные часы и коэффициенты
def print_all(workers):
    print("отработано:  ", get_brig_otr(workers))
    print("отраб субб:  ", get_brig_otr_s(workers))
    print("сверхкрочн:  ", get_brig_sve(workers))
    print("закрытые:    ", get_brig_zak(workers))
    print("закр субб:   ", get_brig_zak_s(workers))
    print("приработок:  ", prirabotok(workers))
    print("коэф без сб: ", get_brig_coef(workers))
    print("коэф за су:  ", get_brig_coef_s(workers))
    print("коэф общий:  ", get_brig_coef_f(workers))


# приработок
def prirabotok(workers):
    otr = get_brig_otr(workers)
    zak = get_brig_zak(workers)
    sve = get_brig_sve(workers)
    otr_s = get_brig_otr_s(workers)
    zak_s = get_brig_zak_s(workers)
    hours = (zak + zak_s) - (otr + otr_s + sve)
    if hours <= 0:
        hours = 0
    hours = round(hours, 2)
    return hours

# реальный кту
def real_ktu(workers):
    # сумма всех отраб*кту
    sum_ktu_otr = sum([worker.get_ktu()*worker.get_otr_o() for worker in workers])
    prir_o = prirabotok(workers)

    for worker in workers:
        try:
            worker.set_ktu_r((worker.get_prir() * sum_ktu_otr) / ((prir_o*worker.get_otr_o())))
        except ZeroDivisionError as err:
            print(err)
            worker.set_ktu_r(0)

# какой должен быть приработок
def prir_dol(workers):
    sum_ktu_otr = sum([worker.get_ktu() * worker.get_otr_o() for worker in workers])

    try:
        temp = prirabotok(workers) / sum_ktu_otr
    except ZeroDivisionError:
        temp = 0

    for worker in workers:
        worker.set_prir_d(temp * worker.get_ktu() * worker.get_otr_o())
        worker.set_prir_r()
