class units():
    def __init__(self):
        """Units of measurement and function for converting between them"""
        self.volume = [
            'cubic metre',
            'barrel',
            'cubic foot',
            'litre',
            'gallon',
            'pint',
            'cubic inch',
            'cubic centimetre'
        ]

        self.time = [
            'miliseconds',
            'seconds',
            'minutes',
            'hours',
            'days',
            'weeks',
            'months',
            'years'
        ]

    def name_change_litre(self):
        self.volume[3] = 'cubic decemetre'

    def set_volume(self):
        return self.volume[3]
    
    def set_time(self):
        return self.time[1]