#!/usr/bin/env python
import sys
import warnings

from summarizer.crew import Summarizer

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': text,
    }
    
    try:
        Summarizer().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": text
    }
    try:
        Summarizer().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Summarizer().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """

    TEXT = """10/2023 Now
    • Technical leader
    Credit Agricole (banking area)
    Development of the technical strategy, contribution to the LLM base
    Design of the technical architecture for the deployment in
    SaaS mode of an email categorisation solution
    Design of a solution based on generative AI for the deployment of
    an assistant on the client workstation.
    Design of the software architecture for the solution in micro
    services and REST APIs for integration with the messaging system.

    10/2021 09/2023
    Senior Architect / Lead Data-Scientist
    Capgemini / Hybrid Intelligence
    • Assessment and architecture development for SaaS deployment
    of an SaaS mode of an IoT/Batch data processing solution on
    Azure/AWS/"On premises
    • Audit of a Python-Datascience source code, re-engineering it for
    its industrialization in a context of a business application managing
    metadata with a graph model (life sciences), design of the
    technical architecture for deployment/production in SaaS mode
    • Industrialization of source code of an NLP based solution for
    automatic generation of quotations
    • Design of a conceptual graph data model and implementation of
    of the cloud data workflow for a leading industrial company
    • Development of a digital twin ontology model feeded by IoT
    sensors on Azure for a steel manufacturer
    • Analysis of how Deep Learning models based on transformers
    work to implement fine-tuning methods

    01/09/2022 Now
    Data-scientist teacher
    EML-Lyon (9 th business sch. world ranking, Financial Times)
    • Machine learning and deep learning basics
    • Python object oriented programming

    01/05/2021 31/07/2021
    BPCE group (bank, insurance)
    Product Owner / Lead Data-Scientist
    • Industrialization of machine learning systems
    • Specification of industrialization methodology
    • Specification of machine learning monitoring
    • Workshops animation

    01/2021 04/2021
    Lead Data-Scientist
    OAIO / subsidiary of the infotel group
    • Study of the development of an AI practice intended for PO
    • Development of a proof of concept based on ML model
    • Interpretation model of explanatory variables

    07/2020 12/2020
    Lead Data-Scientist / Corporate Strategy Department
    Bouygues Telecom / Konatus project
    • Study of the realization of a B2B software suite powered with
    A.I. to enhance the digital assets of the company.
    • Design and prototyping of the solution based on SKOS-RDF
    • Analysis of ontologies databases eco-system: OntoDB, Neo4j,
    LP-ETL

    01/2020 06/2020
    Lead Data-Scientist (leading 5 Data scientists)
    Bouygues Telecom / Internet client experience
    • Machine Learning : unsupervized, supervized, NLP
    • Data analysis over data streams
    • Time series modeling: ARMA/ARIMA/SARIMA , RNN, CNN

    11/2019 Now
    Full-stack Data-Scientist teacher
    JEDHA bootcamp
    • Data Analysis : seaborn, matplotlib, numpy, pandas
    • Dimension reduction : PCA, DFA
    • Machine Learning (supervised, unsupervised), deep learning
    • NLP, API&Web scrapping, Cloud computing


    08/2019 10/2019
    Lead Data-Scientist
    MARGO (Finance industry)
    ● Methodological and technical support, mentoring.
    ● Data-preparation, exploratory analysis, inferential statistics
    ● Software engineering, Machine Learning and Deep Learning
    algorithms integration into web applications
    ● Deployment support, update of predictive models in production
    ● Evangelization of AI technologies with business departments.


    02/2018 07/2019
    Data-scientist
    DATAFORCAST (Data-Sciences) Project link
    Kaggle : toxics conversations detector on social networks
    AdaNet : ensemble method applied to the CNN and RNN networks
    Images classifier with Deep Learning and Machine Learning algo.
    NLP Engine TAG generator for StackOverflow platform
    Segmentation of a e-business customers database
    Estimator for aircraft flights delay in USA
    Engine for movies recommendation over IMDB database

    09/2018 12/2018
    Consultant R&D / Blockchain
    DATAFORCAST / TALIUM (Blockchains integrator)
    Development of a JAVA platform for ICO / STO fundraising.
    Market positioning study of Blockchains supporting data
    market place services.

    12/2017 06/2018
    Data Scientist
    DATAFORCAST / PROBRAIN FRANCE (Software editor)
    Customer database segmentation using M.L. algorithms.
    Maintenance of WEB-JEE applications for digital TV.
    Management and multi-site integration for a CRM application.
    Functional and technical study of integration of an open source CRM.
    PyRoboc : labyrinth game development in Python."""

    inputs = {
        "topic": TEXT
    }
    try:
        Summarizer().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
