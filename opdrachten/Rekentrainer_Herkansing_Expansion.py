#!/usr/bin/env python
# -*- coding: utf-8 -*-

import builtins
import collections
import json
import random
import re
import sys
import traceback

"""
Programming
Opdracht PROG: Rekentrainer in de herkansing
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
    resultaten.json toegevoegd, gescheiden door puntkomma's. Stel dat het bestand eerst de lege lijst [ ] bevat,
    dan zal het na het bovenstaande voorbeeld (helemaal links) er zo uitzien::

    [
        { "a": 9, "op": "*", "b": 0, "correct": 0, "uw_antwoord": "9", "uitslag": "fout" },
        { "a": 3, "op": "*", "b": 1, "correct": 3, "uw_antwoord": "3", "uitslag": "goed" },
        { "a": 8, "op": "*", "b": 3, "correct": 24, "uw_antwoord": "24", "uitslag": "goed" }
    ]

    Returns:
        int: het aantal correct gegeven antwoorden
    """
    return


def herkansen():
    """
    Het bestand wordt geheel als JSON gelezen, en de lijst met sommen wordt één voor één langsgelopen.
    Bij een fout antwoord wordt de som nogmaals aan de gebruiker getoond, en kan deze een antwoord
    invoeren. De som-dictionary wordt bijgewerkt met het nieuwe antwoord en bijbehorende uitslag. Overschrijf
    resultaten.json met de nieuwe lijst, en return het aantal goede antwoorden (als een int).

    Returns:
        int: het aantal (correct) verbeterde antwoorden
    """
    return


def reset():
    """
    Maakt het bestand resultaten.json leeg.

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
    return "testresultaten.json"


def __create_test_file(sums, testfile=__my_test_file()):
    som_mv_ev = 'som' if len(sums) == 1 else 'sommen'
    print(f"Voor testdoeleinden wordt bestand {testfile} aangemaakt met {len(sums)} {som_mv_ev}... ", end="")

    try:
        sommen = []

        for number_one, operator, number_two, result, answer, verdict in sums:
            sommen.append({'a': number_one, 'op': operator, 'b': number_two,
                           'correct': result, 'uw_antwoord': str(answer), 'uitslag': verdict})

        with open(testfile, 'w') as dummy_file:
            json.dump(sommen, dummy_file, indent=2)
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


def __to_number(input_str):
    try:
        return int(input_str)
    except:
        return float(input_str)

def __create_fake_input(buffer, give_right_answers=True):
    def fake_input(prompt=""):
        print(prompt, end="", flush=True)

        new_sum = buffer.get_last_sum()
        getal1 = __to_number(new_sum[0])
        bewerking = new_sum[1]
        getal2 = __to_number(new_sum[2])

        outcome = eval(f'{getal1} {bewerking} {getal2}')
        my_answer = outcome

        new_record = {'a': getal1, 'op': bewerking, 'b': getal2,
                      'correct': outcome, 'uw_antwoord': str(my_answer), 'uitslag': 'goed'}

        if not give_right_answers:
            my_answer += 1
            new_record['uw_antwoord'] = str(my_answer)
            new_record['uitslag'] = 'fout'

        buffer.expected_sum_records.append(new_record)

        print(my_answer)        # Print answer to test-output
        buffer.clear_buffer()   # Remove answer from buffer to avoid problems with the next sum

        return str(my_answer)

    return fake_input


def test_rekensessie():
    function = rekensessie

    case = collections.namedtuple('case', 'operator sum_count min max give_right_answers')
    testcases = [
        case('*', 3, 0, 10, True),
        case('+', 3, 0, 10, False),
        case('*', 8, 0, 10, True),
        case('-', 8, 0, 10, False)
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

            function_report = json.load(open(__my_test_file()))
            for record in io_buffer.expected_sum_records:
                assert record in function_report, f'{record} verwacht maar niet aangetroffen in rapportbestand!'

        finally:
            builtins.open = original_open
            builtins.print = original_print
            builtins.input = original_input


def test_herkansen():
    function = herkansen

    test_sums = [
        [2, '*', 8, 16, "17", 'fout'],
        [2, '-', 8, -6, "-6", 'goed'],
        [2, '+', 10, 12, "17", 'fout'],
    ]

    for give_right_answers in [True, False]:
        __create_test_file(test_sums)
        io_buffer = IOBuffer()

        original_open = builtins.open
        original_print = builtins.print
        original_input = builtins.input

        builtins.open = __create_fake_open(original_open)
        builtins.print = __create_fake_print(original_print, io_buffer)
        builtins.input = __create_fake_input(io_buffer, give_right_answers)

        try:
            expected_corrections = sum(1 for s in test_sums if s[5] == 'fout') if give_right_answers else 0

            __my_assert_args(function, tuple(), expected_corrections, check_type=True)

            builtins.open = original_open
            builtins.print = original_print
            builtins.input = original_input

            function_report = json.load(open(__my_test_file()))
            for testsum in test_sums:
                sum_original = {'a': testsum[0], 'op': testsum[1], 'b': testsum[2],
                                'correct': testsum[3], 'uw_antwoord': testsum[4], 'uitslag': testsum[5]}

                sum_corrected = sum_original.copy()
                sum_corrected.update({'uw_antwoord': str(testsum[3]), 'uitslag': 'goed'})

                if sum_original['uitslag'] == 'fout':
                    if give_right_answers:
                        assert sum_original not in function_report, f'{sum_original} niet verwacht maar wel aangetroffen in rapportbestand!'
                        assert sum_corrected in function_report, f'{sum_corrected} verwacht maar niet aangetroffen in rapportbestand!'
                    else:
                        assert sum_corrected not in function_report, f'{sum_corrected} niet verwacht maar wel aangetroffen in rapportbestand!'

                else:
                    assert sum_original in function_report, f'{sum_original} verwacht maar niet aangetroffen in rapportbestand!'

        finally:
            builtins.open = original_open
            builtins.print = original_print
            builtins.input = original_input


def test_reset():
    function = reset

    test_sums = [
        [2, '*', 8, 16, "17", 'fout'],
        [2, '-', 8, -6, "-6", 'goed'],
        [2, '+', 10, 12, "17", 'fout'],
    ]

    __create_test_file(test_sums)
    original_open = builtins.open

    try:
        builtins.open = __create_fake_open(original_open)

        function()

        # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
        data = None
        with open(__my_test_file()) as testfile:
            data = testfile.read()

        try:
            with open(__my_test_file()) as testfile:
                data = json.load(testfile)
        except :
            pass


        assert data == [], f"Fout: {function.__name__}() maakt het resultatenbestand niet gelijk aan []!"

    finally:
        builtins.open = original_open

def __run_tests():
    with open(__my_test_file(), "w") as bestand:
        json.dump([], bestand)

    """ Test alle functies. """
    test_functions = [test_rekensessie,
                      test_herkansen,
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