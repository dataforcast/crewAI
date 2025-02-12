from pydantic import BaseModel, Field
from typing import Type
from crewai import Agent, Crew, Process, Task
from crewai.tools import BaseTool

from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff


# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

class Abstract(BaseModel):
    title: str
    content: str


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


counter_word_tool = CounterWordTool()
percent_tool = PercentWordTool()

@CrewBase
class Summarizer():
    """Summarizer crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @before_kickoff
    def before_kickoff_function(self, inputs):
        print(f"Before kickoff function with inputs: {inputs}")
        return inputs  # You can return the inputs or modify them as needed

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def string_to_period_converter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['string_to_period_converter_agent'],
            verbose=True
        )

    @agent
    def summarizer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer_agent'],
            tools=[counter_word_tool, percent_tool,],
            verbose=True,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def summarizer_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarizer_task'],
            output_file='summarizer_task.txt',
            output_pydantic=Abstract,
        )

    @task
    def string_to_period_converter_task(self) -> Task:
        return Task(
            config=self.tasks_config['string_to_period_converter_task'],
            output_file='string_to_period_converter_task.txt'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Summarizer crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=False,
            full_output=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
