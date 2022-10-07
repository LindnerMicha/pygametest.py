import turtle # kleines visualisierungs modul

wn = turtle.Screen()
wn.title("Ping Pong Motherfucker")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)                                                                    # verhindert das ständige Auffrischen des bildschirms

#main game loop
while True:
    wn.update()

