# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os 
import pandas as pd

def create_file_cvs(name_cvs, dir_input_path, dir_ouput_path):
    #Definicion de variables
    row = []
    #Recorrido por cada una de las carpetas presentes en la ruta de entrada.
    for folder in os.listdir(dir_input_path):
        #Union de ruta con el nombre de la carpeta
        folder_path = os.path.join(dir_input_path, folder)
        #Recorrido por uno de los elmentos presentes en las carpeta.
        for file in os.listdir(folder_path):
            #Union de ruta de la carpeta con el nombre del archivo de texto
            text_path = os.path.join(folder_path, file)
            #Agregar linea de texto como una serie a la lista
            with open(text_path, "r") as f:
                row.append({"phrase" : f.read(), "target" : str(folder)})
    #Generar dataframe
    df = pd.DataFrame(row)
    #Convertir y guardar dataframe como a csv
    output_file = os.path.join(dir_ouput_path, name_cvs)
    df.to_csv(output_file, index=False)

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    #Crear "test_dataset.csv"
    create_file_cvs("test_dataset.csv", "./files/input/test", "./files/output")
    #Crear "train_dataset.csv"
    create_file_cvs("train_dataset.csv", "./files/input/train", "./files/output")


