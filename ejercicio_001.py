with open("C:/Users/adpar/ejercicio-001-adpardo1/informacion.txt") as file:
    lines = file.readlines()
    for index, line in enumerate(lines, start=1):
        print(f"Línea {index}: {line.strip()}")
