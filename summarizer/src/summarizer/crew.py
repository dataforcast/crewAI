from pydantic import BaseModel
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff

from src.summarizer.tools.custom_tool import CounterWordTool, PercentWordTool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

class Abstract(BaseModel):
    title: str
    content: str


@CrewBase
class Summarizer():
    """Summarizer crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @before_kickoff
    def before_kickoff_function(self, inputs):
        print(f"Before kickoff function with inputs: {inputs}")
        return inputs  # You can return the inputs or modify them as needed

    @agent
    def string_to_period_converter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['string_to_period_converter_agent'],
            verbose=True
        )

    @agent
    def summarizer_agent(self) -> Agent:
        counter_word_tool = CounterWordTool()
        percent_tool = PercentWordTool()

        return Agent(
            config=self.agents_config['summarizer_agent'],
            tools=[counter_word_tool, percent_tool,],
            verbose=True,
        )

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

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=False,
            full_output=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
