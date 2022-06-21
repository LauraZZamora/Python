import random # se importa la libreria de python random

sujetos = ["mami", "bebe", "princess", "mami"] # se define una lista
intenciones = ["yo quiero", "yo puedo", "yo vengo a", "voy a"]
verbos = ["encendelte", "amalte", "ligal", "jugal"]
advs = ["suave", "lento", "lapido", "fuelte"]
complementos_uno = ["hasta que salga el sol", "toda la noche","hasta el amanecer", "todo el dia"]
complementos_dos = ["sin anestesia", "sin compromiso", "feis to feis","sin miedo"]


sujeto_seleccionado = random.choice(sujetos)
# se utiliza la libreria random para seleccionar un elemento al azar de la lista sujetos
intencion_seleccionada = random.choice(intenciones)
verbo_seleccionado = random.choice(verbos)
adv_seleccionado = random.choice(advs)
compl1s_seleccionado = random.choice(complementos_uno)
compl2s_seleccionado = random.choice(complementos_dos)

print("letra generada: " + sujeto_seleccionado + " "+ intencion_seleccionada + " " + verbo_seleccionado + " "+ adv_seleccionado + " " + compl1s_seleccionado + " "+ compl2s_seleccionado) # se imprime la cancion
