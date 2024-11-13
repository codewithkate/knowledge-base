# Monday, November 12, 2024
## A Python Data Engineer’s Journey with Snowflake
From ingestion, transformation to operationalization

Options available for different use cases:

![[snowflake-pipelines.png]]

![[snowflake-python-data-engineering-flow.png]]

- Snowflake Notebooks: python, sql or markdown cells
- External Access Private Connectivity: connect and ingest data
- pandas on Snowflake: faster performance with distributed compute so it's not single thread processing. you can work with more data. no need to rewrite code in big data language. compiles to sql to run on snowflake engine (how snowpark pandas API works). 
- snowpark updates: orchestration and devops. import and create a session.