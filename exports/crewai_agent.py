from crewai import Agent

socratic_concept_dependency_grapher = Agent(
    role="Socratic Concept Dependency Grapher",
    goal="Deliver high-precision autonomous Socratic Concept Dependency Grapher operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
