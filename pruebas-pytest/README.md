# Pruebas con Pytest

Mejore la experiencia de pruebas con Pytest, una excelente opción para escribir, ejecutar y ampliar pruebas en Python. Expóngase a patrones útiles y a los conceptos básicos de las pruebas con Pytest.

🔗 [Microsoft Learn](https://learn.microsoft.com/es-es/training/modules/test-python-with-pytest/)

### Objetivos de aprendizaje:

* Escribir pruebas mediante `pytest`, uno de los marcos de pruebas más populares para Python
* Acostumbrarse a los potentes informes en los errores de las pruebas.
* Usar funciones, clases y métodos para las pruebas

<hr/>

## Introducción

La introducción a las pruebas en Python puede ser abrumadora. La biblioteca estándar de Python ofrece utilidades y asistentes para escribir pruebas, pero con algunos inconvenientes que podrían hacerlo difícil.

Pytest es una de las herramientas y marcos de pruebas más populares para Python. Aunque Pytest puede ayudar con escenarios de pruebas muy complejos, no fuerza sus funcionalidades al crear pruebas. Puede escribir pruebas muy sencillas y seguir beneficiándose del ejecutor de pruebas rápido y con características y de informes útiles.

Un aspecto crucial de Pytest es que facilita mucho la escritura de pruebas. Puede escribir una función de prueba sin dependencias ni configuración y ejecutar la prueba inmediatamente.

En este módulo se tratarán algunos de los conceptos básicos necesarios para empezar a trabajar con Pytest y poder llevar el conjunto de pruebas al siguiente nivel.

<hr/>

## Conceptos básicos de Pytest

Comencemos a realizar pruebas con Pytest. Como hemos mencionado antes, Pytest es altamente configurable y puede controlar conjuntos de pruebas complejos. Pero no requiere muchos conocimientos para empezar a escribir pruebas. De hecho, cuanto más sencillo sea escribir pruebas en un marco, mejor.

Al final de esta sección, tendrá todo lo que necesita para empezar a escribir las primeras pruebas y ejecutarlas con Pytest.

### Convenciones

Antes de profundizar en la escritura de pruebas, debemos cubrir algunas de las convenciones de prueba en las que se basa Pytest.

No hay reglas difíciles sobre archivos de prueba, directorios de prueba o diseños de pruebas generales en Python. Al conocer estas reglas, puede aprovechar la detección y ejecución automáticas de pruebas sin necesidad de ninguna configuración adicional.

#### Archivos de prueba y directorio de pruebas

El directorio principal de las pruebas es el directorio tests. Puede colocar este directorio en el nivel raíz del proyecto, pero tampoco es inusual verlo junto con los módulos de código.

> ℹ️ **Nota** <br/>
> En este módulo, usaremos de forma predeterminada *tests* en la raíz de un proyecto.

Veamos cómo se ve la raíz de un pequeño proyecto de Python denominado *jformat*:

```text
.
├── README.md
├── jformat
│   ├── __init__.py
│   └── main.py
├── setup.py
└── tests
    └── test_main.py
```

El directorio *tests* se encuentra en la raíz del proyecto con un único archivo de prueba. En este caso, el archivo de prueba se denomina *test_main.py*. Estas son dos convenciones críticas:

* Uso de un directorio *tests* para colocar archivos de prueba y directorios de pruebas anidados
* Prefijo de archivos de prueba con *test*. El prefijo indica que el archivo contiene código de prueba.

> ❌ **Precaución** <br/>
> Evite usar `test` (forma singular) como nombre de directorio. El nombre `test` es un módulo de Python, por lo que la creación de un directorio con el mismo nombre lo invalidaría. Use siempre el plural *tests* en su lugar.

#### Funciones de prueba

Uno de los argumentos fuertes para usar Pytest es que permite escribir funciones de prueba. De forma similar a los archivos de prueba, la función debe tener el prefijo `test_`. Con el prefijo `test_`, se asegurará de que Pytest recopila la prueba y la ejecuta.

A continuación se muestra el aspecto de una función de prueba sencilla:

```Python
def test_main():
    assert "a string value" == "a string value"
```

#### Clases de prueba y métodos de prueba

De forma similar a las convenciones ya mencionadas, las clases de prueba y los métodos deben tener el prefijo `test`.

De la misma manera que otras convenciones de nomenclatura en Python para clases y métodos, se muestra cómo sería una clase de prueba pequeña que compruebe los nombres de usuario en una aplicación:

```Python
class TestUser:

    def test_username(self):
        assert default() == "default username"
```

Esta es una diferencia principal con la biblioteca `unittest` de Python: no es necesario realizar ninguna herencia. Estas son las convenciones adicionales:

* Las clases de prueba tienen el prefijo `Test`
* Los métodos de prueba tienen el prefijo `test_`

### Ejecutar pruebas

Pytest es a la vez un marco de pruebas y un ejecutor de pruebas. El ejecutor de pruebas es un ejecutable en la línea de comandos que, a nivel alto, puede:

* Realizar la recopilación de pruebas, buscar todos los archivos de prueba, las clases de prueba y las funciones de prueba para una ejecución de prueba
* Iniciar una ejecución de pruebas mediante la ejecución de todas las pruebas
* Realizar un seguimiento de los errores y superar pruebas
* Proporcionar informes completos al final de una ejecución de prueba

> ℹ️ **Nota** <br/>
> Dado que Pytest es una biblioteca externa, se *debe* instalar para poder usarse.

Dados estos contenidos en un archivo *test_main.py*, podemos ver cómo se comporta Pytest mediante la ejecución de las pruebas:

```Python
# contents of test_main.py file

def test_main():
    assert True
```

En la línea de comandos, en la misma ruta de acceso donde existe el archivo *test_main.py*, podemos ejecutar el ejecutable `pytest`:

```Bash
$ pytest
=========================== test session starts ============================
Python 3.10.9, pytest-7.3.1, pluggy-1.0.0
collected 1 item

tests\test_main.py .                                                  [100%]

============================ 1 passed in 0.00s =============================
```

En segundo plano, Pytest recopiló la prueba de ejemplo en el archivo de prueba sin necesidad de configuración.

#### Instrucción de aserción eficaz

Como es posible que ya haya observado, todos los ejemplos de prueba usan la llamada sin formato `assert`. Normalmente, en Python, la instrucción `assert` no se usa para las pruebas porque carece de informes adecuados cuando se produce un error en la aserción. Sin embargo, al usar Pytest, este no es el caso. En segundo plano, Pytest permite que la instrucción realice comparaciones enriquecidas sin forzar al usuario a escribir más código ni configurar nada.

Mediante la instrucción sin formato `assert`, puede usar los operadores de Python. Por ejemplo, `>`, `<`, `!=`, `>=` o `<=`. Todos los operadores de Python son válidos. Esta funcionalidad puede ser la característica más crucial de Pytest: no es necesario aprender una nueva sintaxis para escribir aserciones.

Veamos cómo se traduce al tratar con comparaciones comunes con objetos de Python. En este caso, vamos a pasar por el informe de errores al comparar cadenas muy largas:

```Bash
================================= FAILURES =================================
____________________________ test_long_strings _____________________________

    def test_long_strings():
        left = "this is a very long strings to be compared with another long string"
        right = "This is a very long string to be compared with another long string"
>       assert left == right
E       AssertionError: assert 'this is a ve...r long string' == 'This is a ve...r long string'
E         - This is a very long string to be compared with another long string
E         ? ^
E         + this is a very long strings to be compared with another long string
E         ? ^                         +

test_main.py:4: AssertionError
```

Pytest muestra contexto útil entorno al error. Un uso de mayúsculas y minúsculas incorrectos al principio de la cadena y un carácter adicional en una palabra. Pero más allá de las cadenas, Pytest puede ayudar con otros objetos y estructuras de datos. Así se comporta con las listas:

```Bash
________________________________ test_lists ________________________________

    def test_lists():
        left = ["sugar", "wheat", "coffee", "salt", "water", "milk"]
        right = ["sugar", "coffee", "wheat", "salt", "water", "milk"]
>       assert left == right
E       AssertionError: assert ['sugar', 'wh...ater', 'milk'] == ['sugar', 'co...ater', 'milk']
E         At index 1 diff: 'wheat' != 'coffee'
E         Full diff:
E         - ['sugar', 'coffee', 'wheat', 'salt', 'water', 'milk']
E         ?                     ---------
E         + ['sugar', 'wheat', 'coffee', 'salt', 'water', 'milk']
E         ?           +++++++++

test_main.py:9: AssertionError
```

Este informe identifica que el índice 1 (segundo elemento de la lista) es diferente. No solo identifica el número de índice, sino que también proporciona una representación del error. Aparte de las comparaciones de elementos, también puede notificar si faltan elementos y proporcionar información que puede indicar exactamente qué elemento podría ser. En el siguiente caso, es `"milk"`:

```Bash
________________________________ test_lists ________________________________

    def test_lists():
        left = ["sugar", "wheat", "coffee", "salt", "water", "milk"]
        right = ["sugar", "wheat", "salt", "water", "milk"]
>       assert left == right
E       AssertionError: assert ['sugar', 'wh...ater', 'milk'] == ['sugar', 'wh...ater', 'milk']
E         At index 2 diff: 'coffee' != 'salt'
E         Left contains one more item: 'milk'
E         Full diff:
E         - ['sugar', 'wheat', 'salt', 'water', 'milk']
E         + ['sugar', 'wheat', 'coffee', 'salt', 'water', 'milk']
E         ?                    ++++++++++

test_main.py:9: AssertionError
```

Por último, veamos cómo se comporta con los diccionarios. Comparar dos diccionarios grandes puede ser abrumador si hay errores, pero Pytest realiza un trabajo sobresaliente al proporcionar contexto e identificar el error:

```Bash
____________________________ test_dictionaries _____________________________

    def test_dictionaries():
        left = {"street": "Ferry Ln.", "number": 39, "state": "Nevada", "zipcode": 30877, "county": "Frett"}
        right = {"street": "Ferry Lane", "number": 38, "state": "Nevada", "zipcode": 30877, "county": "Frett"}
>       assert left == right
E       AssertionError: assert {'county': 'F...rry Ln.', ...} == {'county': 'F...ry Lane', ...}
E         Omitting 3 identical items, use -vv to show
E         Differing items:
E         {'street': 'Ferry Ln.'} != {'street': 'Ferry Lane'}
E         {'number': 39} != {'number': 38}
E         Full diff:
E           {
E            'county': 'Frett',...
E
E         ...Full output truncated (12 lines hidden), use '-vv' to show
```

En esta prueba, hay dos errores en el diccionario. Uno es que el valor `"street"` es diferente y el otro es que `"number"` no coincide.

Pytest detecta con precisión estas diferencias (aunque se trata de un error en una sola prueba). Dado que los diccionarios contienen muchos elementos, Pytest omite las partes idénticas y solo muestra contenido relevante. Veamos lo que sucede si hacemos uso de la marca `-vv` sugerida para aumentar el nivel de detalle en el resultado:

```Bash
____________________________ test_dictionaries _____________________________

    def test_dictionaries():
        left = {"street": "Ferry Ln.", "number": 39, "state": "Nevada", "zipcode": 30877, "county": "Frett"}
        right = {"street": "Ferry Lane", "number": 38, "state": "Nevada", "zipcode": 30877, "county": "Frett"}
>       assert left == right
E       AssertionError: assert {'county': 'Frett',\n 'number': 39,\n 'state': 'Nevada',\n 'street': 'Ferry Ln.',\n 'zipcode': 30877} == {'county': 'Frett',\n 'number': 38,\n 'state': 'Nevada',\n 'street': 'Ferry Lane',\n 'zipcode': 30877}
E         Common items:
E         {'county': 'Frett', 'state': 'Nevada', 'zipcode': 30877}
E         Differing items:
E         {'number': 39} != {'number': 38}
E         {'street': 'Ferry Ln.'} != {'street': 'Ferry Lane'}
E         Full diff:
E           {
E            'county': 'Frett',
E         -  'number': 38,
E         ?             ^
E         +  'number': 39,
E         ?             ^
E            'state': 'Nevada',
E         -  'street': 'Ferry Lane',
E         ?                    - ^
E         +  'street': 'Ferry Ln.',
E         ?                     ^
E            'zipcode': 30877,
E           }
```

Al ejecutar `pytest -vv`, el informe aumenta la cantidad de detalles y proporciona una comparación pormenorizada. No solo este informe detecta y muestra el error, sino que le permite realizar rápidamente cambios para corregir el problema.

<hr/>

## Clases y métodos de prueba

Además de escribir funciones de prueba, Pytest permite el uso de clases. Como ya hemos mencionado, no es necesaria la herencia y las clases de prueba siguen algunas reglas sencillas. El uso de clases proporciona más flexibilidad y reutilización. Como verá a continuación, Pytest se mantiene fuera del camino y evita forzarle a escribir pruebas de una manera determinada.

Al igual que las funciones, todavía puede escribir aserciones mediante la instrucción `assert`.

### Compilación de una clase de prueba

Vamos a usar un escenario real para ver cómo pueden ayudar las clases de prueba. La siguiente función comprueba si un archivo determinado tiene un contenido de "yes" para devolver `True`. Si el archivo no existe o si contiene un "no", devuelve `False`. Este escenario es común en las tareas asincrónicas que usan el sistema de archivos para indicar la finalización.

Este es el aspecto de la función:

```Python
import os

def is_done(path):
    if not os.path.exists(path):
        return False
    with open(path) as _f:
        contents = _f.read()
    if "yes" in contents.lower():
        return True
    elif "no" in contents.lower():
        return False
```

Este es el aspecto de una clase con dos pruebas (una para cada condición) en un archivo denominado *test_files.py*:

```Python
class TestIsDone:

    def test_yes(self):
        with open("/tmp/test_file", "w") as _f:
            _f.write("yes")
        assert is_done("/tmp/test_file") is True

    def test_no(self):
        with open("/tmp/test_file", "w") as _f:
            _f.write("no")
        assert is_done("/tmp/test_file") is False
```

> ❌ **Precaución** <br/>
> Los métodos de prueba usan la ruta de acceso */tmp* para un archivo de prueba temporal porque es más fácil de usar para el ejemplo. Sin embargo, si necesita usar archivos temporales, considere la posibilidad de usar una biblioteca como `tempfile` que pueda crearlos (y quitarlos) de forma segura. No todos los sistemas tienen un directorio */tmp* y esa ubicación podría no ser temporal en función del sistema operativo.

La ejecución de las pruebas con la marca `-v` para aumentar el nivel de detalle muestra las pruebas superadas:

```Bash
pytest -v test_files.py
============================= test session starts ==============================
Python 3.10.9, pytest-7.3.1, pluggy-1.0.0
rootdir: /private
cachedir: .pytest_cache
collected 2 items

test_files.py::TestIsDone::test_yes PASSED                               [ 50%]
test_files.py::TestIsDone::test_no PASSED                                [100%]

============================== 2 passed in 0.00s ===============================
```

Aunque se superan las pruebas, parecen algo repetitivas y también dejan archivos una vez finalizada la prueba. Antes de ver cómo podemos mejorar esto, vamos a tratar los métodos auxiliares en la sección siguiente.

### Métodos auxiliares

En una clase de prueba, hay algunos métodos que puede usar para configurar y anular la ejecución de pruebas. Pytest los ejecutará automáticamente si así se define. Para usar estos métodos, debe saber que tienen un orden y un comportamiento específicos.

* `setup`: se ejecuta una vez antes de cada prueba en una clase.
* `teardown`: se ejecuta una vez después de cada prueba en una clase.
* `setup_class`: se ejecuta una vez antes de todas las pruebas en una clase.
* `teardown_class`: se ejecuta una vez después de todas las pruebas en una clase.

Le resultará útil escribir métodos de configuración cuando las pruebas requieran recursos similares (o idénticos) para funcionar. Lo ideal es que una prueba no deje recursos cuando se complete, por lo que los métodos de anulación pueden ayudar en la limpieza de pruebas en esas situaciones.

#### Limpieza

Vamos a comprobar una clase de prueba actualizada que limpia los archivos después de cada prueba:

```Python
class TestIsDone:

    def teardown(self):
        if os.path.exists("/tmp/test_file"):
            os.remove("/tmp/test_file")

    def test_yes(self):
        with open("/tmp/test_file", "w") as _f:
            _f.write("yes")
        assert is_done("/tmp/test_file") is True

    def test_no(self):
        with open("/tmp/test_file", "w") as _f:
            _f.write("no")
        assert is_done("/tmp/test_file") is False
```

Con el método `teardown()`, esta clase de prueba ya no dejará atrás un archivo */tmp/test_file*.

#### Configurar

Otra mejora que podemos hacer en esta clase es agregar una variable que apunte al archivo. Puesto que el archivo se declara ahora en seis lugares, cualquier cambio en la ruta de acceso significaría cambiarlo en todos esos puntos. Este es el aspecto de la clase con un método `setup()` agregado que declara la variable de ruta de acceso:

```Python
class TestIsDone:

    def setup(self):
        self.tmp_file = "/tmp/test_file"

    def teardown(self):
        if os.path.exists(self.tmp_file):
            os.remove(self.tmp_file)

    def test_yes(self):
        with open(self.tmp_file, "w") as _f:
            _f.write("yes")
        assert is_done(self.tmp_file) is True

    def test_no(self):
        with open(self.tmp_file, "w") as _f:
            _f.write("no")
        assert is_done(self.tmp_file) is False
```

#### Métodos del asistente personalizados

Puede crear métodos del asistente personalizados en una clase. Estos métodos no deben tener el prefijo con el nombre `test` y no se pueden denominar como los métodos de configuración o limpieza. En la clase `TestIsDone`, podríamos automatizar la creación del archivo temporal en un asistente personalizado. Este es el aspecto que podría tener el método auxiliar:

```Python
def write_tmp_file(self, content):
        with open(self.tmp_file, "w") as _f:
            _f.write(content)
```

Pytest no ejecutará automáticamente el método `write_tmp_file()` y otros métodos pueden llamarlo directamente para ahorrarse la realización de tareas repetitivas como escribir en un archivo.

Este es el aspecto de toda la clase después de actualizar los métodos de prueba para usar el asistente personalizado:

```Python
class TestIsDone:

    def setup(self):
        self.tmp_file = "/tmp/test_file"

    def teardown(self):
        if os.path.exists(self.tmp_file):
            os.remove(self.tmp_file)

    def write_tmp_file(self, content):
        with open(self.tmp_file, "w") as _f:
            _f.write(content)

    def test_yes(self):
        self.write_tmp_file("yes")
        assert is_done(self.tmp_file) is True

    def test_no(self):
        self.write_tmp_file("no")
        assert is_done(self.tmp_file) is False
```

### Cuándo usar una clase en lugar de una función

No hay reglas estrictas en cuanto a cuándo usar una clase en lugar de una función. Siempre es buena idea seguir las convenciones de los proyectos y equipos actuales con los que trabaja, pero estas son algunas ideas generales que puede usar para determinar cuándo usar una clase.

* Cuando las pruebas necesitan una configuración o limpieza similares
* Cuando tiene sentido agruparlos
* Si hay al menos varias pruebas
* Cuando las pruebas pueden beneficiarse de un conjunto común de asistentes

<hr/>

## Ejercicio

En este ejercicio, usará Pytest para probar una función. A continuación, encontrará y corregirá algunos posibles problemas con la función que provocan que las pruebas tengan errores. Examinar los errores y usar los informes de errores enriquecidos de Pytest es esencial para identificar y corregir errores o pruebas problemáticas en el código de producción.

En este ejercicio, usaremos una función denominada `admin_command()` que acepta un comando del sistema como entrada y, opcionalmente, le agrega un prefijo con la herramienta `sudo`. La función tiene un error, que detectará escribiendo pruebas.

### Paso 1: Adición de un archivo con pruebas para este ejercicio

1. Cree un nuevo archivo de prueba usando las convenciones de nombre de archivo de Python para los archivos de prueba. Dele el nombre *test_exercise.py* al archivo de prueba y agregue el siguiente código:

```Python
def admin_command(command, sudo=True):
    """
    Prefix a command with `sudo` unless it is explicitly not needed. Expects `command` to be a list.
    """
    if sudo:
        ["sudo"] + command
    return command
```

La función `admin_command()` toma una lista como entrada mediante el argumento `command` y, opcionalmente, puede agregar un prefijo a la lista con `sudo`. Si el argumento de palabra clave `sudo` se establece en `False`, devuelve el mismo comando especificado como entrada.

2. En el mismo archivo, anexe las pruebas para la función `admin_command()`. Las pruebas usan un método auxiliar que devuelve un comando de ejemplo:

```Python
class TestAdminCommand:

def command(self):
    return ["ps", "aux"]

def test_no_sudo(self):
    result = admin_command(self.command(), sudo=False)
    assert result == self.command()

def test_sudo(self):
    result = admin_command(self.command(), sudo=True)
    expected = ["sudo"] + self.command()
    assert result == expected
```
 
> ℹ️ **Nota** <br/>
> No es habitual tener pruebas dentro del mismo archivo como código real. Por motivos de simplicidad, los ejemplos de este ejercicio tendrán código real en el mismo archivo. En los proyectos de Python reales, descubrirá que las pruebas están separadas por archivos y directorios del código que está probando.

### Paso 2: Ejecución de las pruebas e identificación del error

Ahora que el archivo de prueba tiene una función para probarla y un par de pruebas para comprobar su comportamiento, es el momento de ejecutar las pruebas y trabajar con errores.

* Ejecute el archivo con Python:

```Bash
$ pytest test_exercise.py
```

La ejecución debe completarse con la superación de una prueba y un error, y la salida del error debe ser similar a la siguiente:

```Bash
=================================== FAILURES ===================================
__________________________ TestAdminCommand.test_sudo __________________________

self = <test_exercise.TestAdminCommand object at 0x10634c2e0>

    def test_sudo(self):
        result = admin_command(self.command(), sudo=True)
        expected = ["sudo"] + self.command()
>       assert result == expected
E       AssertionError: assert ['ps', 'aux'] == ['sudo', 'ps', 'aux']
E         At index 0 diff: 'ps' != 'sudo'
E         Right contains one more item: 'aux'
E         Use -v to get the full diff

test_exercise.py:24: AssertionError
=========================== short test summary info ============================
FAILED test_exercise.py::TestAdminCommand::test_sudo - AssertionError: assert...
========================= 1 failed, 1 passed in 0.04s ==========================
```

El resultado produce un error en la prueba `test_sudo()`. Pytest proporciona detalles sobre las dos listas que se comparan. En este caso, la variable `result` no contiene el comando `sudo`, que es lo que espera la prueba.

### Paso 3: Corrección del error y superación de las pruebas

Antes de realizar cambios, debe comprender por qué hay un error en primer lugar. Aunque sabemos que no se cumple la expectativa (`sudo` no está en el resultado), debe averiguar por qué.

Examine las siguientes líneas de código de la función `admin_command()` cuando se cumpla la condición `sudo=True`:

```Python
if sudo:
    ["sudo"] + command
```

La operación de las listas no se usa para devolver el valor. Puesto que no se devuelve, la función termina devolviendo siempre el comando sin `sudo`.

1. Actualice la función `admin_command()` para que devuelva la operación de lista de modo que se use el resultado modificado al solicitar un comando `sudo`. La función actualizada debe tener este aspecto:

```Python
def admin_command(command, sudo=True):
    """
    Prefix a command with `sudo` unless it is explicitly not needed. Expects `command` to be a list.
    """
    if sudo:
        return ["sudo"] + command
    return command
```

2. Vuelva a ejecutar la prueba con Pytest. Intente aumentar el nivel de detalle de la salida mediante la marca `-v` con Pytest:

```Bash
$ pytest -v test_exercise.py
```

3. Compruebe la salida. Ahora debería mostrar que se superan dos pruebas:

```Bash
============================= test session starts ==============================
Python 3.10.9, pytest-7.3.1, pluggy-1.0.0
rootdir: /private
collected 2 items

test_exercise.py::TestAdminCommand::test_no_sudo PASSED                  [ 50%]
test_exercise.py::TestAdminCommand::test_sudo PASSED                     [100%]

============================== 2 passed in 0.00s ===============================
```

> ℹ️ **Nota** <br/>
> Puesto que la función admite más valores con diferentes usos de mayúsculas y minúsculas, se deben agregar más pruebas para cubrir esas variantes. Esto impediría que, en el futuro, los cambios que se realicen en la función den lugar a un comportamiento diferente (inesperado).

### Paso 4: Adición de código nuevo con pruebas

Ahora que ha agregado pruebas, debe sentirse cómodo teniendo más cambios en la función y comprobarlos con pruebas. Incluso si los cambios no están cubiertos por las pruebas existentes, puede sentirse seguro de que no está rompiendo ninguna suposición anterior.

En este caso, la función `admin_command()` confía ciegamente en que el argumento `command` siempre es una lista. Vamos a mejorarlo asegurándose de que se genera una excepción con un mensaje de error útil.

1. En primer lugar, cree una prueba que capture el comportamiento. Aunque la función aún no se ha actualizado, primero probará un enfoque de prueba (también conocido como Desarrollo controlado por pruebas o TDD).

    - Actualice el archivo test_exercise.py para que importe pytest en la parte superior. Esta prueba usará un asistente interno del marco de trabajo pytest:

    ```Python
    import pytest
    ```

    - Ahora, anexe una nueva prueba a la clase para comprobar la excepción. Esta prueba debe esperar una `TypeError` de la función cuando se pasa un valor que no es de lista a la función:

    ```Python
    def test_non_list_commands(self):
        with pytest.raises(TypeError):
            admin_command("some command", sudo=True)
    ```

2. Vuelva a ejecutar las pruebas con Pytest. Todas se deben superar:

```Bash
============================= test session starts ==============================
Python 3.10.9, pytest-7.3.1, pluggy-1.0.0
rootdir: /private
collected 3 items

test_exercise.py ...                                                     [100%]

============================== 3 passed in 0.00s ===============================
```

La prueba es lo suficientemente buena para comprobar `TypeError`, pero sería bueno agregar el código con un mensaje de error útil.

3. Actualice la función para generar explícitamente un `TypeError` con un mensaje de error útil:

```Python
def admin_command(command, sudo=True):
    """
    Prefix a command with `sudo` unless it is explicitly not needed. Expects `command` to be a list.
    """
    if not isinstance(command, list):
        raise TypeError(f"was expecting command to be a list, but got a {type(command)}")
    if sudo:
        return ["sudo"] + command
    return command
```

4. Por último, actualice el método `test_non_list_commands()` para comprobar el mensaje de error:

```Python
def test_non_list_commands(self):
    with pytest.raises(TypeError) as error:
        admin_command("some command", sudo=True)
    assert error.value.args[0] == "was expecting command to be a list, but got a <class 'str'>"
```

La prueba actualizada usa `error` como una variable que contiene toda la información de excepción. Con `error.value.args`, puede examinar los argumentos de la excepción. En este caso, el primer argumento tiene la cadena de error que la prueba puede comprobar.

### Comprobar el trabajo

Llegado a este punto, debe tener un archivo de prueba de Python con un nombre similar a test_exercise.py y los siguientes elementos:

* Una función `admin_command()` que acepta un argumento y un argumento de palabra clave.
* Una excepción `TypeError` con un mensaje de error útil en la función `admin_command()`.
* Una clase de prueba `TestAdminCommand()` que tiene un método auxiliar `command()` y tres métodos de prueba que comprueban la función `admin_command()`.

Todas las pruebas deben superarse al ejecutarlas en el terminal, sin errores.