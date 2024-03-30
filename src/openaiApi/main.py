
from openai import OpenAI
from datetime import date, datetime
from openaiApi import config
today = date.today()
tomorrow = str(today).split('-')
tomorrow[2] = str(int(tomorrow[2])+1)
hora = datetime.now().strftime("%H:%M")
hoy = date.today().strftime("%A")
# Crea una instancia del cliente de OpenAI
client = OpenAI(api_key=config.api_key)
def AiGenerator(peticion,names):
    if names is None:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "La fecha actual es: "+str(today)+" Hoy es: "+str(hoy)+" y la hora actual es: "+hora+". Eres un asistente en una app de administracion de tareas, Tendras que generar una tarea que tienen los siguientes atributos:Nombre, Descripcion, Fecha y Hora.Estos los obtendras analizando el texto del usuario Por ejemplo si te dijeran:Mañana tengo una reunion a las 2pm. Tu tendrias que devolver la siguiente cadena separando cada parte con un _ asi:Reunion_Tienes una reunion_"+(tomorrow[0]+'-'+tomorrow[1]+'-'+tomorrow[2])+"_14:00. Siempre con el siguiente orden: Nombre, Descripcion, Fecha y por ultima la Hora es inportante que manejes este orden o habra errores. Si el usuario no te proporciona fecha u hora deberas crear la tarea con la fecha y hora actuales"},
                {"role": "user", "content": peticion}
            ]
        )
    else:
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "La fecha actual es: "+str(today)+" Hoy es: "+str(hoy)+" y la hora actual es: "+hora+". Eres un asistente en una app de administracion de tareas, Tendras que generar una tarea que tienen los siguientes atributos:Nombre, Descripcion, Fecha y Hora.Estos los obtendras analizando el texto del usuario Por ejemplo si te dijeran:Mañana tengo una reunion a las 2pm. Tu tendrias que devolver la siguiente cadena separando cada parte con un _ asi:Reunion_Tienes una reunion_"+(tomorrow[0]+'-'+tomorrow[1]+'-'+tomorrow[2])+"_14:00. Siempre con el siguiente orden: Nombre, Descripcion, Fecha y por ultima la Hora es inportante que manejes este orden o habra errores. Por ultimo verifica que el nombre de la tarea que vayas a crear no sea igual a alguna de las sigueintes(Sin diferenciar entre mayusculas y minusculas):"+str(names)+" En caso de ser igual a alguna deberas cambiar el nombre añadiendole un numero Por ejemplo si la tarea se llama:Reunion y ya existe en la lista ahora el nombre sera:Reunion2 .sumandole 1 al numero la proxima vez que se repita .Por ultimo es mui inportante que devuelvas la tarea con la estructura adecuada:Nombre_Descripcion_Fecha_Hora .Reemplazando Nombre,Descripcion,Fecha y Hora con la informacion de la tarea que hayas creado. Si el usuario no te proporciona fecha u hora deberas crear la tarea con la fecha y hora actuales."},
            {"role": "user", "content": peticion}
        ]
    )
    return completion.choices[0].message.content