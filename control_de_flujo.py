lista = [1,2,3,4,'5','hola',False]

users = [
    {
        'name': 'Diego',
        'username': 'DzRM',
        'correo': 'gg@gmal.com',
    },
    {
        'name': 'Dani',
        'username': 'DaGod',
        'correo': 'hh@gmal.com',
    },
    {
        'name': 'Angel',
        'username': 'AnGod',
        'correo': 'jj@gmal.com',
    }
]

#print(len(lista))

for i in range(len(users)):
    print(users[i]['name'])

for usuario in users:
    print(usuario['name'])
    print(usuario['correo'])

    # if user['name']=='Diego':
    #     print('Es el Diego')
    # elif user['name']=='Dani':
    #     print('Es Dani')
    # else:
    #     print('Es un random')


# switch (user['name']):
#     case 'Dani':
#         print('Es Dani')
#     case 'Diego':
#         print('Es Diego')