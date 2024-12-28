def get_prompt() -> str:
    return """
        Answer the question based on only on the following context:
        ```
        {context}
        ```

        Answer the question based on the context above: 
        ```
        {question}
        ```

        If the question is out of context, please answer with "I don't know".
        """

