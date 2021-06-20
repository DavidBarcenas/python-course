class VotingBox:
    def __init__(self, id, country) -> None:
        self._id = id
        self._country: country
        self._region = None

    @property
    def region(self):
        return self._region

    @property.setter
    def region(self, region):
        if region in self._country:
            self._region = region
        else:
            raise ValueError(f'The region {region} is not valid in {self._country}')


if __name__ == '__main__':
    box = VotingBox(123, ['Mexico city', 'Monterrey'])