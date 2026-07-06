#!/usr/bin/env python
# -*- coding: utf-8 -*-

import builtins
import collections
import random
import re
import sys
import traceback

"""
Programming
Opdracht PROG: Rekentrainer
(c) 2026 Hogeschool Utrecht,
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
Lever je werk in op Canvas als alle tests slagen.
"""


def rekensessie(bewerking, aantal, min, max):
    """
    Deze functie genereert aantal keer een willekeurige rekensom, waarbij twee getallen worden gegenereerd
    van min t/m max. De functie rekent zelf het antwoord van de bewerking ("+", "-" of "*") uit, en vraagt
    de gebruiker ook om een antwoord. Daarna controleert de functie of de gebruiker goed heeft geantwoord.

    De som, het correcte antwoord, het gegeven antwoord en de uitkomst worden direct aan het bestand
    resultaten.txt toegevoegd, gescheiden door puntkomma's. Stel dat het bestand eerst leeg is, dan zal het
    na het bovenstaande voorbeeld (helemaal links) er zo uitzien:

        9;*;0;0;9;fout
        3;*;1;3;3;goed
        8;*;3;24;24;goed

    Returns:
        int: het aantal correct gegeven antwoorden
    """
    return


def foutrapport():
    """
    Alle regels van het bestand worden één voor één gelezen. Voor elk verkeerd gegeven antwoord moet een
    foutmelding opgesteld worden. Voorbeeld: als op de som 9 * 0 het antwoord 9 is gegeven, is de foutmelding:

        9 * 0 is helaas geen 9

    Returns:
        list: een lijst met alle opgestelde foutmeldingen (strings)
    """
    return


def reset():
    """
    Maakt het bestand resultaten.txt leeg.

    Returns:
        None
    """
    return


def main():
    # Breid deze code uit om het keuzemenu te realiseren:
    print("1: Nieuwe rekensessie")


def module_runner():
    main()              # Comment deze regel om je 'main() functie' uit te schakelen
    __run_tests()       # Comment deze regel om de HU-tests uit te schakelen


"""
==========================[ HU TESTRAAMWERK ]================================
Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
"""

def __my_assert_args(function, args, expected_output, check_type=False):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output).__name__} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    if str(expected_output) == str(output):
        msg = f"Fout: {function.__name__}{argstr} geeft {output} ({type(output).__name__}) " \
              f"in plaats van {expected_output} (type {type(expected_output).__name__})"
    else:
        msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"

    if type(expected_output) is float and isinstance(output, (int, float, complex)):
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def __out_of_input_error():
    raise AssertionError("Fout: er werd in de functie vaker om input gevraagd dan verwacht.")


def __my_test_file():
    return "testresultaten.txt"


def __create_test_file(sums, testfile=__my_test_file()):
    som_mv_ev = 'som' if len(sums) == 1 else 'sommen'
    print(f"Voor testdoeleinden wordt bestand {testfile} aangemaakt met {len(sums)} {som_mv_ev}... ", end="")

    try:
        with open(testfile, 'w') as dummy_file:
            for number_one, operator, number_two, result, answer, verdict in sums:
                dummy_file.write(f"{number_one};{operator};{number_two};{result};{answer};{verdict}\n")
    except:
        print(f"\nFout: bestand {testfile} kon niet worden aangemaakt. Python-error:")
        print(traceback.format_exc())
        sys.exit()

    print("Klaar.")


class IOBuffer:
    def __init__(self):
        self.value = ""
        self.expected_sum_records = []

    def append(self, text):
        self.value += text

    def get_last_sum(self):
        pattern = re.compile(r"""
            (-?(?:\d+(?:\.\d+)?|\.\d+))   # eerste getal
            .*?                           # willekeurige tekst ertussen
            ([+\-*/])                     # operator
            .*?                           # willekeurige tekst ertussen
            (-?(?:\d+(?:\.\d+)?|\.\d+))   # tweede getal
        """, re.VERBOSE)

        matches = pattern.findall(self.value)
        if len(matches) == 0:
            raise IOError('Er werd in je functie om invoer gevraagd, maar er is in de geprinte tekst geen som gevonden!')

        return matches[-1]

    def clear_buffer(self):
        self.value = ""

def __create_fake_open(original_open):
    def fake_open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        return original_open(__my_test_file(), mode=mode, buffering=buffering, encoding=encoding, errors=errors,
                      newline=newline, closefd=closefd, opener=opener)
    return fake_open


def __create_fake_print(original_print, buffer):
    def fake_print(*args, sep=' ', end='\n', file=None, flush=True):
        buffer.append(sep.join([str(arg) for arg in args]) + end)
        original_print(*args, sep=' ', end='\n', file=None)
    return fake_print


def __create_fake_input(buffer, give_right_answers=True):
    def fake_input(prompt=""):
        print(prompt, end="", flush=True)

        new_sum = buffer.get_last_sum()
        getal1 = new_sum[0]
        bewerking = new_sum[1]
        getal2 = new_sum[2]

        outcome = eval(f'{getal1} {bewerking} {getal2}')
        my_answer = outcome
        new_record = f'{getal1};{bewerking};{getal2};{outcome};{my_answer};goed'

        if not give_right_answers:
            my_answer += 1
            new_record = f'{getal1};{bewerking};{getal2};{outcome};{my_answer};fout'

        buffer.expected_sum_records.append(new_record)

        print(my_answer)        # Print answer to test-output
        buffer.clear_buffer()   # Remove answer from buffer to avoid problems with the next sum

        return str(my_answer)

    return fake_input


def test_rekensessie():
    function = rekensessie

    case = collections.namedtuple('case', 'operator sum_count level min max give_right_answers')
    testcases = [
        case('*', 3, 'makkelijk', 0, 10, True),
        case('+', 3, 'makkelijk', 0, 10, False),
        case('*', 8, 'moeilijk', -10, 100, True),
        case('-', 8, 'moeilijk', -10, 100, False)
    ]

    for test in testcases:
        io_buffer = IOBuffer()

        original_open = builtins.open
        original_print = builtins.print
        original_input = builtins.input

        builtins.open = __create_fake_open(original_open)
        builtins.print = __create_fake_print(original_print, io_buffer)
        builtins.input = __create_fake_input(io_buffer, test.give_right_answers)

        try:
            right_answers_expected = test.sum_count if test.give_right_answers else 0
            __my_assert_args(function, (test.operator, test.sum_count, test.min, test.max), right_answers_expected, check_type=True)

            builtins.open = original_open
            builtins.print = original_print
            builtins.input = original_input

            function_report = open(__my_test_file()).read()
            for record in io_buffer.expected_sum_records:
                assert record in function_report, f'{record} verwacht maar niet aangetroffen in rapportbestand!'

        finally:
            builtins.open = original_open
            builtins.print = original_print
            builtins.input = original_input


def test_foutrapport():
    function = foutrapport

    test_sums = [
        [2, '*', 8, 16, 17, 'fout'],
        [2, '-', 8, -6, -6, 'goed'],
        [2, '+', 10, 12, 17, 'fout'],
    ]

    __create_test_file(test_sums)

    try:
        original_open = builtins.open
        builtins.open = __create_fake_open(original_open)

        report = function()

        msg = f"Fout: {function.__name__}() geeft geen list terug als return-type"
        assert type(report) is list, msg

        # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
        for my_sum in test_sums:
            if my_sum[5] == 'fout':

                pattern = rf"(?=.*{my_sum[0]})(?=.*{my_sum[2]})(?=.*{my_sum[4]})"
                matches = [line for line in report if re.compile(pattern).search(line)]

                msg = (f"{my_sum[0]} {my_sum[1]} {my_sum[2]} met als antwoord {my_sum[4]} is {my_sum[5]}, "
                       f"maar er werd geen regel met deze getallen gevonden in het foutrapport: {report}")
                assert len(matches) > 0, msg

    finally:
        builtins.open = original_open


def test_reset():
    function = reset

    test_sums = [
        [2, '*', 8, 16, 17, 'fout'],
        [2, '-', 8, -6, -6, 'goed'],
        [2, '+', 10, 12, 17, 'fout'],
    ]

    __create_test_file(test_sums)

    try:
        original_open = builtins.open
        builtins.open = __create_fake_open(original_open)

        function()

        # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
        with open(__my_test_file()) as testfile:
            assert len(testfile.readlines()) == 0, f"Fout: {function.__name__}() maakt het resultatenbestand niet leeg!"

    finally:
        builtins.open = original_open

def __run_tests():
    """ Test alle functies. """
    test_functions = [test_rekensessie,
                      test_foutrapport,
                      test_reset,
                     ]

    try:
        for test_function in test_functions:
            func_name = test_function.__name__[5:]

            print(f"\n======= Test output '{test_function.__name__}()' =======")
            test_function()
            print(f"Je functie {func_name} werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as e:
        print(e.args[0])
    except Exception as e:
        print(f"Fout: er ging er iets mis! Python-error: \"{e}\"")
        print(traceback.format_exc())


if __name__ == '__main__':
    module_runner()