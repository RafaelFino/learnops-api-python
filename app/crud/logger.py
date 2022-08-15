from datetime import datetime

# Background Colors to log messages
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Logger:
    def Info(message):
        print(f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.OKCYAN}{message}")

    def Error(message):
        print(f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.FAIL}{message}")

    def Success(message):
        print(f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.OKGREEN}{message}") 

    def Warning(message):
        print(f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.WARNING}{message}")     

    def Ask(message):
        return input(f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.HEADER}{message}")