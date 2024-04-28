class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MAX_CHANNEL = 3
    MIN_CHANNEL = 0

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """function to turn TV on/off"""
        self.__status = not self.__status

    def mute(self) -> None:
        """function mutes the TV"""
        if self.__status:
            self.__muted = not self.__muted

    def volume_down(self) -> None:
        """function reduces the volume by 1"""
        if self.__status:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def volume_up(self) -> None:
        """function increases the volume by 1"""
        if self.__status:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def channel_up(self) -> None:
        """function increases the channel value by 1"""
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """function decreases the channel value by 1"""
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def __str__(self) -> str:
        """function prints out the statement that represents the power status, channel value, and volume value"""
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


