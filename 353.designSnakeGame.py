import collections

class SnakeGame:
    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.snake = collections.deque([(0,0)])
        self.food = collections.deque(food)
        self.direct = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        h, v = self.direct[direction]
        x, y = self.snake[0]
        x, y = x+h, y+v
        if not ((0 <= x < self.width) and (0 <= y < self.height)): # out of range
            return -1
        if (x,y) in self.snake and (x,y)!= self.snake[-1]: # eat itself
            return -1
        else:
            if self.food and self.food[0] == (x,y): # eat food
                self.snake.appendleft(self.food[0])
                self.food.popleft()
            else:   # move snake
                self.snake.appendleft(self.food[0])
                self.snake.pop()
            return len(self.snake) - 1