from __future__ import annotations

import sys
from abc import ABC, abstractmethod


class Context:
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        print(f"Context: Переключаемся в {type(state).__name__}")
        self._state = state
        self._state.context = self

    def make_response(self, data):
        self._state.make_response(data)

    def handle_answer(self, data):
        self._state.handle_answer(data)


class State(ABC):

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def make_response(self, data) -> None:
        pass

    @abstractmethod
    def handle_answer(self, data) -> None:
        pass


class HelloState(State):
    def make_response(self, data) -> None:
        print("Привет, представься, пожалуйста")

    def handle_answer(self, data) -> None:
        if "Помощь" in data:
            self.context.transition_to(HelpState())
        else:
            self.context.transition_to(RepeaterState())


class HelpState(State):
    def make_response(self, data) -> None:
        print("Это помощь :)")

    def handle_answer(self, data) -> None:
        self.context.transition_to(RepeaterState())


class RepeaterState(State):
    def make_response(self, data) -> None:
        print(f"Я повторю, все что ты скажешь: {data}")

    def handle_answer(self, data) -> None:
        if "Помощь" in data:
            self.context.transition_to(HelpState())
        elif "Выход" in data:
            self.context.transition_to(ExitState())


class ExitState(State):
    def make_response(self, data) -> None:
        print("Пока-пока")
        sys.exit(0)

    def handle_answer(self, data) -> None:
        pass


if __name__ == "__main__":
    context = Context(HelloState())
    data = None
    while True:
        context.make_response(data)
        data = input()
        context.handle_answer(data)
