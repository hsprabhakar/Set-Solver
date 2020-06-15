# Set Game's card selection window
# This program will show all the cards in the deck for a game of set
# you can choose how many cards are currentely in play. The program will return a
# list which contains lists which contain the attributes of each card selected.


import pygame


def CardsWindow():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((1334, 750))
    # set the title of the display window
    pygame.display.set_caption('Set Game Selection Window')
    # get the display surface
    w_surface = pygame.display.get_surface()
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    CardsClicked = game.play()
    # quit pygame and clean up the pygame window
    pygame.quit()

    return CardsClicked


# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object

        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')

        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        # === game specific objects
        # Call to the class method to set the surface for the tile objects
        # >Name of the class>.<name of the class method>()
        Tile.set_surface(self.surface)

        # Need to initialize tile objects
        # Could create a identifer for each tile (not scalable)
        # Could create a list of all tiles (doesn't represent a grid)
        # We will make a 3x3 matrix of the tiles
        # Accomplish this by making a list of list i.e. a list of rows

        self.NumberIndexCalled = -1
        self.ShapeIndexCalled = -1
        self.ColorIndexCalled = -1
        self.ShadingIndexCalled = -1
        self.Index = -1
        self.CardsClicked, self.board, self.image_list = [], [], []
        self.ReferenceImage = pygame.image.load('images/A1PNG.png')
        self.load_images()
        self.create_board()

    def load_images(self):
        # append the images to the list
        Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        for i in range(0, 9):
            for index in range(1, 10):
                image = pygame.image.load('images/' + str(Letters[i]) + str(index) + 'PNG.png')
                self.image_list.append(image)

    def create_board(self):
        width = self.ReferenceImage.get_width()
        height = self.ReferenceImage.get_height()

        for row_index in range(0, 9):
            row = []
            for col_index in range(0, 9):
                # item = (row_index, col_index)
                # Replace "item" with tiles
                x = width * col_index
                y = height * row_index
                tile = Tile(x, y, width, height)
                tile.attributes = [self.GiveNumberIndex(), self.GiveShapeIndex(),
                                   self.GiveColorIndex(), self.GiveShadingIndex()]
                row.append(tile)
            self.board.append(row)

    def GiveNumberIndex(self):
        self.NumberIndexCalled += 1
        if 0 <= self.NumberIndexCalled <= 8:
            return 1
        elif 8 < self.NumberIndexCalled <= 17:
            return 2
        elif 17 < self.NumberIndexCalled <= 26:
            if self.NumberIndexCalled == 26:
                self.NumberIndexCalled = -1
            return 3

    def GiveShapeIndex(self):
        self.ShapeIndexCalled += 1
        if 0 <= self.ShapeIndexCalled <= 26:
            return 2
        elif 26 < self.ShapeIndexCalled <= 53:
            return 1
        elif 53 < self.ShapeIndexCalled <= 90:
            return 3

    def GiveColorIndex(self):
        self.ColorIndexCalled += 1
        if 0 <= self.ColorIndexCalled <= 2:
            return 1
        elif 2 < self.ColorIndexCalled <= 5:
            return 2
        elif 5 < self.ColorIndexCalled <= 8:
            if self.ColorIndexCalled == 8:
                self.ColorIndexCalled = -1
            return 3

    def GiveShadingIndex(self):
        self.ShadingIndexCalled += 1
        if self.ShadingIndexCalled == 0:
            return 1
        elif self.ShadingIndexCalled == 1:
            return 2
        elif self.ShadingIndexCalled == 2:
            self.ShadingIndexCalled = -1
            return 3

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.game_Clock.tick(self.FPS)  # run at most with FPS Frames Per Second
        return self.CardsClicked

    def handle_events(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            if event.type == pygame.MOUSEBUTTONUP and self.continue_game:
                self.handle_mouse_up(event.pos)

    def handle_mouse_up(self, position):
        # position is the (x,y) location of the click and is of type tuple
        for row in self.board:
            for tile in row:
                if tile.select(position):  # click inside unoccupied tile
                    self.CardsClicked.append(tile.attributes)
        print(self.CardsClicked)

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color)  # clear the display surface first
        for row in self.board:
            for tile in row:
                self.surface.blit(self.image_list[self.GiveIndex()], (tile.x, tile.y))
                tile.draw()
        pygame.display.update()  # make the updated surface appear on the display

    def GiveIndex(self):
        self.Index = self.Index + 1
        if self.Index > len(self.image_list) - 1:
            self.Index = 0
        return self.Index

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update
        pass

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        pass


class Tile:
    # Class attributes are attrbites that are the samw for all tile objects
    surface = None
    border_width = 3
    border_color = pygame.Color('black')

    @classmethod
    # A class method is used to set or change the value of a class attribute
    def set_surface(cls, surface_from_game):
        # cls is a parameter that gets bound to the name of the class
        # surface_from_game gets bound to the object that the argumet (self.surface) is bound to
        cls.surface = surface_from_game

    # Instance Methods
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.image = None
        self.attributes = []

    def draw(self):
        pygame.draw.rect(Tile.surface, Tile.border_color, self.rect, Tile.border_width)

    def select(self, position):
        valid_click = False
        if self.rect.collidepoint(position):
            valid_click = True
        return valid_click


CardsClicked = CardsWindow()
