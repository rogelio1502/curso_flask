from jinja2 import Template

# Plantillas sencillas

temp1='Hola {{nombre}}'
print(Template(temp1).render(nombre="Pepe"))

temp2='<a href="{{ url }}"> {{ enlace }}</a>'
print(Template(temp2).render(url="http://www.flask.com",enlace="Flask"))

temp3='<a href="{{ datos[0] }}"> {{ datos[1] }}</a>'
print(Template(temp3).render(datos=["http://www.flask.com","Flask"]))

temp4='<a href="{{ datos.url }}"> {{ datos.enlace }}</a>'
print(Template(temp4).render(datos={"url":"http://www.flask.com","enlace":"Flask"}))

# Ejemplos de filtros

temp5='Hola {{nombre|striptags|title}}'
print(Template(temp5).render(nombre="   pepe  "))

temp6="los datos son {{ lista|join(', ') }}"
print(Template(temp6).render(lista=["amarillo","verde","rojo"]))

temp6="El ultimo elemento tiene {{ lista|last|length}} caracteres"
print(Template(temp6).render(lista=["amarillo","verde","rojo"]))

