from pprint import pprint

arvore100={'raiz':100,
           'direita':{'raiz': 110, 'esquerda':{}, 'direita': {}},
           'esquerda':{'raiz': 30, 'esquerda':{}, 'direita': {'raiz': 40, 'esquerda':{}, 'direita': {}}}
           }


# def busca(arvore,procurado):
#     while True:
#         if arvore == {}
#             return False
#         elif arvore ['raiz'] == procurado:
#             return True
#         elif procurado < arvore ['raiz']:
#             arvore = arvore['esquerda']
#         elif procurado > arvore ['raiz']:
#             arvore = arvore['direita']

# busca(arvore100,3)


def insere(arvore,elemento):
    while True:
        if arvore == {}:
            arvore ['raiz'] = elemento
            arvore['esquerda'] = {}
            arvore['direita'] = {}
            return
        elif arvore ['raiz'] == elemento:
            return
        elif arvore ['raiz'] > elemento:
            arvore = arvore ['esquerda']
        elif arvore ['raiz'] < elemento:
            arvore = arvore ['direita']

pprint(arvore100)
insere(arvore100, 10)
pprint(arvore100)
insere(arvore100, 8)
pprint(arvore100)
insere(arvore100, 50)
pprint(arvore100)
            