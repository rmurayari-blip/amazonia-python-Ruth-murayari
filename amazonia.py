animales = [
    {"nombre": "jaguar","dato": "es el felino mas grande de America."},

]

print("=== animales de la Amazonia ===")
for animal in animales:
    print(f"-{animal['nombre']}:{animal['dato']}")