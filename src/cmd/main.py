from usecases.calculation_usecase import CalculationUseCase


class Main():

    def __init__(self):

        self.calculation = CalculationUseCase(1, 2)
        print(self.calculation.get_product())


main = Main()
