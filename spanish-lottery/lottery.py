# coding: utf-8
from typer import Typer, Option
from random import sample
from trogon import tui
from assets.ascii_art import AsciiTitle


app = Typer()


# This class defines two methods for generating random lottery numbers for Eurodreams and Bonoloto
# games.
class Lottery:
    def eurodreams(self):
        """
        The function generates a list of unique random numbers from a specified population range, along
        with an additional random number.
        :return: The function `eurodreams` returns a string that contains a sorted sample of 6 random
        numbers from the population range 1 to 40, along with one additional random number from the
        range 1 to 6 labeled as "sueño".
        """
        sample_size = 6
        population = range(1, 41)
        sueño = sample(range(1, 6), 1)
        unique_random_numbers_mas_sueño = f"""
            -----------------------------------------
            PLAY: {sorted(sample(population, sample_size))}, sueño:{sueño}
            -----------------------------------------
            """
        title = AsciiTitle.eurodreams()
        print(title)
        return unique_random_numbers_mas_sueño

    def bonoloto(self):
        """
        The function generates a random set of 6 unique numbers between 1 and 49 for a Bonoloto lottery
        ticket.
        :return: Numbers: [7, 15, 23, 31, 38, 45]
        """
        sample_size = 6
        population = range(1, 50)
        # unique_random_numbers = sample(population, sample_size)
        unique_random_numbers = f"""
            ------------------------------
            PLAY: {sorted(sample(population, sample_size))}
            ------------------------------
            """
        title = AsciiTitle.bonoloto()
        print(title)
        return unique_random_numbers

    def euromillones(self):
        """
        This Python function generates a random selection of 5 numbers from 1 to 50 and 2 "estrellas"
        (stars) from 1 to 12 for the Euromillones lottery.
        :return: The function `euromillones` returns a string that contains a sorted list of 5 unique random
        numbers between 1 and 50, along with 2 random numbers (estrellas) between 1 and 12. The format of
        the returned string is: "sorted list of 5 unique random numbers, estrellas: [two random numbers]".
        """
        sample_size = 5
        population = range(1, 51)
        estrellas = sample(range(1, 13), 2)
        # unique_random_numbers_mas_estrellas = (
        #     f"{sorted(sample(population, sample_size))}, estrellas:{estrellas}"
        # )
        unique_random_numbers_mas_estrellas = f"""
            --------------------------------------------
            PLAY: {sorted(sample(population, sample_size))}, estrellas:{estrellas}
            --------------------------------------------
            """
        title = AsciiTitle.euromillones()
        print(title)
        return unique_random_numbers_mas_estrellas

    def primitiva(self):
        sample_size = 6
        population = range(1, 50)
        unique_random_numbers = f"""
            --------------------------------------------
            PLAY: {sorted(sample(population, sample_size))}
            --------------------------------------------
            """
        title = AsciiTitle.primitiva()
        print(title)
        return unique_random_numbers

    def gordo_primitiva(self):
        sample_size = 5
        population = range(1, 55)
        no_clave = sample(range(0, 10), 1)
        unique_random_numbers = f"""
            --------------------------------------------
            PLAY: {sorted(sample(population, sample_size))}, número clave:{no_clave}
            --------------------------------------------
            """
        title = AsciiTitle.gordo_primitiva()
        print(title)
        return unique_random_numbers


@tui
@app.command()
def eurodreams(
    times: int = Option(None, help="Number of times to run the EuroDreams function"),
):
    if times is None:
        times = 1  # Default to running once if no value is provided
    lottery = Lottery()
    for _ in range(times):
        print(lottery.eurodreams())


@tui
@app.command()
def bonoloto(
    times: int = Option(None, help="Number of times to run the Bonoloto generator"),
):
    if times is None:
        times = 1  # Default to running once if no value is provided
    lottery = Lottery()
    for _ in range(times):
        print(lottery.bonoloto())


@tui
@app.command()
def euromillones(
    times: int = Option(None, help="Number of times to run the Euromillones generator"),
):
    if times is None:
        times = 1  # Default to running once if no value is provided
    lottery = Lottery()
    for _ in range(times):
        print(lottery.euromillones())


@tui
@app.command()
def primitiva(
    times: int = Option(None, help="Number of times to run the Primitiva generator"),
):
    if times is None:
        times = 1  # Default to running once if no value is provided
    lottery = Lottery()
    for _ in range(times):
        print(lottery.primitiva())


@tui
@app.command()
def gordo_primitiva(
    times: int = Option(
        None, help="Number of times to run the Gordo_Primitiva generator"
    ),
):
    if times is None:
        times = 1  # Default to running once if no value is provided
    lottery = Lottery()
    for _ in range(times):
        print(lottery.gordo_primitiva())


if __name__ == "__main__":
    app()

