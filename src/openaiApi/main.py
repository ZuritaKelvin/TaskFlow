
from openai import OpenAI
from datetime import date, datetime
from openaiApi import config
today = date.today()
tomorrow = str(today).split('-')
tomorrow[2] = str(int(tomorrow[2])+1)
hora = datetime.now().strftime("%H:%M")
hoy = date.today().strftime("%A")

client = OpenAI(api_key=config.api_key)
def AiGenerator(peticion):
    """AiGenerator

    Args:
        peticion (str): the user text i will use for the Get Request.

    Returns:
        list: Returns a list with the result of Get Request.
    """
    completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "La fecha actual es: "+str(today)+" Hoy es: "+str(hoy)+" y la hora actual es: "+hora+". Eres un asistente en una app de administracion de tareas, Tendras que generar una tarea que tienen los siguientes atributos:Nombre, Descripcion, Fecha y Hora.Estos los obtendras analizando el texto del usuario Por ejemplo si te dijeran:Mañana tengo una reunion a las 2pm. Tu tendrias que devolver la siguiente cadena separando cada parte con un _ asi:Reunion_Tienes una reunion_"+(tomorrow[0]+'-'+tomorrow[1]+'-'+tomorrow[2])+"_14:00. Siempre con el siguiente orden: Nombre, Descripcion, Fecha y por ultima la Hora es inportante que manejes este orden o habra errores. Si el usuario no te proporciona fecha u hora deberas crear la tarea con la fecha y hora actuales"},
                {"role": "user", "content": peticion}
            ]
        )
    return completion.choices[0].message.content
def getEvent(peticion):
    """getEvent method\n

    Args:
        peticion (string): The task that u want to get the Event.

    Returns:
        string: Event of the task provided
    """
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tu tarea es en base al mensaje del usuario que sera una tarea que hacer devolveras un titulo un datetime de inicio de la tare y un datetime final de la tarea por ejemplo si el usuario te la da siguiente tarea:Reunion.Tengo una reunion de 1 hora.2024-05-21.12:21 Tu tarea de igual manera sera dar la siguiente respuesta separando cada item con un punto '.' asi:Reunion.2024.5.21.12.21.2024.5.21.13.21"},
            {"role": "user", "content": peticion}
        ]
    )
    return completion.choices[0].message.content