import random
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from view import *


class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        """
        Initializes the GUI and creates all private variables specifically,
        word_list and labels_list have data added to them.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.__position = 0
        self.__clue = ""
        self.__guess = ""

        self.__word_list = []
        self.__word_file = open("words.txt")
        for word in self.__word_file:
            self.__word_list.append(word.strip().lower())

        self.__answer = random.choice(self.__word_list)
        self.__num_of_guesses = 0
        self.__guessed_correctly = False
        self.__label_number = 0
        self.__labels_list = [self.label_1_1, self.label_1_2, self.label_1_3, self.label_1_4, self.label_1_5,
                              self.label_2_1, self.label_2_2, self.label_2_3, self.label_2_4, self.label_2_5,
                              self.label_3_1, self.label_3_2, self.label_3_3, self.label_3_4, self.label_3_5,
                              self.label_4_1, self.label_4_2, self.label_4_3, self.label_4_4, self.label_4_5,
                              self.label_5_1, self.label_5_2, self.label_5_3, self.label_5_4, self.label_5_5,
                              self.label_6_1, self.label_6_2, self.label_6_3, self.label_6_4, self.label_6_5,
                              ]

    def keyPressEvent(self, event):
        """
        Function to handle the main code for the game when the user presses enter,
        which takes in the input and resets the text edit.
        :param event: Return key is the triggering event.
        :return: None.
        """
        if event.key() == Qt.Key_Return:
            if self.__num_of_guesses < 6 and not self.__guessed_correctly:
                if self.input_word.text().strip().lower() in self.__word_list:
                    self.__guess = self.input_word.text().strip().lower()
                    self.input_word.setText("")
                    self.__num_of_guesses += 1
                    self.__guessed_correctly = self.process_guess(self.__answer, self.__guess, self.__num_of_guesses)
                else:
                    self.label_errors.setText('Word is not in list')
            if self.__guessed_correctly:
                self.label_errors.setText('You guessed the word in ' + str(self.__num_of_guesses) + ' guesses')
            if self.__num_of_guesses == 6 and not self.__guessed_correctly:
                self.label_errors.setText('Out of guesses the word was ' + self.__answer)

    def process_guess(self, answer: str, guess: str, num_guesses: int):
        """
        Function to check how the letters in guess match the letters in answer.
        :param answer: A randomly selected word from words.txt.
        :param guess: User entered input from the textedit prompted by the enter key.
        :param num_guesses: Amount of times a valid guess has been inputted .
        :return: Returns self.__clue if it is equivalent to 5 correct letters.
        """
        self.__position = 0
        self.__clue = ""
        for letter in guess:
            if letter == answer[self.__position]:
                self.__clue += "G"
                self.__label_number = (num_guesses * 5) + (self.__position - 5)
                self.__labels_list[self.__label_number].setText(letter)
                self.__labels_list[self.__label_number].setStyleSheet("background-color: green;")
            elif letter in self.__answer:
                self.__clue += "Y"
                self.__label_number = (num_guesses * 5) + (self.__position - 5)
                self.__labels_list[self.__label_number].setText(letter)
                self.__labels_list[self.__label_number].setStyleSheet("background-color: yellow;")
            else:
                self.__clue += "-"
                self.__label_number = (num_guesses * 5) + (self.__position - 5)
                self.__labels_list[self.__label_number].setText(letter)
                self.__labels_list[self.__label_number].setStyleSheet("background-color: gray;")
            self.__position += 1
        return self.__clue == "GGGGG"
