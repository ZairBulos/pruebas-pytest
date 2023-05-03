# Pruebas avanzadas con Pytest

Cree accesorios Pytest personalizados para código reutilizable y mejore las pruebas de entrada múltiple con parametrize.

🔗 [Microsoft Learn](https://learn.microsoft.com/es-es/training/modules/python-advanced-pytest/)

### Objetivos de aprendizaje:

* Usar el marco `pytest` y sus asistentes de biblioteca para resolver problemas comunes de pruebas
* Trabajar con *parametrize* para crear pruebas a partir de varios valores de entrada
* Crear accesorios, lo que le permite ampliar y compartir la funcionalidad de pruebas

<hr/>

## Introducción

Todavía queda mucho que aprender con Pytest más allá de los conceptos básicos de la ejecución de pruebas y la creación de informes avanzados. Aunque el uso de Pytest como biblioteca no es un requisito para ejecutar o escribir pruebas, es útil comprender sus funcionalidades. Estas funcionalidades de Pytest le permiten escribir mejores pruebas y aumentar la cobertura y ser eficaz en la resolución de errores.

En este módulo, repasará algunas de las características más esenciales del marco Pytest para que pueda escribir pruebas eficaces, a la vez que las mantiene sencillas y legibles.

<hr/>

## Conceptos básicos de Pytest

La característica *parametrize* de Pytest puede parecer intimidante al principio. Se vuelve inmediatamente clara una vez que se comprende el problema que resuelve. En la mayoría de los casos, la característica parametrize permite proporcionar fácilmente diferentes entradas a una prueba que realiza la misma aserción.

### Cuándo se debe usar

Hay dos escenarios comunes que presentan una razón perfecta para usar parametrize. En ambos casos, debe tener en cuenta los inconvenientes. Debe intentar evitar estos inconvenientes y, afortunadamente, Pytest ofrece una mejor manera de resolverlos. Veamos cada uno de estos casos en detalle.

#### Bucles for

Si alguna vez ha visto una prueba que usa un bucle for para realizar aserciones basadas en diferentes entradas, es un escenario perfecto para usar parametrize. Este es el aspecto de una función de prueba con un bucle for:

```Python
def test_string_is_digit():
    items = ["1", "10", "33"]
    for item in items:
        assert item.isdigit()
```

Esta prueba es problemática porque si se produce un error en uno de los elementos, se encuentra con estos problemas:

* El informe de prueba no puede saber si solo se produce un error en un elemento o hay otros elementos que deberían producir un error.
* Todas las combinaciones se ven como una sola prueba.
* Si corrige un error, no puede saber si ha corregido todos los errores, lo que le obliga a volver a ejecutar la prueba.

Vamos a modificar la prueba para que tenga dos elementos que deben producir un error:

```Python
def test_string_is_digit():
    items = ["No", "1", "10", "33", "Yes"]
    for item in items:
        assert item.isdigit()
```

La ejecución de la prueba muestra solo un error aunque haya dos elementos no válidos en esa lista:

```Bash
=================================== FAILURES ===================================
_____________________________ test_string_is_digit _____________________________
test_items.py:4: in test_string_is_digit
    assert item.isdigit()
E   AssertionError: assert False
E    +  where False = <built-in method isdigit of str object at 0x103fa1df0>()
E    +    where <built-in method isdigit of str object at 0x103fa1df0> = 'No'.isdigit
=========================== short test summary info ============================
FAILED test_items.py::test_string_is_digit - AssertionError: assert False
============================== 1 failed in 0.01s ===============================
```

Este es un caso de uso perfecto para *parametrize*. Antes de ver cómo actualizar la prueba, vamos a explorar otra situación común que no implica bucles for.

#### Pruebas que declaran el mismo comportamiento

Un grupo de pruebas que realizan la misma aserción también son un buen candidato para *parametrize*. Si la prueba anterior se reescribe con una prueba para cada elemento, permitirá un mejor informe de errores, pero sería repetitivo:

```Python
def test_is_digit_1():
    assert "1".isdigit()

def test_is_digit_10():
    assert "10".isdigit()

def test_is_digit_33():
    assert "33".isdigit()
```

Estas pruebas son mejores en el sentido de que un error se puede asociar fácilmente con una sola entrada, y aunque puede parecer extraño tener varias pruebas similares, es habitual de ver en conjuntos de pruebas de producción que intentan ser granulares.

Aunque las pruebas serían mejores porque pueden notificar exactamente lo que falla (o lo que funciona), también tienen los siguientes problemas:

* El código es muy repetitivo, lo que crea una carga de mantenimiento innecesaria.
* Es posible que se produzcan fallos y errores tipográficos cuando se deban realizar actualizaciones en todas las pruebas.
* Dado que son repetitivas, es posible que los ingenieros eviten todos los casos de uso y las entradas.

### Uso de parametrize

Ahora que conoce algunos de los casos de uso de *parametrize*, vamos a actualizar la prueba que usa un bucle for que incluye elementos con errores, que actualmente tiene el siguiente aspecto:

```Python
def test_string_is_digit():
    items = ["No", "1", "10", "33", "Yes"]
    for item in items:
        assert item.isdigit()
```

Para usar parametrize, debe importar `pytest` como una biblioteca y, a continuación, usarla como decorador en la función. La prueba actualizada debería tener el aspecto siguiente:

```Python
import pytest

@pytest.mark.parametrize("item", ["No", "1", "10", "33", "Yes"])
def test_string_is_digit(item):
    assert item.isdigit()
```

Antes de ejecutar las pruebas, vamos a repasar los cambios. El decorador `pytest.mark.parametrize()` define dos argumentos. El primer argumento es una cadena denominada `"item"`. Esa cadena se usa como *argumento con nombre* para la función de prueba que se ve en la siguiente línea de la definición de la función de prueba. El otro argumento es la lista de elementos.

#### Informes de error enriquecidos

En segundo plano, Pytest considerará cada elemento de esa lista *como una prueba independiente*. Esto significa que todas las pruebas superadas y con errores se notificarán por separado. Veamos lo que sucede al ejecutar la prueba con `pytest`:
 
```Bash
$ pytest
============================= test session starts ==============================
Python 3.10.9, pytest-7.3.1, pluggy-1.0.0
rootdir: /private
collected 5 items

test_items.py F...F                                                      [100%]

=================================== FAILURES ===================================
___________________________ test_string_is_digit[No] ___________________________
test_items.py:5: in test_string_is_digit
    assert item.isdigit()
E   AssertionError: assert False
E    +  where False = <built-in method isdigit of str object at 0x102d45e30>()
E    +    where <built-in method isdigit of str object at 0x102d45e30> = 'No'.isdigit
__________________________ test_string_is_digit[Yes] ___________________________
test_items.py:5: in test_string_is_digit
    assert item.isdigit()
E   AssertionError: assert False
E    +  where False = <built-in method isdigit of str object at 0x102d45df0>()
E    +    where <built-in method isdigit of str object at 0x102d45df0> = 'Yes'.isdigit
=========================== short test summary info ============================
FAILED test_items.py::test_string_is_digit[No] - AssertionError: assert False
FAILED test_items.py::test_string_is_digit[Yes] - AssertionError: assert False
========================= 2 failed, 3 passed in 0.07s ==========================
```

Hay algunos elementos importantes en los informes de pruebas. En primer lugar, vemos que, a partir de una sola prueba, Pytest notifica cinco pruebas en total: tres superadas y dos con errores. Los errores se notifican por separado, incluida cuál es la entrada con errores. Por ejemplo, la cadena `"No"` se notifica en tres lugares: una en el título de la sección del error, el error de aserción y, por último, en la línea de error hacia el final:

```Bash
___________________________ test_string_is_digit[No] ___________________________
[...]
E    +    where <built-in method isdigit of str object at 0x102d45e30> = 'No'.isdigit
[...]
FAILED test_items.py::test_string_is_digit[No] - AssertionError: assert False
```

Es difícil no identificar el valor que provocó el error, ya que se notifica en muchos lugares.

#### Informes de superación útiles

Al ejecutar las pruebas en la línea de comandos, el número de informes de pruebas que se producen cuando se superan las pruebas es mínimo. Este es el aspecto que tendría la prueba después de una actualización para corregir los errores:

```Python
@pytest.mark.parametrize("item", ["0", "1", "10", "33", "9"])
def test_string_is_digit(item):
    assert item.isdigit()
```

La ejecución de las pruebas genera una respuesta mínima:

```Bash
$ pytest 
============================= test session starts ==============================
Python 3.10.9, pytest-7.3.1, pluggy-1.0.0
rootdir: /private
collected 5 items

test_items.py .....                                                      [100%]

============================== 5 passed in 0.01s ===============================
```

Sin embargo, aumentar el nivel de detalle puede incluir los valores que Pytest ve para cada prueba al parametrizar:

```Bash
pytest -v test_items.py
============================= test session starts ==============================
Python 3.10.9, pytest-7.3.1, pluggy-1.0.0
rootdir: /private
collected 5 items

test_items.py::test_string_is_digit[0] PASSED                            [ 20%]
test_items.py::test_string_is_digit[1] PASSED                            [ 40%]
test_items.py::test_string_is_digit[10] PASSED                           [ 60%]
test_items.py::test_string_is_digit[33] PASSED                           [ 80%]
test_items.py::test_string_is_digit[9] PASSED                            [100%]

============================== 5 passed in 0.01s ===============================
```

### Uso de varios argumentos

Hasta ahora ha visto el uso de un solo argumento y varios elementos para parametrize. Sin embargo, es posible usar varios argumentos.

> 💡 **Sugerencia**
> Aunque es posible usar varios argumentos, intente no usar esta característica en exceso, ya que puede hacer que las pruebas sean más difíciles de leer.

Pongamos que hay una prueba que quiere comprobar si un objeto tiene un atributo. Para esta prueba, usaremos la función integrada `hasattr()` de Python. Devuelve un valor booleano en función del atributo del objeto. A continuación se muestra un ejemplo rápido de cómo funciona:

```Python
>>> hasattr(dict(), "keys")
True
>>> hasattr("string", "append")
False
```

Puesto que `hasattr()` requiere dos argumentos, podemos usar parametrize de la siguiente manera:

```Python
@pytest.mark.parametrize("item, attribute", [("", "format"), (list(), "append")])
def test_attributes(item, attribute):
    assert hasattr(item, attribute)
```

El decorador *parametrize* sigue usando una sola cadena para el primer argumento, pero con dos palabras. Estas dos palabras dentro de la cadena ahora están separadas por una coma. Cada palabra separada por comas se convierte en un argumento para la función. En este caso, son `item` y `attribute`.

A continuación, la lista de elementos que se debe superar es una lista de dos elementos. Cada uno de estos pares representa un `item` y un `attribute` para los que se va a realizar una prueba.

Cuando Pytest no puede crear una representación de cadena de los objetos que se pasan, crea una. Puede verla en acción al ejecutar la prueba:

```Bash
$ pytest -v
============================= test session starts ==============================
Python 3.10.9, pytest-7.3.1, pluggy-1.0.0
rootdir: /private
collected 2 items

test_items.py::test_attributes[-format] PASSED                           [ 50%]
test_items.py::test_attributes[item1-append] PASSED                      [100%]

============================== 2 passed in 0.01s ===============================
```

<hr/>

## Accesorios de Pytest

En Pytest, los accesorios son asistentes para pruebas. En su forma más sencilla, esto significa que no son muy diferentes de una función o un método auxiliar. Los accesorios, como la mayoría de las características de Pytest, son fáciles de empezar a utilizar, pero lo suficientemente potentes como para adaptarse a escenarios muy complejos.

A diferencia de las funciones auxiliares sin formato, los accesorios pueden tener su propia configuración y anular el código, lo que garantiza que estos asistentes se puedan reutilizar de forma segura en un conjunto de pruebas.

La siguiente lista puede ayudarle a pensar en accesorios como algo que va más allá de los asistentes de prueba. Se pueden usar para lo siguiente:

* Proporcionar datos listos para usar, como un archivo o una cadena JSON compleja
* Iniciar, detener o interactuar con servicios externos como una base de datos
* Crear objetos que ofrecen un comportamiento específico para las pruebas

Por último, los accesorios se pueden tratar como complementos para Pytest. Cuando los accesorios se definen en archivos específicos, Pytest garantiza que estén disponibles para cualquier prueba que los requiera sin importarlos explícitamente.

### Creación de un accesorio

Un escenario común para las pruebas es tratar con archivos. Vamos a crear un accesorio que cree un archivo temporal. Esto implica el uso de un directorio temporal y la devolución de la ruta de acceso de una prueba que se va a consumir.

Así es como se ve el accesorio en un archivo de prueba:

```Python
import pytest
import tempfile

@pytest.fixture
def tmp_file():
    def create():
        temp = tempfile.NamedTemporaryFile(delete=False)
        return temp.name
    return create
```

La función `tmp_file()` es el propio accesorio. El nombre es importante porque así es como lo necesitará más adelante en las pruebas. La función tiene una función anidada. Es necesaria porque se *llama* al accesorio cuando se usa, lo que hace que esté ansioso. En este caso, es necesario controlar la creación del archivo. El anidamiento con otra función permite retrasar la creación de un archivo.

Dentro de la función anidada `create()`, se crea un archivo temporal y, a continuación, se devuelve la ruta de acceso absoluta a él. Así es como una prueba puede usar ese accesorio:

```Python
import os

def test_file(tmp_file):
    path = tmp_file()
    assert os.path.exists(path)
```

Una prueba puede requerir un accesorio especificando el *nombre del accesorio* como argumento. Ahora cualquier prueba que necesite el accesorio recién escrito puede requerirlo y usarlo. Aunque el caso de uso es demasiado sencillo, puede expandir el accesorio para escribir contenido opcionalmente o realizar modificaciones en el archivo, como permisos o propiedad, por ejemplo.

#### Trabajo con ámbitos

Si ha trabajado con métodos de prueba, es posible que haya usado un método `setup()` o `teardown()` para configurar o limpiar una prueba. Los accesorios tienen un ámbito de "función" de forma predeterminada. Esto implica dos cosas:

* El valor devuelto se calcula para cada prueba que lo usa.
* Si hay una limpieza necesaria para la función, se realiza después de cada prueba que la usa.

Los accesorios pueden definir otros ámbitos. Por ejemplo, si necesita un accesorio que inicie una base de datos, puede que quiera que se ejecute una vez al principio de la sesión de prueba y no con cada prueba. Hay cuatro ámbitos admitidos para los accesorios:

* `function`: se ejecuta una vez por prueba
* `class`: se ejecuta una vez por clase
* `module`: se ejecuta una vez para un módulo
* `session`: se ejecuta una vez para una sesión de prueba

En este caso, *se ejecuta una vez* significa que el valor devuelto se almacena en caché. Por lo tanto, un accesorio que tiene un ámbito de "módulo" puede llamarse varias veces en un módulo de prueba, pero el valor devuelto será el de la primera prueba que lo llamó. Esta característica permite ahorrar tiempo y crear un conjunto de pruebas altamente eficiente sin esfuerzo adicional.

Este es el aspecto que tendría el accesorio `tmp_file()` con un ámbito de módulo:

```Python
@pytest.fixture(scope="module")
def tmp_file():
    def create(contents):
        temp = tempfile.NamedTemporaryFile(delete=False)
        return temp.name
    return create
```

#### Limpieza

Hasta ahora, el accesorio que ha visto crea un archivo y luego lo deja por ahí. Puede registrar una función de limpieza mediante un accesorio interno especial denominado `request`. Esto significa que un accesorio también puede requerir otros accesorios. Para quitar el archivo temporal, podemos actualizar el accesorio `tmp_file()` para que tenga este aspecto:

```Python
@pytest.fixture(scope="module")
def tmp_file(request):
    temp = tempfile.NamedTemporaryFile(delete=False)
    def create():
        return temp.name

    def cleanup():
        os.remove(temp.name)

    request.addfinalizer(cleanup)
    return create
```

Al usar `request.addfinalizer()` y pasar la función `anidada cleanup()`, se llamará a la limpieza en función del ámbito. En este caso, el ámbito es "module", por lo que después de todas las pruebas de un módulo Pytest llamará a esa función de limpieza.

### Uso de conftest.py

Ahora que ha visto accesorios en archivos de prueba, debe tener en cuenta los archivos conftest.py. Estos archivos contienen un significado especial para Pytest. Siempre que haya un archivo conftest.py en un directorio de prueba, significa que puede agregar código como accesorios. Cuando un accesorio está en un conftest.py,_ estará disponible automáticamente para las pruebas sin importarlo.

### Accesorios integrados

Además de poder crear sus propios accesorios, hay un montón de accesorios integrados en Pytest. La mayoría de estos accesorios vienen con sus propias funciones de limpieza para que pueda concentrarse en su uso y no preocuparse por la limpieza.

Estos son algunos accesorios interesantes de Pytest:

* `cache`: permite crear un sistema de almacenamiento en caché para las pruebas
* `capsys`: asistente para capturar y grabar `stderr` y `stdout`
* `tmpdir`: crea y administra directorios temporales
* `monkeypatch`: aplicación de revisiones a módulos, clases o funciones con un comportamiento específico

#### Revisión e invalidación

A veces, el código de producción se escribe de forma que depende estrechamente de otros recursos. Esto dificulta escribir pruebas. Por ejemplo, imagine una función que requiere una base de datos en ejecución o una función que realiza solicitudes HTTP a una API externa. Cuando el código no está desacoplado de la funcionalidad externa, puede usar un patrón denominado *monkey patch*.

Este patrón (y, en este caso, un accesorio) significa que invalidará un módulo, una función o una clase con nombre con un comportamiento específico.

La aplicación de revisiones puede parecer sencilla, pero, de hecho, es muy difícil de conseguir. Este es el motivo por el que es preferible crear código de producción más fácil de probar.

Este es el aspecto que tendría la función `os.path.exists()` al usar el accesorio `monkeypatch`:

```Python
import os

def test_os(monkeypatch):
    monkeypatch.setattr('os.path.exists', lambda x: False)
    assert os.path.exists('/') is False
```

El método `setattr()` puede tomar una cadena con el módulo para aplicar revisiones (`os.path.exists` en este caso) y, a continuación, el código invalidado. Esta prueba usa una función `lambda`, que acepta un único argumento y siempre devuelve false. Opcionalmente, los métodos `setattr()` permiten usar un objeto y un atributo para aplicar revisiones como una cadena. Así es como se puede usar en la misma prueba:

```Python
def test_os(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', lambda x: False)
    assert os.path.exists('/') is False
```

Además de establecer atributos e invalidar métodos, el accesorio `monkeypatch` puede establecer y eliminar variables de entorno, cambiar valores de diccionario y modificar rutas de acceso del sistema.

Modificar el entorno de esta manera puede ser muy problemático, pero el accesorio se encarga de dejar todo como estaba antes de que se iniciara la prueba, lo que hace que sea una buena solución cuando es necesario modificar el entorno.

<hr/>

## Ejercicio

En este ejercicio, usará Pytest con *parametrize* para probar una función. A continuación, actualizará una clase de prueba para usar un accesorio en lugar de un método `setup()` y `teardown()`. El uso de parametrize y el trabajo con accesorios le permitirá ser más flexible al crear o actualizar pruebas.

### Paso 1: Adición de un archivo con pruebas para este ejercicio

1. Cree un archivo de prueba denominado *test_advanced.py* y agregue el código siguiente:

```Python
def str_to_bool(string):
    if string.lower() in ['yes', 'y', '1']:
        return True
    elif string.lower() in ['no', 'n', '0']:
        return False
```

La función `str_to_bool()` acepta una cadena como entrada y, en función de su contenido, devolverá un valor true o false.

2. En el mismo archivo, anexe las pruebas para la función `str_to_bool()`. Use `pytest.mark.parametrize()` para probar primero todos los valores true:

```Python
import pytest 

@pytest.mark.parametrize("string", ['Y', 'y', '1', 'YES'])
def test_str_to_bool_true(string):
    assert str_to_bool(string) is True
```

3. A continuación, anexe otra prueba con los valores false:

```Python
@pytest.mark.parametrize("string", ['N', 'n', '0', 'NO'])
def test_str_to_bool_false(string):
    assert str_to_bool(string) is False
```

Ahora hay dos pruebas que cubren todas las entradas posibles para los valores devueltos true y false.

> ℹ️ **Nota** <br/>
> No es habitual tener pruebas dentro del mismo archivo como código real. Por motivos de simplicidad, los ejemplos de este ejercicio tendrán código real en el mismo archivo. En los proyectos de Python reales, descubrirá que las pruebas están separadas por archivos y directorios del código que está probando.

### Paso 2: Ejecución de las pruebas y exploración del informe

Después de agregar pruebas, el siguiente paso consiste en ejecutar `pytest` e inspeccionar la salida. Use la marca de detalle aumentada (`-v`) para que pueda ver que todos los valores de entrada se tratan como una prueba independiente.

```Bash
$ pytest -v test_avanced.py
============================= test session starts ==============================
Python 3.10.9, pytest-7.3.1, pluggy-1.0.0
rootdir: /private
collected 8 items

test_advanced.py::test_str_to_bool_true[Y] PASSED                        [ 12%]
test_advanced.py::test_str_to_bool_true[y] PASSED                        [ 25%]
test_advanced.py::test_str_to_bool_true[1] PASSED                        [ 37%]
test_advanced.py::test_str_to_bool_true[YES] PASSED                      [ 50%]
test_advanced.py::test_str_to_bool_false[N] PASSED                       [ 62%]
test_advanced.py::test_str_to_bool_false[n] PASSED                       [ 75%]
test_advanced.py::test_str_to_bool_false[0] PASSED                       [ 87%]
test_advanced.py::test_str_to_bool_false[NO] PASSED                      [100%]

============================== 8 passed in 0.01s ===============================
```

Aunque escribió solo dos funciones de prueba, Pytest pudo crear ocho pruebas en total gracias a la función `parametrize()`.

### Paso 3: Migración de una prueba existente a un accesorio

1. Agregue una nueva prueba basada en clases al archivo test_advanced.py . Esta prueba debe usar una función `setup()` y `teardown()` que crea un archivo temporal con texto sobre él. Después de cada prueba, el archivo se elimina. Debería ser parecido a este:

```Python
import os


class TestFile:

    def setup(self):
        with open("/tmp/done", 'w') as _f:
            _f.write("1")

    def teardown(self):
        try:
            os.remove("/tmp/done")
        except OSError:
            pass

    def test_done_file(self):
        with open("/tmp/done") as _f:
            contents = _f.read()
        assert contents == "1"
```

La clase de prueba asegura que se crea un archivo, pero es problemático porque utiliza la ruta de acceso */tmp/*, cuya presencia no está garantizada en todos los sistemas.

2. Cree un accesorio que use el accesorio tmpdir() de Pytest para generar el contenido y devolver la ruta de acceso:

```Python
import pytest

@pytest.fixture
def tmpfile(tmpdir):
    def write():
        file = tmpdir.join("done")
        file.write("1")
        return file.strpath
    return write
```

El accesorio `tmpfile()` usa el accesorio `tmpdir()` de Pytest, que garantiza un archivo temporal válido que se limpia una vez realizadas las pruebas.

3. Actualice la clase `TestFil`e para que use el accesorio en lugar de los métodos del asistente:

```Python
class TestFile:

def test_f(self, tmpfile):
    path = tmpfile()
    with open(path) as _f:
        contents = _f.read()
    assert contents == "1"
```

Esta clase de prueba ahora puede garantizar que se creará y limpiará un archivo temporal con el contenido adecuado para que funcione la aserción.

### Comprobar el trabajo

Ahora debería tener un archivo de Python denominado test_advanced.py con el código siguiente:

* Función `str_to_bool()` que acepta una cadena y devuelve un valor booleano en función del contenido de la cadena.
* Dos pruebas parametrizadas para la función `str_to_bool()`; una prueba los valores true y la otra prueba los valores false.
* Un accesorio de Pytest personalizado que usa el accesorio `tmpdir()` para crear un archivo realizado temporal con algún contenido.
* Clase de prueba que usa el accesorio personalizado `tmpfile()` para crear el archivo.

Todas las pruebas deben pasarse al ejecutarlas en el terminal, sin errores.