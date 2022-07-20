from config.wsgi import *
from core.erp.models import Type

# Listar()
# query = Type.objects.all()
# print(query)

# Insertar datos 1. forma de hacerlo
# t=Type(name='Inversor')
# t.save()

# Edicion
# try:
#     t = Type.objects.get(pk=12)
#     t.name = 'Presidente'
#     t.save()
# except Exception as e:
#         print(e)

# t =Type.objects.get(pk=9)
# t.delete()
# print(f'Objecto eliminado: {t}')


# Filter

x= Type.objects.filter(name__startswith='m')
print(x)

i = Type.objects.filter(name__startswith='P')
print(i)