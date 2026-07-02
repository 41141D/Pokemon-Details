import sys
import requests
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QHBoxLayout
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        icon = "C:/Users/mardi/PycharmProjects/PythonProject3/.venv/img.png"
        self.setWindowTitle("PikaPikaSuiiiiuuUUUUUUuu")
        self.setWindowIcon(QIcon(icon))
        self.button = QPushButton("Search")
        self.button.setObjectName("button")
        self.line = QLineEdit()
        self.line.setPlaceholderText("Enter the Name of the Pokemon")
        self.label = QLabel()
        self.button.clicked.connect(self.search)
        self.label2 = QLabel()
        self.image_label = QLabel()
        self.label3 = QLabel()
        self.label4 = QLabel()
        self.label5 = QLabel()
        self.label6 = QLabel()
        self.initUI()
    def initUI(self):
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label2, alignment=Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        vbox.addWidget(self.label3, alignment=Qt.AlignmentFlag.AlignTop)
        vbox.addWidget(self.label4, alignment=Qt.AlignmentFlag.AlignTop)
        vbox.addWidget(self.label5, alignment=Qt.AlignmentFlag.AlignTop)
        vbox.addWidget(self.label6, alignment=Qt.AlignmentFlag.AlignTop)
        vbox.addWidget(self.image_label, alignment=Qt.AlignmentFlag.AlignRight)
        vbox.addStretch(1)
        vbox.addWidget(self.label)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.line)
        self.line.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.button,alignment=Qt.AlignmentFlag.AlignBottom)
        self.setLayout(vbox)
        self.setGeometry(200, 86, 1200, 700)
        self.setStyleSheet("""
        QPushButton {color: black;
        border: 1px solid black;
        border-radius: 5px;
        font-size: 15px;
        font-weight: bold;
        font-family: Comic Sans MS;
        }
        QWidget {
        
        background-color: #9eb8ff;
        
        }
        QPushButton#button:hover {background-color: grey;}
        QLineEdit {font-size: 15px;
        border: 1px solid black;
        border-radius: 5px;
        font-family: Comic Sans MS;
        }
        QLabel {color: black;
        font-size: 25px;
        font-weight: bold;}
        """)
    def search(self):
        poke_name=self.line.text().lower().strip()
        api = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
        response = requests.get(api)
        data = response.json()

        if self.line.text() == "":
            self.label.setText("Please enter the Pokemon Name")
        elif response.status_code == 200:
            pokemon_image = data["sprites"]["front_default"]
            pokemon_type =  data['types'][0]['type']['name']
            pokemon_id = data['id']
            pokemon_height = data["height"]
            pokemon_weight = data["weight"]/10
            pokemon_ability = data["abilities"][0]["ability"]["name"]
            str(pokemon_id)
            image_data = requests.get(pokemon_image).content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            scaled_pixmap = pixmap.scaled(400, 400,
                                          Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation
                                          )
            self.image_label.setPixmap(scaled_pixmap)
            self.label2.setText("Pokemon Type: " + pokemon_type)
            self.label3.setText("Pokemon ID: " + str(pokemon_id))
            self.label4.setText("Pokemon Height: " + str(pokemon_height)+ " DeciMeters")
            self.label5.setText("Pokemon Weight: " + str(pokemon_weight) + " Kilograms")
            self.label6.setText("Pokemon Ability: " + pokemon_ability)
        else:
            self.label.setText("Please enter a valid Pokemon Name")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
#Im Beat.
