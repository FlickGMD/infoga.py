Infoga es una herramienta de OSINT inspirada en [phoneinfoga](https://sundowndev.github.io/phoneinfoga) y diseñada para recopilar información sobre números de teléfono utilizando APIs externas.
Para sacar una API visita el siguiente [enlace](https://apilayer.com/)

## 🚀 Instalación

Clona el repositorio y asegúrate de tener las dependencias necesarias:

```bash
# Clonar el repositorio
git clone https://github.com/FlickGMD/infoga.py
cd infoga.py

# Instalar dependencias
python3 -m venv .venv && source .venv/bin/activate
pip3 install --disable-pip-version-check -r requirements.txt
```

## 🔍 Uso

Ejecuta el script con los siguientes parámetros:

```bash
python3 infoga.py [PARAMETROS] [ARGUMENTOS]
```

### Opciones disponibles:

```
  -h, --help            Muestra este mensaje de ayuda y sale.
  -p, --phone PHONE     📞 Número de teléfono a analizar.
                         Ejemplo: infoga.py --phone +1 234 567 89

  -a, --api API         🔑 API KEY necesaria para la búsqueda.
                         Ejemplo: infoga.py --api abcd1234fghi789
                         Para obtener una API Key, visita: https://apilayer.com

  -o, --output OUTPUT   📄 Archivo donde se guardará la evidencia.
                         Ejemplo: infoga.py --output /tmp/file.txt

  -x, --exclude_banner  Excluir el banner al mostrar información.
```

## 🌎 Ejemplo de Uso

```bash
python3 infoga.py --phone +34 612 345 678 --api TU_API_KEY --output resultado.txt
```

![imagen](./images/test.jpg)

Esto analizará el número de teléfono y guardará la información en `resultado.txt`.

---

⚠️ **Nota:** Usa esta herramienta de manera ética y legal. No nos hacemos responsables del mal uso de la misma.


