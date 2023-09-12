from Backstage.menus import *

mensagem_boas_vindas()
dic = {}
dic, cpf = area_login(dic)
menu(dic, cpf)
functions.volte_sempre()