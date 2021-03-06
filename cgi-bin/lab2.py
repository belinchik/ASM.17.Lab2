﻿import cgi, cgitb, os, sys, codecs

cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

import st00.main
import st01.main
import st23.main
import st07.main
import st27.main
import st24.main
import st27.main
import st16.main
import st39.main
import st31.main
import st09.main
import st17.main
import st32.main
import st05.main
import st22.main
import st34.main

#	добавить импорт своего модуля по шаблону 
#	import st<номер по журналу>.main


MENU = [
        ["[00] Образец", st00.main.main],
        ["[01] Абдуллатипова", st01.main.main],
        ["[07] Белова", st07.main.main],
        ["[23] Ишмаметьев", st23.main.main],
        ["[27] Ларионов", st27.main.main],
        ["[24] Кондрат", st24.main.main],
        ["[27] Ларионов", st27.main.main],
	["[16] Гаврилов", st16.main.main],
	["[39] Тимошин", st39.main.main],
	["[31] Николаева", st31.main.main],
        ["[09] Беркита", st09.main.main],
        ["[17] Григорян", st17.main.main],
        ["[32] Паньшина", st32.main.main],
        ["[05] Баганов", st05.main.main],
        ["[22] Иванов", st22.main.main],
		["[34] Попова", st34.main.main],
#		добавить пункт меню для вызова своей главной функции по шаблону:
#		["[<номер по журналу>] <Фамилия>", <ссылка на функцию>],
	]


def menu(selfurl):
	print ("Content-type: text/html; charset=utf-8\n\n")
	print ('<pre>------------------------------');
	for i, item in enumerate(MENU):
		print('<a href="{0}?student={1}">{2}</a>'.format(selfurl, i+1, item[0]))
	print ("------------------------------</pre>");


def main():
	q = cgi.FieldStorage()
	selfurl = os.environ['SCRIPT_NAME']
	st = int(q.getvalue('student', 0))
	if st > 0 and st <= len(MENU):
		MENU[st-1][1](q, selfurl)
	else:
		menu(selfurl)

main()
