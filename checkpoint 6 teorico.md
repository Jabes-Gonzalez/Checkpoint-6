# ¿Para qué usamos Clases en Python?
Una clase es un concepto abstracto que define atributos y métodos que un objeto puede tener. Las clases de Python actúan como plantillas para crear objetos concretos, que son instancias de esa clase. Por ejemplo, una clase podría llamarse Coche y podría tener atributos como color y marca, y métodos como ```__conducir__``` o ```__frenar__```.

Cada objeto de una clase puede tener sus propios valores para los atributos, pero **comparte los métodos y la estructura básica de comportamiento con otras instancias** de la misma clase. Por ejemplo, se puede crear un objeto mi_coche de la clase Coche con el color ```__rojo__``` y la marca ```__Toyota__``` y la instancia heredará automáticamente los métodos ```__conducir__``` o ```__frenar__``` de la clase.

### Cómo crear clases de Python
Puedes definir clases en Python escribiendo la palabra clave class seguida del nombre de la clase y dos puntos.

```Python
class MyClass:
    # Constructor method called when creating an object
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
    
    # Method defined within the class
    def my_method(self):
        return f"Attribute 1: {self.attribute1}, Attribute 2: {self.attribute2}"
```

En este código Python, hemos creado una clase llamada MyClass que tiene un **constructor** ```__init__``` al que se accede al crear un objeto y que inicializa dos atributos, el ```attribute1``` y el ```attribute2```. El método ```my_method``` devuelve una cadena formateada que contiene los valores de esos atributos.

Para crear un objeto basado en esta clase, debes utilizar el nombre de la clase seguido de paréntesis:

```Python
object1 = MyClass("Value 1", "Value 2")
result = object1.my_method()
```

### Ejemplos de uso de las clases de Python
Las clases de Python pueden crear sistemas complejos y relaciones entre distintas entidades. A continuación, te enseñamos algunas formas de trabajar con ellas.

La función ```__str__```() en Python es un método especial que puedes definir dentro de las clases de Python. Cuando se implementa, devuelve una cadena con una **representación sencilla de un objeto**. Puedes aplicar la función ```str()``` directamente al objeto o combinarla con una instrucción ```print()```.

```Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
person1 = Person("Alice", 30)
print(person1) # Output: Name: Alice, Age: 30
```

En este código, el método ```__str__()``` dentro de la clase ```Person``` crea una **cadena formateada** que contiene el nombre y la edad de una persona. Cuando se ejecuta ```print(person1)```, llama automáticamente al método ```__str__()``` del objeto ```person1``` y da como resultado la cadena que este método ha devuelto.

#### Definir métodos en clases de Python
En Python también es posible establecer métodos dentro de una clase para ejecutar operaciones sobre los objetos de esta clase. Por lo tanto, los objetos creados pueden llamar a dichos métodos.

```Python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
# Creating an object of the class
my_rectangle = Rectangle(5, 10)
# Calling methods of the object
area = my_rectangle.area()
perimeter = my_rectangle.perimeter()
# Printing the calculated values
print("Area =", area) # Output: Area = 50
print("Perimeter =", perimeter) # Output: Perimeter = 30
```

En el ejemplo anterior, hemos creado la clase ```Rectangle```, que incluye los dos métodos ```area()``` y ```perimeter()```. Estos métodos sirven para calcular el área y el perímetro de un rectángulo basándose en los valores de longitud y anchura que se pasaron al inicializar el objeto. En Python, ```self``` en un método de clase representa una **referencia al objeto actual** al que se aplica el método.

El objeto ```my_rectangle``` se crea con una longitud de 5 y una anchura de 10. Después, se ha llamado a los métodos ```area()``` y ```perimeter()``` sobre este objeto para calcular los valores respectivos.

#### Cambiar las propiedades de objetos
Puedes utilizar el operador punto ```.``` para acceder a **atributos específicos de un objeto** y actualizar sus valores. Puedes asignar nuevos valores directamente al atributo tal y como podemos apreciar a continuación:

```Python
person1.name = "Sarah"
person1.age = 35
```
La palabra clave ```del``` sirve para eliminar propiedades de un objeto. En el ejemplo que sigue, se está eliminando la propiedad name del objeto person1:
```Python
del person1.name
```

# ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?
El método especial ```__init__``` en Python es el constructor de una clase, es decir, el método que se ejecuta automáticamente al crear una nueva instancia (objeto) de esa clase. Su función principal es inicializar los atributos del objeto, estableciendo su estado inicial con los valores que se le pasen o con valores por defecto.

**¿Qué es ```__init__```?**
* Es un método especial con un nombre reservado: comienza y termina con doble guion bajo ```(__init__)```.

* Se llama automáticamente cuando se crea un objeto, sin necesidad de invocarlo explícitamente.

* Recibe como primer argumento self, que representa la instancia que se está creando.

* Puede recibir argumentos adicionales para inicializar atributos con valores específicos.
###### Sintaxis básica
```Python
class MiClase:
    def __init__(self, parametro1, parametro2):
        self.atributo1 = parametro1
        self.atributo2 = parametro2
```
###### Al crear un objeto:
```Python
obj = MiClase(valor1, valor2)
```
###### Python ejecutará internamente:
```Python
obj.__init__(valor1, valor2)
```
##### Ejemplo práctico:
```Python
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Sueldo: {self.sueldo}")

empleado1 = Empleado("Ana", 3500)
empleado1.imprimir()
```
##### Salida:
```Python
Nombre: Ana
Sueldo: 3500
```
En este ejemplo ```__init__``` asigna los valores recibidos a los atributos del objeto, que luego pueden usarse en otros métodos.

#### Ventajas y características
* Automatiza la inicialización ya que no es necesario llamar explícitamente a un método para asignar atributos.

* Nos otorga flexibilidad ya que Puede recibir parámetros para configurar cada objeto con valores diferentes.

* Nos permite definir argumentos con valores predeterminados para que no siempre sea obligatorio pasarlos.

#### ¿Por qué usar init?
* Nos facilita la creación de objetos con atributos ya definidos y listos para usar.

* Nos permite Evitar errores al olvidar asignar atributos manualmente.

* Nos mejora la legibilidad y mantenibilidad del código orientado a objetos.

* Es equivalente al constructor en otros lenguajes de programación, pero con la ventaja de ser un método más flexible y explícito.

#### En resumen:
* ```__init__``` es un método especial que inicializa un objeto al momento de crearlo.

* Siempre recibe self como primer parámetro y puede recibir otros argumentos para configurar el objeto.

* Se ejecuta automáticamente y no debe llamarse directamente.

* Permite definir atributos con valores personalizados o por defecto.

* Es fundamental para la programación orientada a objetos en Python, facilitando la creación y configuración de instancias.

# ¿Cuáles son los tres verbos de API?
En el desarrollo de **APIs REST**, los verbos **HTTP** definen las acciones que se pueden realizar sobre los recursos. Los tres verbos más comunes y esenciales son:

* GET: Obtener información.

* POST: Crear nuevos recursos o enviar datos.

* DELETE: Eliminar recursos existentes.

Cada verbo tiene un propósito claro y reglas que ayudan a mantener la coherencia y semántica en la comunicación cliente-servidor.

#### VERBO HTTP GET:
El verbo GET se utiliza para recuperar o solicitar información de un recurso en el servidor sin modificarlo.

###### Características:
* Seguro: No debe cambiar el estado del recurso ni del servidor.

* Idempotente: Realizar la misma solicitud varias veces produce el mismo resultado.

* Cacheable: Las respuestas pueden ser almacenadas en caché para mejorar el rendimiento.

* Datos enviados en la URL: Generalmente a través de parámetros de consulta.

###### Usos comunes:
* Obtener una lista de recursos (ej. todos los usuarios).

* Obtener un recurso específico (ej. detalles de un usuario por ID).

* Consultar información sin modificar nada.
###### Ejemplo:
```text
GET /api/usuarios HTTP/1.1
Host: ejemplo.com
```
###### Respuesta (JSON):
```json
[
  {"id": 1, "nombre": "Ana"},
  {"id": 2, "nombre": "Luis"}
]
```
#### VERBO HTTP POST:
El verbo POST se utiliza para crear un nuevo recurso o enviar datos al servidor para que sean procesados.

###### Características:
* No idempotente: Repetir la misma solicitud puede crear múltiples recursos o causar efectos secundarios.

* Modifica el estado del servidor.

* Datos enviados en el cuerpo (body) de la solicitud.

###### Usos comunes:
* Crear un nuevo recurso (ej. registrar un nuevo usuario).

* Enviar datos para procesamiento (formularios, archivos).

* Acciones que generan cambios en el servidor.

###### Ejemplo:
```text
POST /api/usuarios HTTP/1.1
Host: ejemplo.com
Content-Type: application/json

{
  "nombre": "Carlos",
  "email": "carlos@example.com"
}
```
###### Respuesta:
```text
HTTP/1.1 201 Created
Location: /api/usuarios/3
```
#### VERBO HTTP DELETE
El verbo DELETE se utiliza para eliminar un recurso existente en el servidor.

###### Características:
* Idempotente: Repetir la misma solicitud DELETE no cambia el resultado después de la primera vez.

* Modifica el estado del servidor.

* Generalmente no tiene cuerpo en la petición.

* Puede devolver un código de estado que indique éxito o fallo.

##### Usos comunes:
* Eliminar un recurso específico (ej. borrar un usuario por ID).

* Eliminar colecciones o recursos relacionados (según diseño de API).
###### Ejemplo:
```text
DELETE /api/usuarios/3 HTTP/1.1
Host: ejemplo.com
```
###### Respuesta:
```text
HTTP/1.1 204 No Content
```
#### Comparación entre GET, POST y DELETE:
![alt text](image.png)

#### Buenas prácticas al usar GET, POST y DELETE:
* Usa GET para obtener datos sin efectos secundarios.

* Usa POST para crear recursos o enviar datos que modifiquen el servidor.

* Usa DELETE para eliminar recursos de forma clara y segura.

* Utiliza códigos de estado HTTP adecuados:

    * 200 OK para respuestas exitosas con contenido.

    * 201 Created tras crear un recurso con POST.

    * 204 No Content tras eliminar un recurso con DELETE.

    * 404 Not Found si el recurso no existe.

* Documenta claramente qué espera y devuelve cada endpoint.

* Considera la seguridad y autenticación para operaciones que modifican datos.

#### Ejemplo práctico en Python con Flask:
```Python
from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = [
    {"id": 1, "nombre": "Ana"},
    {"id": 2, "nombre": "Luis"}
]

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    nuevo_usuario = request.json
    nuevo_usuario['id'] = len(usuarios) + 1
    usuarios.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    global usuarios
    usuarios = [u for u in usuarios if u['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```
Los verbos HTTP GET, POST y DELETE son pilares fundamentales para construir APIs REST claras, eficientes y semánticamente correctas. Cada uno tiene un rol específico que permite a los clientes interactuar con los recursos del servidor de manera estructurada y predecible.

# ¿Es MongoDB una base de datos SQL o NoSQL?
MongoDB es una base de datos NoSQL de código abierto. Como base de datos no relacional, puede procesar datos estructurados, semiestructurados y no estructurados. Utiliza un modelo de datos no relacional orientado a documentos y un lenguaje de consulta no estructurado.

MongoDB es muy flexible y permite combinar y almacenar múltiples tipos de datos. También almacena y maneja mayores cantidades de datos que las bases de datos relacionales tradicionales. MongoDB usa un formato de almacenamiento de documentos llamado BSON, que es una forma binaria de JSON (JavaScript Object Notation o notación de objetos de JavaScript) que puede acomodar más tipos de datos.

#### Cómo funciona MongoDB:
MongoDB almacena objetos de datos en colecciones y documentos en lugar de las tablas y filas que se utilizan en las bases de datos relacionales tradicionales. Las colecciones comprenden conjuntos de documentos, que son equivalentes a tablas en una base de datos relacional. Los documentos consisten en pares clave-valor, que son la unidad básica de datos en MongoDB.

La estructura de un documento se puede cambiar simplemente añadiendo campos nuevos o eliminando los existentes. Los documentos pueden definir una clave principal como identificador único y los valores pueden ser una variedad de tipos de datos, incluidos otros documentos, matrices y matrices de documentos.

#### Cómo funciona la búsqueda de texto de MongoDB:
Una función clave de MongoDB es la búsqueda de texto, que permite consultar campos de cadena para texto o palabras específicas. Se puede realizar una búsqueda de texto usando un índice de texto o el operador $text.

Un índice de texto puede ser una cadena o una matriz de elementos de cadena. Para hacer una consulta de búsqueda de texto, la colección debe contener un índice de texto. Una colección solo puede tener un índice de texto y un único índice de texto se puede aplicar a varios campos.

También se puede efectuar una búsqueda en una colección con un índice de texto usando el operador $text. El operador $text tokeniza cada cadena de búsqueda con espacios en blanco y trata todos los signos de puntuación excepto "–" y "\" como delimitadores. Después de tokenizar la cadena de búsqueda, el operador realiza la operación lógica OR en los tokens.

#### Ejemplos de consultas de MongoDB:
MongoDB utiliza MongoDB Query Language (MQL) para recuperar datos de la base de datos. Es fácil de usar y funciona de manera similar a SQL con operaciones CRUD para crear, leer, actualizar y eliminar documentos. Los nombres de las funciones siguen la sintaxis:
```
 <database>.<collection_name>. <operation>.
```
###### Ejemplos prácticos:
**INSERT:** Crea o inserta un nuevo documento en una colección. Si la colección no existe, se creará una nueva colección.

    db.collection.insertOne() inserta un documento en una colección.

    db.collection.insertMany() inserta varios documentos en una colección a la vez.

Así es como se ve la inserción de un documento en la colección del cliente:

        db.customer.insertOne (

        {

        firstname: “Marta”,

        lastname: “Casas”

        Address: “Calle Petunias 232, Ciempozuelos, Madrid, 28350”

        }

**FIND:** Esto consulta una colección de documentos. Se pueden aplicar criterios y filtros de consulta para encontrar documentos específicos.

        db.collection.find()

El siguiente código encuentra todos los documentos en la colección del cliente:

        db.customer.find()

UPDATE: Esto modifica los documentos existentes en una colección.

        db.collection.updateOne()

        db.collection.updateMany()

        db.collection.replaceOne()

Así es como actualizaría un documento en la colección de clientes:

        db.customer.updateOne(

        { firstname: “Marta” },

                {

                $set: { “address”, “Calle Lavanda 5, Ciempozuelos, Madrid, 28350”}

                }

        )

### Las tres ventajas principales de MongoDB
###### Flexibilidad:
MongoDB tiene una arquitectura de esquema dinámico que funciona con almacenamiento y datos no estructurados. Como los datos se almacenan en documentos flexibles similares a JSON, el esquema de la base de datos no tiene que estar predefinido y los esquemas se pueden modificar dinámicamente sin causar tiempo de inactividad.

Con el formato de datos BSON de MongoDB, los objetos en una colección pueden tener diferentes conjuntos de campos, y casi cualquier tipo de estructura de datos se puede modelar y manipular. Por esta razón, el modelo de base de datos flexible de MongoDB es especialmente beneficioso a medida que cambian los requisitos de negocio y de datos.

###### Fragmentación
MongoDB ofrece escalabilidad horizontal a través de un proceso llamado fragmentación. La fragmentación divide los datos de un gran conjunto de datos y los distribuye entre varios servidores. Si un servidor no puede gestionar una gran carga de datos, puede dividirse y distribuirse automáticamente sin interrumpir el procesamiento de datos.

###### Mayor Rendimiento
MongoDB almacena los datos en RAM para poder acceder más rápidamente a ellos y conseguir un mayor rendimiento al ejecutar consultas. Recopila los datos directamente de la RAM en lugar del disco duro, lo que hace que la lectura y escritura de datos sea más rápida. La estructura de datos no relacional de MongoDB también implica que necesita menos potencia de procesamiento para buscar y recuperar datos que una base de datos relacional.

### ¿En qué casos sería recomendable usar MongoDB?
###### En Analíticas en Tiempo Real:
Como base de datos NoSQL, MongoDB es una buena opción para integrar y procesar macrodatos (es decir, enormes cantidades de datos diversos demasiado grandes para ser procesados por bases de datos relacionales tradicionales).

MongoDB no tiene esquema y, por tanto, se pueden almacenar y acceder a varios tipos de datos sobre la marcha. El soporte incorporado de MongoDB para fragmentación también le permite escalar datos horizontalmente en múltiples servidores. Además, brinda la flexibilidad necesaria para fusionar cientos de fuentes de datos en una sola vista para el análisis en tiempo real y la integración de datos.

###### Gestión de Contenido:
El modelo de documento no estructurado de MongoDB lo convierte en una excelente opción para la gestión de contenido y la entrega de sitios web de comercio electrónico, publicaciones online y sistemas de gestión de contenido web. Su modelo de datos flexible facilita el almacenamiento de varios tipos de contenido, incluidas imágenes, texto y video, así como metadatos.

Todo el contenido relacionado se almacena en un solo documento, lo que facilita añadir nuevas funciones y atributos MongoDB también se puede usar para almacenar contenido generado por el usuario, como comentarios, que se pueden analizar y usar como orientación del desarrollo de contenido futuro.

# ¿Qué es una API?
Una API, o interfaz de programación de aplicaciones, es un conjunto de reglas o protocolos que permite a las aplicaciones informáticas comunicarse entre sí para intercambiar datos, características y funcionalidades.

Las API simplifican y aceleran el desarrollo de aplicaciones y software permitiendo a los desarrolladores integrar datos, servicios y capacidades de otras aplicaciones, en lugar de desarrollarlas desde cero. Las API también ofrecen a los propietarios de aplicaciones una forma sencilla y segura de poner los datos y las funciones de sus aplicaciones a disposición de los departamentos de su organización. Los propietarios de aplicaciones también pueden compartir o comercializar datos y funciones con Business Partners o terceros.

Las API permiten compartir solo la información necesaria, manteniendo ocultos otros detalles internos del sistema, lo que ayuda a la seguridad del sistema. Los servidores o dispositivos no tienen que exponer completamente los datos: las API permiten compartir pequeños paquetes de datos, relevantes para la solicitud específica.

La documentación de la API es como un manual de instrucciones técnicas que proporciona detalles sobre una API e información para los desarrolladores sobre cómo trabajar con una API y sus servicios. Una documentación bien diseñada promueve una mejor experiencia de API para los usuarios y, en general, hace que las API sean más exitosas.

#### ¿Cómo funcionan las API?
Una forma sencilla de entender cómo funcionan las API es examinar un ejemplo común: el procesamiento de pagos de terceros. Cuando un usuario compra un producto en un sitio de comercio electrónico, es posible que se le pida que "pague con PayPal" u otro tipo de sistema externo. Esta función depende de las API para realizar la conexión.

Cuando el comprador hace clic en el botón de pago, se envía una llamada a la API para recuperar la información. Esta es la petición. Esta solicitud se procesa desde una aplicación al servidor web a través del identificador uniforme de recursos (URI) de la API e incluye un verbo de solicitud, una cabecera y, a veces, un cuerpo de solicitud.
 

Tras recibir una solicitud válida desde la página web del producto, la API llama al programa externo o al servidor web, en este caso, al sistema de pago externo.
 

El servidor envía una respuesta a la API con la información solicitada.
 

La API transfiere los datos a la aplicación solicitante inicial, en este caso, el sitio web del producto.

Si bien la transferencia de datos diferida según el servicio web utilizado, las solicitudes y respuestas se realizan a través de una API. No hay visibilidad en la interfaz de usuario, lo que significa que las API intercambian datos dentro del ordenador o la aplicación, y aparecen ante el usuario como una conexión sin fisuras.

#### Tipos de API
Las API se pueden clasificar por casos de uso: API de datos, API de sistemas operativos, API remotas y API web.

###### API web:
Las API web permiten la transferencia de datos y funcionalidades a través de Internet mediante el protocolo HTTP.

Hoy en día, la mayoría de las API son API web. Las API web son un tipo de API remota (lo que significa que la API utiliza protocolos para manipular recursos externos) que exponen los datos y la funcionalidad de una aplicación a través de Internet.

**Los cuatro tipos principales de API web son:**

###### API abiertas:
Las API abiertas son interfaces de programación de aplicaciones de código abierto que se puede acceder con el protocolo HTTP. También conocidas como API públicas, han definido endpoints de API y formatos de solicitud y respuesta.

###### API de socios:
Las API de socios conectan a Business Partners estratégicos. Normalmente, los programadores acceden a estas API en modo de autoservicio a través de un portal público para programadores de API . Aún así, deben completar un proceso de incorporación y obtener credenciales de inicio de sesión para acceder a las API de socios.

###### API internas:
Las API internas o privadas permanecen ocultas para los usuarios externos. Estas API privadas no están disponibles para usuarios fuera de la empresa. En cambio, las organizaciones los utilizan para mejorar la productividad y la comunicación entre diferentes equipos de desarrollo internos.

###### API compuestas:
Las API compuestas combinan múltiples API de datos o servicios. Permiten a los programadores acceder a varios endpoints en una sola llamada. Las API compuestas son útiles en la arquitectura de microservicios, donde la realización de una única tarea puede requerir información de varias fuentes.

#### Ventajas de la API:
Las API simplifican el diseño y el desarrollo de nuevas aplicaciones y servicios, así como la integración y gestión de las existentes. También ofrecen beneficios significativos a los desarrolladores y a las organizaciones en general.

###### Colaboración mejorada:
La empresa promedio utiliza casi 1200 aplicaciones en la nube, muchas de las cuales están desconectadas. Las API permiten la integración, para que estas plataformas y aplicaciones puedan comunicarse entre sí sin problemas. Mediante esta integración, las empresas pueden automatizar los flujos de trabajo y mejorar la colaboración en el lugar de trabajo. Sin las API, muchas empresas carecerían de conectividad, lo que provocaría silos de información que comprometerían la productividad y el rendimiento.

###### Innovación acelerada:
Las API ofrecen flexibilidad, lo que permite a las empresas establecer conexiones con nuevos business partners y ofrecer nuevos servicios a su mercado existente. Esta flexibilidad también permite a las empresas acceder a nuevos mercados que pueden aumentar los rendimientos e impulsar la transformación digital.

Por ejemplo, la empresa Stripe comenzó como una API con solo siete líneas de código. Desde entonces, la compañía ha trabajado con muchas de las empresas más grandes del mundo. Stripe se ha diversificado para ofrecer préstamos y tarjetas corporativas, y recientemente ha recibido una valoración de 65 000 millones de USD.

###### Monetización de datos:
Muchas empresas optan por ofrecer API gratuitas, al menos al principio, para poder crear una audiencia de desarrolladores en torno a su marca y forjar relaciones con posibles socios. Si la API da acceso a recursos digitales valiosos, una empresa lo monetiza vendiendo el acceso. Esta práctica se conoce como la economía API.

Cuando AccuWeather puso en marcha su portal de autoservicio para desarrolladores con el fin de vender una amplia gama de paquetes de API, tardó solo diez meses en atraer a 24 000 desarrolladores y vender 11 000 claves de API. Este movimiento ayudó a construir una comunidad próspera en el proceso.

###### Seguridad del sistema:
Las API separan la aplicación solicitante de la infraestructura del servicio que responde y ofrecen capas de seguridad entre las dos a medida que se comunican. Por ejemplo, las llamadas a la API suelen requerir credenciales de autenticación. Los encabezados HTTP, cookies o cadenas de consulta pueden proporcionar seguridad adicional durante el intercambio de datos. Una pasarela API puede controlar el acceso para minimizar aún más las amenazas a la seguridad.

###### Seguridad y privacidad del usuario:
Las API brindan protección adicional dentro de una red. También pueden proporcionar otra capa de protección para los usuarios personales. Cuando un sitio web solicita la ubicación de un usuario (una API de ubicación proporciona esta información), el usuario puede decidir si permite o rechaza esta solicitud.

Muchos navegadores web y sistemas operativos móviles y de escritorio tienen estructuras de permisos integradas. Cuando una aplicación debe acceder a los archivos a través de una API, los sistemas operativos como iOS, macOS, Windows y Linux utilizan permisos para ese acceso.

# ¿Qué es Postman?
Postman es una **herramienta de colaboración y desarrollo que permite a los desarrolladores interactuar y probar el funcionamiento de servicios web y aplicaciones**. proporcionando una interfaz gráfica intuitiva y fácil de usar para enviar solicitudes a servidores web y recibir las respuestas correspondientes

Con esta plataforma se puede gestionar diferentes entornos de desarrollo, organizar las solicitudes en colecciones y realizar pruebas automatizadas para verificar el comportamiento de los sistemas. 
Postman es utilizado por los desarrolladores para **testear colecciones y catálogos APIs** (*tanto a nivel front-end como back-end*), para gestionar el ciclo de vida de las APIs, mejorar el trabajo colaborativo y mejorar la organización del proceso de diseño y desarrollo.

#### Cómo funciona Postman:
Este entorno ofrece una GUI que facilita a los desarrolladores el envío de solicitudes HTTP y HTTPS a una API y a gestionar las respuestas recibidas.

Las principales características y funcionalidades de Postman son:

* **Envío de solicitudes:** Permite enviar solicitudes GET, POST, PUT, DELETE y otros métodos HTTP a una API especificando los parámetros, encabezados y cuerpo de la solicitud.
* **Gestión de entornos:** Facilita la configuración para diferentes entornos (por ejemplo, desarrollo, prueba, producción) y el cambio sencillo entre ellos (para realizar pruebas y desarrollo en diferentes contextos).
**Colecciones de solicitudes:** Agrupa las solicitudes relacionadas en colecciones, lo que facilita la organización y ejecución de pruebas automatizadas.
**Pruebas automatizadas:** Es ideal para crear y ejecutar pruebas automatizadas para verificar el comportamiento de una API (detectar errores e incrementar la calidad del software).
**Documentación de API:** Genera de forma automatizada, documentación detallada de la API a partir de las solicitudes y respuestas realizadas, lo que facilita su comprensión y uso por parte de otros desarrolladores.

#### Cuáles son sus ventajas respecto a otras herramientas:
Cada vez son más los desarrolladores y programadores que apuestan por un entorno como Postman para automatizar pruebas y mejorar sus procesos de trabajo. Los principales beneficios que se obtienen con esta herramienta son:

* **Facilidad a la hora de trabajar** al disponer de una interfaz gráfica de usuario intuitiva, sencilla y personalizable.
* **Amplia compatibilidad con numerosas tecnologías y protocolos web**, como por ejemplo; HTTP, HTTPS, REST, SOAP, GraphQL… (lo que permite interaccionar con diversos tipos de API sin complicaciones o problemas).
* Ofrece una **amplia gama de funcionalidades para diseñar, probar y documentar APIs**, siendo probablemente la solución más completa del mercado para gestionar el ciclo de vida completo de desarrollo de APIs.
* **Fomenta y facilita la colaboración** entre los miembros del equipo de desarrollo (con opciones interesantes como compartir colecciones de solicitudes con otros desarrolladores).
* Cuenta con una **comunidad amplia de usuarios que está en constante crecimiento** y que aporta una gran cantidad de recursos, como tutoriales, documentación, foros y grupos de discusión…
* **Se integra perfectamente con varias herramientas populares utilizadas en el desarrollo de software**. Por ejemplo, se puede conectar con sistemas de control de versiones como GitHub, servicios de generación de documentación como Swagger o herramientas de automatización de pruebas como Jenkins, entre muchas otras.
* Permite a los usuarios **agregar scripts personalizados utilizando JavaScript** (para automatizar tareas repetitivas, configurar pruebas avanzadas o agregar validaciones personalizadas a las respuestas de la API).
* Las colecciones son una característica central de Postman que permite **organizar y agrupar solicitudes relacionadas**. Esto simplifica la administración de API complejas y facilita la reutilización de solicitudes y flujos de trabajo en diferentes proyectos.

# ¿Qué es el polimorfismo?
El polimorfismo es un principio fundamental de la programación orientada a objetos (POO) que permite que diferentes objetos respondan de manera distinta a un mismo llamado de método. En otras palabras, un mismo método o función puede comportarse de formas diferentes según el objeto que lo invoque.

En Python, gracias a su tipado dinámico y a características como el duck typing, el polimorfismo es especialmente flexible: no es necesario que los objetos compartan una interfaz común, basta con que tengan los métodos que se desean usar.

###### Conceptos clave relacionados:
* Herencia: Permite que una clase hija herede atributos y métodos de una clase padre.

* Sobrescritura (overriding): Una clase hija redefine un método heredado para modificar su comportamiento.

* Duck typing: "Si camina como un pato y suena como un pato, entonces es un pato". En Python, la compatibilidad se basa en la presencia de métodos o atributos, no en la herencia explícita.

**Ejemplo básico de polimorfismo con herencia:**
```python
class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")

for animal in [Perro(), Gato()]:
    animal.hablar()
```
**Salida:**
```text
Guau!
Miau!
```
Aquí, el método ```hablar()``` se comporta diferente según la clase del objeto, demostrando polimorfismo.

###### Polimorfismo sin herencia (gracias al duck typing):
Python permite que objetos de clases no relacionadas respondan a los mismos métodos, siempre que los implementen:
```python
class Pato:
    def hablar(self):
        print("Cuac!")

class Persona:
    def hablar(self):
        print("Hola!")

for obj in [Pato(), Persona()]:
    obj.hablar()
```
Esto funciona aunque ```Pato``` y ```Persona``` no compartan una clase base común.

###### Polimorfismo en funciones y operadores:
* Funciones integradas: Por ejemplo, ```len()``` funciona con cadenas, listas, diccionarios, etc.
```python
print(len("hola"))          # 4
print(len([1, 2, 3]))       # 3
print(len({"a": 1, "b": 2}))# 2
```
* Sobrecarga de operadores: El operador + suma números o concatena cadenas.
```python
print(4 + 5)        # 9 (suma)
print("4" + "5")    # "45" (concatenación)
```
###### Polimorfismo con métodos definidos por el usuario:
Distintas clases pueden tener métodos con el mismo nombre que realizan tareas específicas para cada clase:
```python
from math import pi

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return pi * self.radio ** 2

formas = [Cuadrado(4), Circulo(7)]
for forma in formas:
    print(forma.area())
```

###### Polimorfismo y herencia: sobrescritura de métodos:
La clase hija puede modificar el comportamiento de un método heredado:
```python
class Figura:
    def area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def area(self):
        return self.largo * self.ancho

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2

figuras = [Rectangulo(10, 5), Triangulo(6, 8)]
for figura in figuras:
    print(figura.area())
```
###### Polimorfismo con métodos de clase en distintas clases:
Clases diferentes pueden implementar métodos con el mismo nombre para comportarse de forma específica:
```python
class Amazon:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def info(self):
        print(f"Producto Amazon: {self.nombre}, Precio: {self.precio}")

class Flipkart:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def info(self):
        print(f"Producto Flipkart: {self.nombre}, Precio: {self.precio}")

productos = [Amazon("iPhone", 1000), Flipkart("iPhone", 950)]
for producto in productos:
    producto.info()
```
###### Ventajas del polimorfismo
* Flexibilidad: Permite escribir código genérico que funciona con diferentes tipos de objetos.

* Reutilización: Facilita reutilizar funciones y métodos con distintos tipos de datos.

* Extensibilidad: Nuevas clases pueden integrarse sin modificar código existente.

* Claridad: Reduce la necesidad de estructuras condicionales complejas para manejar distintos tipos.

![alt text](image-1.png)

# ¿Qué es un método dunder?
Los métodos dunder son funciones predefinidas en Python que tienen un propósito especial. Estos métodos están rodeados por dos guiones bajos antes y después del nombre del método, de ahí el nombre «dunder». Los métodos dunder también se conocen como «métodos mágicos». Algunos ejemplos comunes incluyen ```__init__```, ```__str__```, ```__len__```, ```__add__```, entre otros.

Estos métodos permiten a los desarrolladores definir cómo los objetos de una clase deben comportarse en ciertas situaciones, como cuando se imprimen, se comparan, se agregan, etc.

#### Principales Métodos Dunder
* ```__init__```(self, ...)
Este es probablemente el método dunder más conocido. Es utilizado para inicializar una nueva instancia de una clase. Es el constructor de la clase en Python.
```Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Juan", 30)
```

* ```__str__```(self)
Este método define cómo se debe representar un objeto como una cadena de texto. Es el método al que se llama cuando se utiliza print() o str() en una instancia de la clase.
```Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

p = Persona("Juan", 30)
print(p)  # Output: Juan, 30 años
```

* ```__repr__```(self)
Este método define una representación oficial de la instancia de la clase. Es útil para depuración y desarrollo. Se llama cuando se usa repr() en una instancia.
```Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __repr__(self):
        return f"Persona({self.nombre}, {self.edad})"

p = Persona("Juan", 30)
print(repr(p))  # Output: Persona(Juan, 30)
```

* ```__len__```(self)
Este método permite definir la longitud de un objeto. Es útil para clases que contienen una colección de elementos.
```Python
class Grupo:
    def __init__(self, miembros):
        self.miembros = miembros
    
    def __len__(self):
        return len(self.miembros)

g = Grupo(["Juan", "Ana", "Luis"])
print(len(g))  # Output: 3
```

* ```__add__```(self, other)
Este método permite definir el comportamiento de la suma + entre dos objetos de la clase.
```Python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: (4, 6)
```

* ```__eq__```(self, other)
Este método permite definir el comportamiento de la comparación de igualdad == entre dos objetos de la clase.
```Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.edad == otro.edad

p1 = Persona("Juan", 30)
p2 = Persona("Juan", 30)
print(p1 == p2)  # Output: True
```

* ```__getitem__```(self, key)
El método __getitem__ permite que los objetos de una clase se comporten como colecciones (por ejemplo, listas o diccionarios). Esto permite acceder a los elementos utilizando la notación de corchetes.
```Python
class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __getitem__(self, indice):
        return self.elementos[indice]

lista = MiLista([1, 2, 3, 4])
print(lista[2])  # Output: 3
```

* ```__setitem__```(self, key, value)
El método __setitem__ se usa para asignar valores a los elementos de un objeto utilizando la notación de corchetes. Es útil para objetos que deben permitir la modificación de sus elementos.
```Python
class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __getitem__(self, indice):
        return self.elementos[indice]

    def __setitem__(self, indice, valor):
        self.elementos[indice] = valor

lista = MiLista([1, 2, 3, 4])
lista[2] = 10
print(lista[2])  # Output: 10
```

* ```__delitem__```(self, key)
El método delitem permite eliminar elementos de un objeto utilizando la notación de corchetes. Es apropiado para clases que necesitan permitir la eliminar de sus elementos.
```Python
class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __getitem__(self, indice):
        return self.elementos[indice]

    def __setitem__(self, indice, valor):
        self.elementos[indice] = valor

    def __delitem__(self, indice):
        del self.elementos[indice]

lista = MiLista([1, 2, 3, 4])
del lista[2]
print(lista.elementos)  # Output: [1, 2, 4]
```
#### Ventajas de los métodos dunder:
* Integración natural con las funciones y operadores de Python.

* Permiten sobrecargar operadores y personalizar el comportamiento de los objetos.

* Facilitan la legibilidad y mantenibilidad del código.

* Evitan conflictos de nombres con métodos normales, ya que su sintaxis es única.

#### Consideraciones y buenas prácticas:
* No se recomienda llamar a los métodos dunder directamente; deja que Python los invoque cuando corresponda.

* Úsalos solo cuando realmente necesites personalizar el comportamiento estándar de tus objetos.

* Consulta la documentación oficial del modelo de datos de Python para conocer todos los métodos dunder disponibles y su uso adecuado

# ¿Qué es un decorador de python?
Un decorador en Python es una función (o clase) que recibe otra función o método como argumento, le añade funcionalidades adicionales y retorna una nueva función con ese comportamiento extendido, sin modificar el código original de la función decorada. Los decoradores son una herramienta poderosa para la reutilización de código, la separación de responsabilidades y la mejora de la legibilidad.

En Python, la sintaxis para aplicar un decorador es mediante el símbolo ```@``` colocado justo encima de la función o método a decorar.

#### ¿Cómo funcionan los decoradores?
Un decorador es, esencialmente, un envoltorio (wrapper) que permite ejecutar código antes y/o después de la función original, o incluso modificar su resultado. El decorador recibe la función original como argumento, define una función interna (el wrapper) que añade la lógica extra, y luego retorna esa función interna.

```Python
def mi_decorador(funcion_original):
    def funcion_envolvente():
        print("Código antes de la función original")
        funcion_original()
        print("Código después de la función original")
    return funcion_envolvente

@mi_decorador
def saludar():
    print("¡Hola, mundo!")

saludar()
```
###### Salida:
```text
Código antes de la función original
¡Hola, mundo!
Código después de la función original
```
quí, ```@mi_decorador``` indica que la función ```saludar``` será pasada como argumento a ```mi_decorador```, y el resultado será la función decorada.

#### Ventajas de los decoradores:
* Reutilización de código: Permiten aplicar la misma lógica a múltiples funciones o métodos.

* Separación de responsabilidades: Separan la lógica principal de una función de funcionalidades accesorias, como logs, validaciones o manejo de errores.

* Legibilidad: Mejoran la claridad del código al evitar duplicaciones y centralizar comportamientos transversales.

* Encapsulamiento: Añaden funcionalidades sin modificar el código fuente original, facilitando el mantenimiento y la extensión del software.

#### Decoradores con argumentos:
Los decoradores pueden aceptar argumentos propios, lo que permite personalizar su comportamiento. Esto se logra añadiendo un nivel extra de funciones anidadas.

###### Ejemplo: Decorador con argumento:
```Python
def repetir(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador

@repetir(3)
def saludar():
    print("¡Hola!")

saludar()
```
###### Salida:
```text
¡Hola!
¡Hola!
¡Hola!
```
El decorador ```@repetir(3)``` hace que la función ```saludar``` se ejecute tres veces.

#### Decoradores aplicados a funciones con argumentos:

Un decorador puede aplicarse a funciones que reciben cualquier número de argumentos usando *args y **kwargs.
```python
def decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de la función")
        resultado = func(*args, **kwargs)
        print("Después de la función")
        return resultado
    return wrapper

@decorador
def suma(a, b):
    print("Entra en función suma")
    return a + b

suma(5, 8)
```
###### Salida:
```text
Antes de la función
Entra en función suma
Después de la función
```

#### Decoradores prácticos: Logger:
Uno de los usos más comunes de los decoradores es el registro de información (logging). Permiten registrar qué funciones han sido llamadas, con qué argumentos y qué resultados han producido.
```python
def log(fichero_log):
    def decorador_log(func):
        def decorador_funcion(*args, **kwargs):
            with open(fichero_log, 'a') as opened_file:
                output = func(*args, **kwargs)
                opened_file.write(f"{output}\n")
            return output
        return decorador_funcion
    return decorador_log

@log('ficherosalida.log')
def suma(a, b):
    return a + b

suma(10, 30)
```
Este decorador escribe en un archivo el resultado de cada función decorada, independientemente de la cantidad de argumentos.

#### Decoradores múltiples:
Es posible aplicar varios decoradores a una misma función. Se aplican en orden de arriba hacia abajo.
```python
def mayusculas(func):
    def wrapper():
        return func().upper()
    return wrapper

def invertir(func):
    def wrapper():
        return func()[::-1]
    return wrapper

@mayusculas
@invertir
def saludo():
    return "hola mundo"

print(saludo())  # Output: "ODNUM ALOH"
```
#### Usos comunes de los decoradores
Registro de logs (logger)

* Validación de parámetros

* Medición de tiempo de ejecución

* Control de acceso y autenticación

* Gestión de caché

* Depuración y pruebas

![alt text](image-2.png)