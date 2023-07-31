import pyautogui as bot
import pyperclip as ppc
import time

class DataProcessingBot:
    """
    A class to automate data processing.

    ...

    Attributes
    ----------
    counter_keyword1 : int
        A counter for the first keyword.
    counter_keyword2 : int
        A counter for the second keyword.
    keyword_one_down : int
        Y-coordinate of the first keyword row.
    keyword_two_down : int
        Y-coordinate of the second keyword row.
    keyword_three_down : int
        Y-coordinate of the third keyword row.
    result_down : int
        Y-coordinate of the result row.
    result_right : int
        X-coordinate of the result column.

    Methods
    -------
    copy_paste(source_x, source_y, destination_x, destination_y)
        Copy content from the source location and paste it to the destination location.
    process_data()
        Process data using the automation logic.
    """
    def __init__(self):
        bot.PAUSE = 1.0
        bot.FAILSAFE = False

        self.counter_keyword1 = 0
        self.counter_keyword2 = 0
        self.keyword_one_down = 220
        self.keyword_two_down = 220
        self.keyword_three_down = 220
        self.result_down = 220
        self.result_right = 143
        self.FIRST_ROW_X = 143
        self.FIRST_ROW_Y = 220
        self.sheet_increment = 229
        self.END_REACHED = False
        self.end_message = "You've"
        self.temp = "empty"
        self.empty_check = "nothing"
        self.empty = "Your"

    def copy_paste(self, source_x, source_y, destination_x, destination_y):
        """
        Copy content from the source location and paste it to the destination location.

        Parameters
        ----------
        source_x : int
            X-coordinate of the source location.
        source_y : int
            Y-coordinate of the source location.
        destination_x : int
            X-coordinate of the destination location.
        destination_y : int
            Y-coordinate of the destination location.
        """
        bot.click(source_x, source_y) # Click on source location.
        bot.hotkey('ctrl', 'c') # Copy the content.
        time.sleep(0.5)
        bot.click(destination_x, destination_y) # Click on destination location.
        bot.hotkey('ctrl', 'a') # Select all contents in the textbox.
        bot.press('backspace') # Delete contents in the text box.
        bot.hotkey('ctrl', 'v') # Paste the copied content.

    def process_data(self):
        """
        Process data using the automation logic.
        """
        while self.counter_keyword2 != 7:
            bot.click(32, 576) # Click on libre office.
            bot.click(301, 1047) # Click on sheet number 2.
            bot.click(1076, self.keyword_two_down) # Click on row x.
            self.copy_paste(1076, self.keyword_two_down, 617, 353)

            for i in range(14):
                bot.click(32, 576) # Click on libre office.
                bot.click(387, 1049) # Click on sheet number 3.
                bot.click(294, self.keyword_three_down) # Click on row x.
                self.copy_paste(294, self.keyword_three_down, 652, 395)

                bot.click(983, 1010) # Click the search button.
                time.sleep(2) # Program will sleep for 2 seconds to allow the page to load.

                bot.press('F5') # Refresh the page
                time.sleep(3)

                bot.moveTo(1704, 80) # Move the mouse to the back to top extension.
                bot.click()
                time.sleep(2)

                bot.moveTo(1704, 80) # Move the mouse to the back to top extension.
                bot.click()
                time.sleep(2)

                bot.moveTo(484, 304) # Move the mouse to the result.
                time.sleep(2)
                bot.doubleClick() # Double click the result to highlight the number.
                bot.hotkey('ctrl', 'c')

                self.empty_check = str(ppc.paste()) # Copy the number of the result and store it in the amount variable.

                if (self.empty_check != self.empty):
                    bot.moveTo(484, 304) # Move the mouse to the result.
                    bot.moveTo(484, 304) # Move the mouse to the result.
                    bot.doubleClick() # Double click the result to highlight the number.
                    bot.hotkey('ctrl', 'c')

                    amount = int(ppc.paste()) # Copy the number of the result and store it in the amount variable.

                    if (amount > 10):
                        while self.END_REACHED == False:
                            bot.moveTo(1673, 80) # Move the mouse to the bottom page extension.
                            bot.click() # Bot will click the extension down button.
                            time.sleep(2)
                            bot.moveTo(512, 1058) # Move the mouse to the location where the message appears.
                            bot.doubleClick() # Double click to select the message.
                            bot.hotkey('ctrl', 'c')
                            self.temp = str(ppc.paste()) # Capture the result and store it in a temp variable.

                            if (self.temp == self.end_message):
                                self.END_REACHED = True # If the temp matches the end message then end the loop.
                            else:
                                continue # If they don't then continue the loop.

                        bot.moveTo(1704, 80) # Click the page up extension
                        bot.click()
                        time.sleep(2)

                        bot.moveTo(1704, 80) # Click the page up extension
                        bot.click()
                        time.sleep(2)

                        bot.moveTo(1673, 80) # Move the mouse to the bottom page extension.
                        bot.click() # Bot will click the extension down button.
                        time.sleep(2)

                        bot.moveTo(1704, 80) # Click the page up extension
                        bot.click()
                        time.sleep(2)

                        bot.moveTo(844, 234)
                        bot.rightClick()
                        bot.moveTo(886, 508)
                        bot.moveTo(1255, 535)
                        bot.click()

                        bot.click(725, 725) # Click on select all which will select all of the papers found.
                        bot.click(1270, 725) # Click on ok to save the papers to Zorato.

                        # bot.press('F5') # Refresh the page
                        time.sleep(15)

                        bot.moveTo(1704, 80) # Click the page up extension
                        bot.click()
                        time.sleep(2)

                        bot.moveTo(484, 302) # Move the mouse to the result.
                        bot.moveTo(484, 302) # Move the mouse to the result.
                        bot.doubleClick() # Double click the result to highlight the number.
                        bot.hotkey('ctrl', 'c')

                        amount = int(ppc.paste()) # Copy the number of the result and store it in the amount variable.

                        bot.click(32, 576) # Click on libre.
                        bot.click(461, 1049) # Click on sheet number 4.
                        bot.click(self.result_right, self.result_down) # Click on row x.
                        bot.hotkey('ctrl', 'shift', 'alt', 'v')
                    else:
                        # bot.moveTo(1641, 80) # Move to the zortero extension
                        # bot.click() # Click on Zorato extension.

                        bot.moveTo(844, 234)
                        bot.rightClick()
                        bot.moveTo(886, 508)
                        bot.moveTo(1255, 535)
                        bot.click()

                        bot.click(725, 725) # Click on select all which will select all of the papers found.
                        bot.click(1270, 725) # Click on ok to save the papers to Zorato.

                        time.sleep(5)

                        bot.click(32, 576) # Click on libre.
                        bot.click(461, 1049) # Click on sheet number 4.
                        bot.click(self.result_right, self.result_down) # Click on row x.
                        bot.hotkey('ctrl', 'shift', 'alt', 'v')
                else:
                    bot.click(32, 576) # Click on libre.
                    bot.click(461, 1049) # Click on sheet number 4.
                    bot.click(result_right, result_down) # Click on row x.
                    bot.typewrite('0')
        
                bot.click(31, 52) # Click on chrome.
                bot.click(1479, 202) # Click on the options to bring the bot back to the search engine.
        
                END_REACHED = False
                result_down = result_down + 18
                keyword_three_down = keyword_three_down + 18
            result_down = 220
            keyword_three_down = 220
            result_right = result_right + 80
            keyword_two_down = keyword_two_down + 18
            counter_keyword2 = counter_keyword2 + 1

def main():
    """
    The main function to call the DataProcessingBot class and execute data processing.
    """
    bot.alert('Please ensure that all required applications are open and the correct sheets are active.')
    time.sleep(5)
    bot.alert('Data processing will begin now.')
    time.sleep(3)
    
    data_bot = DataProcessingBot()
    data_bot.process_data()

if __name__ == "__main__":
    main()