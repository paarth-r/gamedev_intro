import pygame as pg
import math

class Cooldown:
    def __init__(self, time: int) -> None:
        '''
        Docstring for __init__
        :param time: Time in seconds
        :type time: int
        '''
        self.start_time = 0
        self.time = self.to_milliseconds(time) # convert to milliseconds and set time # set cooldown time
    def start(self) -> None:
        '''
        Static method used to start 
        '''
        self.start_time = pg.time.get_ticks()

    def to_seconds(self, num: float, return_int: bool = False) -> float:
        '''
        Docstring for to_seconds
        
        :param num: Number to convert from milliseconds to seconds
        :type num: float
        :param return_int: Boolean as to whether or not to round the return value, defaults to False
        :type return_int: bool
        :return: Returns converted value in seconds
        :rtype: float
        '''
        # converts milliseconds to seconds by multiplying by 1000
        if return_int:
            # check if user wants to round and return rounded value
            return math.trunc(num / 1000)
        #otherwise return unrounded value
        return num / 1000
    
    def to_milliseconds(self, num: float, return_int: bool = False) -> float:
        # converts seconds to milliseconds by multiplying by 1000
        if return_int:
            # check if user wants to round and return rounded value
            return math.trunc(num * 1000)
        #otherwise return unrounded value
        return num * 1000

    
    def remaining_time(self) -> float:
        '''
        Docstring for remaining_time
        
        :return: Returns remaining time in seconds
        :rtype: float
        '''
        if self.ready():
            return 0
        current_time = pg.time.get_ticks()
        return self.to_seconds(current_time - self.start_time, return_int=True)
    
    def ready(self) -> bool:
        '''
        Static method used to check if the cooldown is ready
        returns type bool
        '''
        # sets current time
        current_time = pg.time.get_ticks()
        # if the difference between current and start time are greater than self.time
        # return True
        if current_time - self.start_time >= self.time:
            return True
        return False