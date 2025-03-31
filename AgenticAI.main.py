llm = LLM(model= "gpt-4")
#tool 2
search_tool=SerperDevTool(n=10)

#Agent 1
Senior_research_analyst= Agent(
    role= "Senior Research Analyst",
    goal= f"Research, analyze and synthesie comprehensive information on {topic} from reliable web search",
    backstory= "You are a very smart analyst."
                "You excel at finding, analyzing and synthesizing information from accross the internet"
    Verbose= True,
    Alow_delegation= False,
    tools= [search tool],
    llm= llm)

#Agent 2
Content_writer= Agent(
    role= "Content writer",
    goal= "Transform research findings into engaging blog while maintaining accuracy"
    backstory= "You are skilled content writer specialized in content generation"
                "You work closely with senior research analyst and excel at maintaining the perfect"
    Verbose= True,
    Alow_delegation= False,
    llm= llm)

#Research Tools
research_tasks= Task(
    description= ("""
              1. Conduct comprehensive research on {topic} including:
                  - Recent developments and news
                  - Key industry trends and innovations
                  - Expert opinions and analyses
                  - Statistical data and market insights
              2. Evaluate source credibility and fact check all information
              3. Organize findings into a structured research brief
            """)
    Exoected_Output= """" A detailed research report containing:
            -Executive summary of key findings
            - Comprehensive analysis of current trends and developments
            - List of verified facts and original sources. """,
    agent = Senior_research_analyst
)

#Task 2 content writing
writing_task= Task(
    description= (""" Using the research briedf provided, create an engaging blog post that:
             1. Transforms all factual accuracy and citations from the research
             2. Maintain technical information
             3. includes:
                 - Attention-grabbing introduction
                 - Well- structured body sections with clear headings
            4. Include a reference section at the end""" ),
    Expented_Output= """A polished blog post in markdown format that:
             - Engages readers while maintaining accuracy
             - Contains properly structured sections
             - includes inline citations hyperlinked to the original source url""",
    agent=  Content_writer      
)
crew = Crew(
    agents= [Senior_research_analyst,Content_writer],
    tasks= [research_tasks,writing_task],
    verbose = True
)

result = crew.kickoff(input = {"topic" :topic})
print(result)
