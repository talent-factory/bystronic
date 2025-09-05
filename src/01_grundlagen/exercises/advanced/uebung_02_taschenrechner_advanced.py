#!/usr/bin/env python3
"""
🔴 ADVANCED: Übung 2 - Mathematik-Engine mit Expression Parser
=============================================================

LERNZIELE:
- Expression Parsing und Evaluation
- Plugin-Architektur für erweiterbare Funktionen
- Performance-Benchmarking und Optimierung
- Umfassende Fehlerbehandlung und Logging
- Design Patterns (Strategy, Factory, Command)
- Unit Testing und Dokumentation

AUFGABE:
Entwickeln Sie eine vollständige Mathematik-Engine, die mathematische
Ausdrücke parsen und evaluieren kann, mit erweiterbarer Plugin-Architektur
und Performance-Optimierungen.

ZEIT: 45-60 Minuten
SCHWIERIGKEIT: 🔴 Experte

ANFORDERUNGEN:
- Expression Parser für komplexe mathematische Ausdrücke
- Plugin-System für erweiterbare Funktionen
- Performance-Benchmarking
- Umfassende Fehlerbehandlung
- Design Patterns
- Type Hints und Dokumentation
"""

import logging
import math
import operator
import time
from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from functools import wraps
from typing import Any, Protocol

# Logging konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TokenType(Enum):
    """Enum für Token-Typen im Expression Parser."""

    NUMBER = "NUMBER"
    OPERATOR = "OPERATOR"
    FUNCTION = "FUNCTION"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    COMMA = "COMMA"
    EOF = "EOF"


@dataclass
class Token:
    """Repräsentiert einen Token im mathematischen Ausdruck."""

    type: TokenType
    value: Any
    position: int


class MathError(Exception):
    """Basis-Exception für mathematische Fehler."""

    pass


class ParseError(MathError):
    """Exception für Parser-Fehler."""

    pass


class EvaluationError(MathError):
    """Exception für Evaluierungs-Fehler."""

    pass


def benchmark(func: Callable) -> Callable:
    """Decorator für Performance-Benchmarking."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000  # in Millisekunden
        logger.info(f"{func.__name__} executed in {execution_time:.3f}ms")
        return result

    return wrapper


class FunctionPlugin(Protocol):
    """Protocol für Funktions-Plugins."""

    def get_name(self) -> str:
        """Gibt den Namen der Funktion zurück."""
        ...

    def get_arity(self) -> int:
        """Gibt die Anzahl der erwarteten Argumente zurück."""
        ...

    def execute(self, *args: float) -> float:
        """Führt die Funktion aus."""
        ...

    def get_description(self) -> str:
        """Gibt eine Beschreibung der Funktion zurück."""
        ...


class BasicMathFunctions:
    """Sammlung von grundlegenden mathematischen Funktionen."""

    class SinFunction:
        def get_name(self) -> str:
            return "sin"

        def get_arity(self) -> int:
            return 1

        def execute(self, x: float) -> float:
            return math.sin(x)

        def get_description(self) -> str:
            return "Sinus-Funktion (Radiant)"

    class CosFunction:
        def get_name(self) -> str:
            return "cos"

        def get_arity(self) -> int:
            return 1

        def execute(self, x: float) -> float:
            return math.cos(x)

        def get_description(self) -> str:
            return "Cosinus-Funktion (Radiant)"

    class TanFunction:
        def get_name(self) -> str:
            return "tan"

        def get_arity(self) -> int:
            return 1

        def execute(self, x: float) -> float:
            return math.tan(x)

        def get_description(self) -> str:
            return "Tangens-Funktion (Radiant)"

    class LogFunction:
        def get_name(self) -> str:
            return "log"

        def get_arity(self) -> int:
            return 1

        def execute(self, x: float) -> float:
            if x <= 0:
                raise EvaluationError(
                    "Logarithmus ist nur für positive Zahlen definiert"
                )
            return math.log10(x)

        def get_description(self) -> str:
            return "Logarithmus zur Basis 10"

    class LnFunction:
        def get_name(self) -> str:
            return "ln"

        def get_arity(self) -> int:
            return 1

        def execute(self, x: float) -> float:
            if x <= 0:
                raise EvaluationError(
                    "Natürlicher Logarithmus ist nur für positive Zahlen definiert"
                )
            return math.log(x)

        def get_description(self) -> str:
            return "Natürlicher Logarithmus"

    class SqrtFunction:
        def get_name(self) -> str:
            return "sqrt"

        def get_arity(self) -> int:
            return 1

        def execute(self, x: float) -> float:
            if x < 0:
                raise EvaluationError("Quadratwurzel aus negativer Zahl nicht möglich")
            return math.sqrt(x)

        def get_description(self) -> str:
            return "Quadratwurzel"

    class AbsFunction:
        def get_name(self) -> str:
            return "abs"

        def get_arity(self) -> int:
            return 1

        def execute(self, x: float) -> float:
            return abs(x)

        def get_description(self) -> str:
            return "Absolutwert"

    class PowFunction:
        def get_name(self) -> str:
            return "pow"

        def get_arity(self) -> int:
            return 2

        def execute(self, base: float, exponent: float) -> float:
            return math.pow(base, exponent)

        def get_description(self) -> str:
            return "Potenz-Funktion pow(base, exponent)"

    class MaxFunction:
        def get_name(self) -> str:
            return "max"

        def get_arity(self) -> int:
            return 2

        def execute(self, a: float, b: float) -> float:
            return max(a, b)

        def get_description(self) -> str:
            return "Maximum von zwei Zahlen"

    class MinFunction:
        def get_name(self) -> str:
            return "min"

        def get_arity(self) -> int:
            return 2

        def execute(self, a: float, b: float) -> float:
            return min(a, b)

        def get_description(self) -> str:
            return "Minimum von zwei Zahlen"


class Lexer:
    """Lexikalischer Analyzer für mathematische Ausdrücke."""

    def __init__(self, expression: str):
        self.expression = expression.replace(" ", "")  # Entferne Leerzeichen
        self.position = 0
        self.current_char = self.expression[0] if expression else None

    def advance(self) -> None:
        """Bewegt den Zeiger zum nächsten Zeichen."""
        self.position += 1
        if self.position >= len(self.expression):
            self.current_char = None
        else:
            self.current_char = self.expression[self.position]

    def peek(self, offset: int = 1) -> str | None:
        """Schaut voraus ohne den Zeiger zu bewegen."""
        peek_pos = self.position + offset
        if peek_pos >= len(self.expression):
            return None
        return self.expression[peek_pos]

    def read_number(self) -> float:
        """Liest eine Zahl (int oder float)."""
        num_str = ""
        while self.current_char is not None and (
            self.current_char.isdigit() or self.current_char == "."
        ):
            num_str += self.current_char
            self.advance()

        try:
            return float(num_str)
        except ValueError:
            raise ParseError(f"Ungültige Zahl: {num_str}")

    def read_identifier(self) -> str:
        """Liest einen Bezeichner (Funktionsname)."""
        identifier = ""
        while self.current_char is not None and (
            self.current_char.isalnum() or self.current_char == "_"
        ):
            identifier += self.current_char
            self.advance()
        return identifier

    def get_next_token(self) -> Token:
        """Gibt das nächste Token zurück."""
        while self.current_char is not None:
            if self.current_char.isdigit() or self.current_char == ".":
                return Token(TokenType.NUMBER, self.read_number(), self.position)

            elif self.current_char.isalpha():
                identifier = self.read_identifier()
                return Token(TokenType.FUNCTION, identifier, self.position)

            elif self.current_char in "+-*/^%":
                token = Token(TokenType.OPERATOR, self.current_char, self.position)
                self.advance()
                return token

            elif self.current_char == "(":
                token = Token(TokenType.LPAREN, self.current_char, self.position)
                self.advance()
                return token

            elif self.current_char == ")":
                token = Token(TokenType.RPAREN, self.current_char, self.position)
                self.advance()
                return token

            elif self.current_char == ",":
                token = Token(TokenType.COMMA, self.current_char, self.position)
                self.advance()
                return token

            else:
                raise ParseError(
                    f"Unbekanntes Zeichen: {self.current_char} an Position {self.position}"
                )

        return Token(TokenType.EOF, None, self.position)


class ExpressionParser:
    """Parser für mathematische Ausdrücke mit Operator-Precedence."""

    def __init__(self, lexer: Lexer, function_registry: dict[str, FunctionPlugin]):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        self.function_registry = function_registry

        # Operator-Precedence (höhere Zahl = höhere Priorität)
        self.precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 3}

        # Operator-Funktionen
        self.operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "%": operator.mod,
            "^": operator.pow,
        }

    def eat(self, token_type: TokenType) -> None:
        """Konsumiert ein Token des erwarteten Typs."""
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise ParseError(
                f"Erwarteter Token-Typ {token_type}, erhalten {self.current_token.type}"
            )

    def factor(self) -> float:
        """Parst Faktoren (Zahlen, Funktionen, Klammern)."""
        token = self.current_token

        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return token.value

        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            result = self.expression()
            self.eat(TokenType.RPAREN)
            return result

        elif token.type == TokenType.FUNCTION:
            return self.function_call()

        elif token.type == TokenType.OPERATOR and token.value == "-":
            # Unäres Minus
            self.eat(TokenType.OPERATOR)
            return -self.factor()

        elif token.type == TokenType.OPERATOR and token.value == "+":
            # Unäres Plus
            self.eat(TokenType.OPERATOR)
            return self.factor()

        else:
            raise ParseError(f"Unerwarteter Token: {token.value}")

    def function_call(self) -> float:
        """Parst Funktionsaufrufe."""
        func_name = self.current_token.value
        self.eat(TokenType.FUNCTION)

        if func_name not in self.function_registry:
            raise ParseError(f"Unbekannte Funktion: {func_name}")

        function = self.function_registry[func_name]

        self.eat(TokenType.LPAREN)

        # Sammle Argumente
        args = []
        if self.current_token.type != TokenType.RPAREN:
            args.append(self.expression())

            while self.current_token.type == TokenType.COMMA:
                self.eat(TokenType.COMMA)
                args.append(self.expression())

        self.eat(TokenType.RPAREN)

        # Prüfe Anzahl der Argumente
        if len(args) != function.get_arity():
            raise ParseError(
                f"Funktion {func_name} erwartet {function.get_arity()} Argumente, erhalten {len(args)}"
            )

        try:
            return function.execute(*args)
        except Exception as e:
            raise EvaluationError(f"Fehler bei Ausführung von {func_name}: {e}")

    def term(self) -> float:
        """Parst Terme (Multiplikation, Division, Modulo)."""
        result = self.factor()

        while (
            self.current_token.type == TokenType.OPERATOR
            and self.current_token.value in ["*", "/", "%"]
        ):
            op = self.current_token.value
            self.eat(TokenType.OPERATOR)

            if (
                op == "/"
                and self.current_token.type == TokenType.NUMBER
                and self.current_token.value == 0
            ):
                raise EvaluationError("Division durch Null")

            right = self.factor()
            result = self.operators[op](result, right)

        return result

    def expression(self) -> float:
        """Parst Ausdrücke (Addition, Subtraktion, Potenz)."""
        result = self.term()

        while (
            self.current_token.type == TokenType.OPERATOR
            and self.current_token.value in ["+", "-", "^"]
        ):
            op = self.current_token.value
            self.eat(TokenType.OPERATOR)
            right = self.term()
            result = self.operators[op](result, right)

        return result

    def parse(self) -> float:
        """Parst den kompletten Ausdruck."""
        result = self.expression()
        if self.current_token.type != TokenType.EOF:
            raise ParseError("Unerwartete Zeichen am Ende des Ausdrucks")
        return result


class MathEngine:
    """Hauptklasse der Mathematik-Engine."""

    def __init__(self):
        self.function_registry: dict[str, FunctionPlugin] = {}
        self.constants: dict[str, float] = {"pi": math.pi, "e": math.e, "tau": math.tau}
        self.history: list[str] = []

        # Registriere Standard-Funktionen
        self._register_standard_functions()

    def _register_standard_functions(self) -> None:
        """Registriert alle Standard-Funktionen."""
        functions = [
            BasicMathFunctions.SinFunction(),
            BasicMathFunctions.CosFunction(),
            BasicMathFunctions.TanFunction(),
            BasicMathFunctions.LogFunction(),
            BasicMathFunctions.LnFunction(),
            BasicMathFunctions.SqrtFunction(),
            BasicMathFunctions.AbsFunction(),
            BasicMathFunctions.PowFunction(),
            BasicMathFunctions.MaxFunction(),
            BasicMathFunctions.MinFunction(),
        ]

        for func in functions:
            self.register_function(func)

    def register_function(self, function: FunctionPlugin) -> None:
        """Registriert eine neue Funktion."""
        self.function_registry[function.get_name()] = function
        logger.info(f"Funktion '{function.get_name()}' registriert")

    def preprocess_expression(self, expression: str) -> str:
        """Vorverarbeitung des Ausdrucks (Konstanten ersetzen)."""
        for name, value in self.constants.items():
            expression = expression.replace(name, str(value))
        return expression

    @benchmark
    def evaluate(self, expression: str) -> float:
        """
        Evaluiert einen mathematischen Ausdruck.

        Args:
            expression: Mathematischer Ausdruck als String

        Returns:
            Ergebnis der Berechnung

        Raises:
            ParseError: Bei Syntax-Fehlern
            EvaluationError: Bei mathematischen Fehlern
        """
        try:
            # Vorverarbeitung
            processed_expr = self.preprocess_expression(expression)

            # Lexing und Parsing
            lexer = Lexer(processed_expr)
            parser = ExpressionParser(lexer, self.function_registry)

            # Evaluation
            result = parser.parse()

            # Zur Historie hinzufügen
            self.history.append(f"{expression} = {result}")

            return result

        except (ParseError, EvaluationError) as e:
            logger.error(f"Fehler bei Evaluation von '{expression}': {e}")
            raise
        except Exception as e:
            logger.error(f"Unerwarteter Fehler: {e}")
            raise EvaluationError(f"Unerwarteter Fehler: {e}")

    def get_available_functions(self) -> dict[str, str]:
        """Gibt alle verfügbaren Funktionen mit Beschreibungen zurück."""
        return {
            name: func.get_description()
            for name, func in self.function_registry.items()
        }

    def get_history(self) -> list[str]:
        """Gibt die Berechnungshistorie zurück."""
        return self.history.copy()

    def clear_history(self) -> None:
        """Löscht die Historie."""
        self.history.clear()


class MathEngineInterface:
    """Benutzeroberfläche für die Mathematik-Engine."""

    def __init__(self):
        self.engine = MathEngine()

    def show_help(self) -> None:
        """Zeigt Hilfe und verfügbare Funktionen an."""
        print("\n" + "=" * 60)
        print("📚 HILFE - MATHEMATIK-ENGINE")
        print("=" * 60)

        print("\nVERFÜGBARE FUNKTIONEN:")
        print("-" * 30)
        functions = self.engine.get_available_functions()
        for name, description in sorted(functions.items()):
            print(f"  {name:8} - {description}")

        print("\nKONSTANTEN:")
        print("-" * 15)
        print("  pi       - π (3.14159...)")
        print("  e        - Eulersche Zahl (2.71828...)")
        print("  tau      - τ = 2π (6.28318...)")

        print("\nOPERATOREN:")
        print("-" * 15)
        print("  +, -, *, /, %, ^")
        print("  Klammern: ( )")

        print("\nBEISPIELE:")
        print("-" * 12)
        print("  2 + 3 * 4")
        print("  sin(pi/2)")
        print("  sqrt(16) + log(100)")
        print("  pow(2, 8)")
        print("  max(5, min(10, 7))")
        print("=" * 60)

    def show_history(self) -> None:
        """Zeigt die Berechnungshistorie an."""
        history = self.engine.get_history()
        if not history:
            print("📝 Historie ist leer.")
            return

        print("\n📜 BERECHNUNGSHISTORIE:")
        print("-" * 40)
        for i, entry in enumerate(history, 1):
            print(f"{i:2d}. {entry}")
        print("-" * 40)

    def run(self) -> None:
        """Hauptschleife der Anwendung."""
        print("🔬 MATHEMATIK-ENGINE MIT EXPRESSION PARSER")
        print("=" * 50)
        print("Geben Sie mathematische Ausdrücke ein.")
        print("Befehle: 'help', 'history', 'clear', 'quit'")
        print("=" * 50)

        while True:
            try:
                expression = input("\n🧮 Ausdruck: ").strip()

                if not expression:
                    continue

                elif expression.lower() == "quit":
                    break

                elif expression.lower() == "help":
                    self.show_help()

                elif expression.lower() == "history":
                    self.show_history()

                elif expression.lower() == "clear":
                    self.engine.clear_history()
                    print("🗑️ Historie geleert.")

                else:
                    result = self.engine.evaluate(expression)
                    print(f"➡️  {result}")

            except (ParseError, EvaluationError) as e:
                print(f"❌ {e}")
            except KeyboardInterrupt:
                print("\n\n⚠️ Programm abgebrochen.")
                break
            except Exception as e:
                print(f"❌ Unerwarteter Fehler: {e}")

        print("\n🎉 Vielen Dank für die Nutzung der Mathematik-Engine!")


def main():
    """Hauptfunktion."""
    interface = MathEngineInterface()
    interface.run()


if __name__ == "__main__":
    main()

"""
ERWARTETE AUSGABE:
==================
🔬 MATHEMATIK-ENGINE MIT EXPRESSION PARSER
==================================================
Geben Sie mathematische Ausdrücke ein.
Befehle: 'help', 'history', 'clear', 'quit'
==================================================

🧮 Ausdruck: 2 + 3 * 4
➡️  14.0

🧮 Ausdruck: sin(pi/2)
➡️  1.0

🧮 Ausdruck: sqrt(pow(3, 2) + pow(4, 2))
➡️  5.0

🧮 Ausdruck: help

============================================================
📚 HILFE - MATHEMATIK-ENGINE
============================================================

VERFÜGBARE FUNKTIONEN:
------------------------------
  abs      - Absolutwert
  cos      - Cosinus-Funktion (Radiant)
  ln       - Natürlicher Logarithmus
  log      - Logarithmus zur Basis 10
  max      - Maximum von zwei Zahlen
  min      - Minimum von zwei Zahlen
  pow      - Potenz-Funktion pow(base, exponent)
  sin      - Sinus-Funktion (Radiant)
  sqrt     - Quadratwurzel
  tan      - Tangens-Funktion (Radiant)

[... weitere Ausgabe ...]

LERNKONTROLLE:
==============
□ Verstehe ich Expression Parsing?
□ Kann ich Plugin-Architekturen implementieren?
□ Beherrsche ich Design Patterns?
□ Kann ich Performance-Benchmarking durchführen?
□ Verstehe ich umfassende Fehlerbehandlung?
□ Kann ich erweiterbare Systeme entwickeln?
"""
