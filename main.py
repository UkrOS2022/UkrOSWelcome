from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
import subprocess
import time

time.sleep(5)

class UkrOSWelcome(QWidget):
    def __init__(self):
        super().__init__()

        buttons = """
            QPushButton {
                background-color: #B1B1B1;
                color: black;
                border: 2px solid #B1B1B1;
                border-radius: 5px;
                padding: 8px;
            }

            QPushButton:hover {
                background-color: #8B8B8B;
                color: white;
            }
        """
        
        h1 = """
            QLabel {
                font-size: 30px;
            }
        """

        # Set up media player for welcome sound
        self.media_player = QMediaPlayer()
        sound_path = os.path.abspath("sounds/title.mp3")
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(sound_path)))
        self.media_player.play()

        # Set up main window properties
        self.setWindowTitle(self.tr("Welcome to UkrOS"))
        self.setGeometry(100, 100, 600, 400)
        self.setFixedSize(600, 400)
        icon = QIcon('images/icon.png')
        self.setWindowIcon(icon)
        self.setStyleSheet(buttons)

        # First page widgets
        self.label_first = QLabel(self.tr("Welcome to UkrOS"), self)
        self.label_first.setGeometry(5, 5, 590, 50)
        self.label_first.setStyleSheet(h1)

        self.label_second = QLabel(self.tr("Welcome to UkrOS. This window for \ncontinuation of installing UkrOS. If you \nwant to continue of installing UkrOS, \nplease to click button \"Next\""), self)
        self.label_second.setGeometry(25, 150, 250, 70)

        self.cancel_button = QPushButton(self.tr("Cancel"), self)
        self.cancel_button.clicked.connect(self.cancel)
        self.cancel_button.setGeometry(5, 360, 60, 35)

        self.next_button = QPushButton(self.tr("Next"), self)
        self.next_button.clicked.connect(self.next_second)
        self.next_button.setGeometry(535, 360, 60, 35)

        # Second page widgets
        self.connect_button = QPushButton(self.tr("Connect"), self)
        self.connect_button.clicked.connect(self.connect)
        self.connect_button.setGeometry(460, 360, 70, 35)
        self.connect_button.hide()

        self.next_button_second = QPushButton(self.tr("Next"), self)
        self.next_button_second.clicked.connect(self.next_third)
        self.next_button_second.setGeometry(535, 360, 60, 35)
        self.next_button_second.hide()
        
        
        # THIRD PAGE
        
        self.telegram_checkbox = QCheckBox("Telegram", self)
        self.telegram_checkbox.setGeometry(25, 150, 200, 20)
        self.telegram_checkbox.hide()
        
        self.blender_checkbox = QCheckBox("Blender", self)
        self.blender_checkbox.setGeometry(25, 170, 200, 20)
        self.blender_checkbox.hide()
        
        self.librecad_checkbox = QCheckBox("LibreCAD", self)
        self.librecad_checkbox.setGeometry(25, 190, 200, 20)
        self.librecad_checkbox.hide()
        
        self.sqlitebrowser_checkbox = QCheckBox("DB Browser (SQLiteBrowser)", self)
        self.sqlitebrowser_checkbox.setGeometry(25, 210, 200, 20)
        self.sqlitebrowser_checkbox.hide()
        
        self.qtdesigner_checkbox = QCheckBox("Qt Designer", self)
        self.qtdesigner_checkbox.setGeometry(25, 230, 200, 20)
        self.qtdesigner_checkbox.hide()

        self.next_button_third = QPushButton(self.tr("Next"), self)
        self.next_button_third.clicked.connect(self.next_fourth)
        self.next_button_third.setGeometry(535, 360, 60, 35)
        self.next_button_third.hide()


        # FOURTH PAGE
        self.exit_button = QPushButton(self.tr("Exit"), self)
        self.exit_button.clicked.connect(self.setup_complete)
        self.exit_button.setGeometry(535, 360, 60, 35)
        self.exit_button.hide()

        self.label_exit = QLabel(self.tr("The installation was finished. You can \nclick button \"Exit\""), self)
        self.label_exit.setGeometry(25, 150, 250, 55)
        self.label_exit.hide()

    def cancel(self):
        self.close()

    def next_second(self):
        # Update labels for the second page
        self.label_first.setText(self.tr("Add account to Thunderbird"))
        self.label_second.setText(self.tr("Do you want to connect your account to \nmail client Thunderbird?\n\nIf you want to connect your account, you \nmust click on the button \"Connect\""))

        # Show relevant buttons for the second page
        self.connect_button.show()
        self.next_button_second.show()

    def connect(self):
        # Attempt to open Thunderbird
        try:
            subprocess.Popen(['thunderbird', '--display=:0', '-AddProfile'])
        except Exception as e:
            print(f"Error opening Thunderbird: {e}")

    def next_third(self):
        # Hide buttons and labels from the second page
        self.connect_button.hide()
        self.next_button_second.hide()
        self.label_second.hide()

        # Update labels for the third page
        self.label_first.setText(self.tr("What programs do you want to install?"))
        self.label_first.setGeometry(5, 5, 590, 70)

        # Show checkboxes for different programs and the "Next" button
        self.telegram_checkbox.show()
        self.blender_checkbox.show()
        self.librecad_checkbox.show()
        self.sqlitebrowser_checkbox.show()
        self.qtdesigner_checkbox.show()
        self.next_button_third.show()

    def next_fourth(self):
        # Collect selected programs
        selected_programs = []

        # Add selected programs to the list
        if self.telegram_checkbox.isChecked():
            selected_programs.append("telegram-desktop")
        if self.blender_checkbox.isChecked():
            selected_programs.append("blender")
        if self.librecad_checkbox.isChecked():
            selected_programs.append("librecad")
        if self.sqlitebrowser_checkbox.isChecked():
            selected_programs.append("sqlitebrowser")
        if self.qtdesigner_checkbox.isChecked():
            selected_programs.append("qt-designer")

        # If there are selected programs, install them using the terminal
        if selected_programs:
            programs_to_install = ' '.join(selected_programs)
            command = f'sudo apt-get install {programs_to_install} -y'
            
            try:
                subprocess.run(['gnome-terminal', '--', 'bash', '-c', command])
            except Exception as e:
                print(f"Error executing command: {e}")

        # Hide widgets from the third page
        self.telegram_checkbox.hide()
        self.blender_checkbox.hide()
        self.librecad_checkbox.hide()
        self.sqlitebrowser_checkbox.hide()
        self.qtdesigner_checkbox.hide()
        self.next_button_third.hide()
        self.cancel_button.hide()
        self.next_button_third.hide()

        # Update labels for the fourth page
        self.label_first.setText(self.tr("Finished"))
        self.label_first.setGeometry(5, 5, 590, 50)

        # Show exit button and completion message
        self.exit_button.show()
        self.label_exit.show()

    def setup_complete(self):
        self.remove_from_startup()
        self.close()

    def remove_from_startup(self):
        # Get the current user's home directory
        home_dir = os.path.expanduser("~")

        # Create or open the autostart desktop file
        autostart_file_path = os.path.join(home_dir, ".config/autostart/ukroswelcome.desktop")

        # Remove the autostart file if it exists
        if os.path.exists(autostart_file_path):
            os.remove(autostart_file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome_window = UkrOSWelcome()
    welcome_window.show()
    sys.exit(app.exec_())
