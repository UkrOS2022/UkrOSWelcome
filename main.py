from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
import subprocess

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
        self.label_first = QLabel("Welcome to UkrOS", self)
        self.label_first.setGeometry(5, 5, 590, 50)
        self.label_first.setStyleSheet(h1)

        self.label_second = QLabel("Welcome to UkrOS. This window for \ncontinuation of installing UkrOS. If you \nwant to continue of installing UkrOS, \nplease to click button \"Next\"", self)
        self.label_second.setGeometry(25, 150, 250, 70)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.clicked.connect(self.cancel)
        self.cancel_button.setGeometry(5, 360, 60, 35)

        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.next_second)
        self.next_button.setGeometry(535, 360, 60, 35)

        # Second page widgets
        self.connect_button = QPushButton("Connect", self)
        self.connect_button.clicked.connect(self.connect)
        self.connect_button.setGeometry(460, 360, 70, 35)
        self.connect_button.hide()

        self.next_button_second = QPushButton("Next", self)
        self.next_button_second.clicked.connect(self.next_third)
        self.next_button_second.setGeometry(535, 360, 60, 35)
        self.next_button_second.hide()
        
        
        # THIRD PAGE
        
        self.community_label = QLabel("Please to write your community for finding of weather.", self)
        self.community_label.setGeometry(25, 125, 330, 30)
        self.community_label.hide()
        
        self.community_input = QLineEdit("Your community", self)
        self.community_input.setGeometry(25, 150, 130, 30)
        self.community_input.hide()

        self.add_button = QPushButton("Add", self)
        self.add_button.clicked.connect(self.add)
        self.add_button.setGeometry(25, 185, 60, 35)
        self.add_button.hide()

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.clicked.connect(self.delete)
        self.delete_button.setGeometry(90, 185, 60, 35)
        self.delete_button.hide()

        self.next_button_third = QPushButton("Next", self)
        self.next_button_third.clicked.connect(self.next_fourth)
        self.next_button_third.setGeometry(535, 360, 60, 35)
        self.next_button_third.hide()

        self.list =  []
        self.listbox = QListWidget(self)
        self.listbox.setGeometry(160, 150, 200, 150)
        self.listbox.hide()


        # FOURTH PAGE
        
        self.background_label = QLabel("Please to choose your desktop background.", self)
        self.background_label.setGeometry(25, 125, 330, 30)
        self.background_label.hide()

        self.carpatian_background_label = QPushButton(self)
        self.carpatian_background = QIcon('/usr/share/backgrounds/UkrOS/carpatian.jpg')
        self.carpatian_background_label.setIcon(self.carpatian_background)
        self.carpatian_background_label.setIconSize(QSize(126, 96))
        self.carpatian_background_label.setGeometry(25, 150, 120, 60)
        self.carpatian_background_label.clicked.connect(self.set_carpatian_background)
        self.carpatian_background_label.hide()

        self.autumn_background_label = QPushButton(self)
        self.autumn_background = QIcon('/usr/share/backgrounds/UkrOS/autumn.jpg')
        self.autumn_background_label.setIcon(self.autumn_background)
        self.autumn_background_label.setIconSize(QSize(126, 96))
        self.autumn_background_label.setGeometry(150, 150, 120, 60)
        self.autumn_background_label.clicked.connect(self.set_autumn_background)
        self.autumn_background_label.hide()

        self.palanok_background_label = QPushButton(self)
        self.palanok_background = QIcon('/usr/share/backgrounds/UkrOS/palanok.jpg')
        self.palanok_background_label.setIcon(self.palanok_background)
        self.palanok_background_label.setIconSize(QSize(126, 96))
        self.palanok_background_label.setGeometry(275, 150, 120, 60)
        self.palanok_background_label.clicked.connect(self.set_palanok_background)
        self.palanok_background_label.hide()

        self.dnipro_background_label = QPushButton(self)
        self.dnipro_background = QIcon('/usr/share/backgrounds/UkrOS/dnipro.jpg')
        self.dnipro_background_label.setIcon(self.dnipro_background)
        self.dnipro_background_label.setIconSize(QSize(126, 96))
        self.dnipro_background_label.setGeometry(400, 150, 120, 60)
        self.dnipro_background_label.clicked.connect(self.set_dnipro_background)
        self.dnipro_background_label.hide()

        self.next_button_fourth = QPushButton("Next", self)
        self.next_button_fourth.clicked.connect(self.next_fiveth)
        self.next_button_fourth.setGeometry(535, 360, 60, 35)
        self.next_button_fourth.hide()


        # FIFTH PAGE

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.setup_complete)
        self.exit_button.setGeometry(535, 360, 60, 35)
        self.exit_button.hide()

        self.label_exit = QLabel("The installation was finished. You can \nclick button \"Exit\"", self)
        self.label_exit.setGeometry(25, 150, 250, 55)
        self.label_exit.hide()
    
    def set_dnipro_background(self):
        self.background_label.setText('You set background of: Dnipro')
        subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-uri', 'file://' + '/usr/share/backgrounds/UkrOS/dnipro.jpg'])
    
    def set_palanok_background(self):
        self.background_label.setText('You set background of: Palanok')
        subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-uri', 'file://' + '/usr/share/backgrounds/UkrOS/palanok.jpg'])
    
    def set_autumn_background(self):
        self.background_label.setText('You set background of: Autumn')
        subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-uri', 'file://' + '/usr/share/backgrounds/UkrOS/autumn.jpg'])
    
    def set_carpatian_background(self):
        self.background_label.setText('You set background of: Carpathian')
        subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-uri', 'file://' + '/usr/share/backgrounds/UkrOS/carpatian.jpg'])

    def cancel(self):
        self.close()

    def add(self):
        text = self.community_input.text()
        self.list.append(str(text))
        self.listbox.clear()
        self.listbox.addItems(self.list)

    def delete(self):
        selected_item = self.listbox.currentItem()
        if selected_item:
            text = selected_item.text()
            self.list.remove(text)
            self.listbox.clear()
            self.listbox.addItems(self.list)

    def next_second(self):
        # Update labels for the second page
        self.label_first.setText("Add account to Thunderbird")
        self.label_second.setText("Do you want to connect your account to \nmail client Thunderbird?\n\nIf you want to connect your account, you \nmust click on the button \"Connect\"")

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

        # Update labels for the fourth page
        self.label_first.setText("Add your community")

        # Show exit button and completion message
        self.community_label.show()
        self.community_input.show()
        self.add_button.show()
        self.delete_button.show()
        self.next_button_third.show()
        self.listbox.show()

    def next_fourth(self):

        # Get the home directory of the current user
        home_directory = os.path.expanduser("~")
            
        # Construct the full file path
        file_path = os.path.join(home_directory, '.programdates', 'weather.txt')

        with open(file_path, 'w') as f:
            for item in self.list:
                f.write(f'{item}\n')
        
        # Hide widgets from the third page
        self.community_label.hide()
        self.community_input.hide()
        self.add_button.hide()
        self.delete_button.hide()
        self.next_button_fourth.hide()
        self.listbox.hide()

        # Update labels for the fourth page
        self.label_first.setText("Selecting of background")

        # Show exit button and completion message
        self.next_button_fourth.show()
        self.background_label.show()
        self.carpatian_background_label.show()
        self.autumn_background_label.show()
        self.palanok_background_label.show()
        self.dnipro_background_label.show()

    def next_fiveth(self):

        # Hide widgets from the third page
        self.cancel_button.hide()
        self.next_button_fourth.hide()
        self.background_label.hide()
        self.carpatian_background_label.hide()
        self.autumn_background_label.hide()
        self.palanok_background_label.hide()
        self.dnipro_background_label.hide()

        # Update labels for the fourth page
        self.label_first.setText("Finished")

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
