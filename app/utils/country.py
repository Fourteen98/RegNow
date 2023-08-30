import pycountry

class Country(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if value not in [country.alpha_2 for country in pycountry.countries]:
            raise ValueError('Invalid country code')
        return value
