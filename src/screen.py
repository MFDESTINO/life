import os


class Screen:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def clear(self):
        os.system('clear')
        top = '┌' + '─' * self.width * 2 + '┐\n'
        mid = ('│' + ' ' * self.width * 2 + '│\n') * self.height
        bot = '└' + '─' * self.width * 2 + '┘\n'
        print(top+mid+bot)

    def refresh(self, frame):
        #os.system('clear')
        top = '┌' + '─' * self.width * 2 + '┐\n'
        mid = ''
        for i in range(self.height):
            line = '│'
            for j in range(self.width):
                if frame[i][j]:
                    line += '██'
                else:
                    line += '  '
            line += '│\n'
            mid += line
        bot = '└' + '─' * self.width * 2 + '┘\n'
        print(top+mid+bot)
