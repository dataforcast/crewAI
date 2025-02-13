from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class CounterWordToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Text of words to be counted")

class CounterWordTool(BaseTool):
    name: str = "word counter"
    description: str = "Counts words in a text"
    args_schema: Type[BaseModel] = CounterWordToolInput

    def _run(self, argument: str) -> int:
        return len(argument.split())

class PercentToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    number1: int = Field(..., description="Represents the numerator of a ratio")
    number2: int = Field(..., description="Represents the denominator of a ratio")

class PercentWordTool(BaseTool):
    name: str = "word percentage"
    description: str = "Compute a percentage from two numbers number1*100/number2"
    args_schema: Type[BaseModel] = PercentToolInput

    def _run(self, number1: int, number2:int) -> float:
        return 100*number1/number2
