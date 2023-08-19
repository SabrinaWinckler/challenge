from controller.ContaController import app
from setup.init_db import *

criar_registros()
app.run(debug=True)