import datetime 

import random 

import pytz  

import qrcode

def generar_codigo_qr(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save("sebas_bot_qr.png")
    print("Código QR generado y guardado como 'sebas_bot_qr.png'.")

#días y meses en español 

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"] 

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"] 

 

# Configuración de la zona horaria de Colombia (Bogotá) 

zona_horaria_colombia = pytz.timezone('America/Bogota') 

 

def obtener_saludo(): 

    """ 

    Devuelve un saludo basado en la hora actual. 

    """ 

    now = datetime.datetime.now(zona_horaria_colombia)  # Obtener hora de Colombia 

    hour = now.hour 

    if 6 <= hour < 12: 

        return "Buenos días" 

    elif 12 <= hour < 19: 

        return "Buenas tardes" 

    else: 

        return "Buenas noches" 

 

def sebas_bot(): 

    """ 

    Simula una interacción básica con el asistente virtual Sebas Bot. 

    """ 

    saludo = obtener_saludo() 

    print(f"{saludo}! ¿Cómo estás?") 

    respuesta = input() 

     

    if 'bien' in respuesta.lower(): 

        print("Me alegra que estés bien.") 

    else: 

        print("Espero que todo esté bien.") 

     

    while True: 

        pregunta = input("Escribe tu pregunta (o escribe 'salir' para terminar): ").lower() 

 

        if pregunta == 'salir': 

            print("¡Hasta luego!") 

            break 

        elif pregunta == "como estas": 

            respuestas = [ 

                "Estoy bien, gracias por preguntar.",  

                "Genial, listo para ayudarte.",  

                "Excelente, ¿y tú?" 

            ] 

            print(random.choice(respuestas)) 

 

        elif pregunta == "que dia es hoy?": 

            now = datetime.datetime.now(zona_horaria_colombia)  # Hora de Colombia 

            # Utilizamos los diccionarios para obtener el nombre del día y el mes en español 

            dia_semana = dias[now.weekday()] 

            mes = meses[now.month - 1] 

            print(f"Hoy es {dia_semana}, {now.day} de {mes} de {now.year}")  # Día en español. 

    

        elif pregunta == "que hora es?": 

            now = datetime.datetime.now(zona_horaria_colombia)  # Hora de Colombia 

            print(f"Son las {now.strftime('%I:%M:%S %p')} en el horario de Colombia.")  # Formato 12 horas con AM/PM 

 

        elif pregunta == "en que año estamos?": 

            now = datetime.datetime.now(zona_horaria_colombia)  # Hora de Colombia 

            print(f"Estamos en el año {now.year}.") 

 

        elif pregunta == "como esta el clima hoy?": 

            # respuesta sobre el clima 

            respuestas_clima = [ 

                "El clima está soleado.",  

                "Está nublado.",  

                "Está lloviendo.",  

                "El clima es agradable." 

            ] 

            print(random.choice(respuestas_clima)) 

 

        elif pregunta == "quien eres?": 

            print("Soy Sebas Bot, tu asistente virtual.") 

 

        elif pregunta == "cual es tu nombre?": 

            print("Mi nombre es Sebas Bot.") 

 

        elif pregunta == "que puedes hacer?": 

            print( 

                "Puedo decirte la hora, el día, el año, el clima (de manera simulada por ahora). " 

                "También puedo responder a otras preguntas básicas." 

            ) 

 

        else: 

            print("Lo siento, no entiendo tu pregunta. Intenta de nuevo.") 

 

if __name__ == "__main__": 

    print("¡Hola! Soy Sebas Bot. Escribe 'salir' para terminar.") 

    sebas_bot() 