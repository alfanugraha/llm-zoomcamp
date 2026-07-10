INSTRUCTION = '''
You are a helpful assistant for the LLM Zoomcamp course.
You will answer questions about the course content, homework, and capstone project.
Please provide clear and concise answers based on the information provided in the course materials.
If a question is not covered in the materials, please indicate that you do not have enough information to answer it.

Use the context to find relevant information and provide accurate answers. If the answer is not found in the context, 
respond with "I do not have enough information to answer that question."
'''

USER_PROMPT_TEMPLATE = ''' 
Question:
{question}

Context:
{context}
'''.strip()

class RAGBase:

    def __init__(
        self,
        index,
        llm_client,
        instructions=INSTRUCTION,
        prompt_template=USER_PROMPT_TEMPLATE,
        course="llm-zoomcamp",
        model="gemini-3.5-flash"
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.course = course
        self.prompt_template = prompt_template
        self.model = model

    def search(self, query, num_results=5):
        boost_dict = {"question": 3.0, "section": 0.5}
        filter_dict = {"course": self.course}

        return self.index.search(
            query,
            num_results=num_results,
            boost_dict=boost_dict,
            filter_dict=filter_dict
        )

    def build_context(self, search_results):
        lines = []

        for doc in search_results:
            lines.append(doc["section"])
            lines.append("Q: " + doc["question"])
            lines.append("A: " + doc["answer"])
            lines.append("")

        return "\n".join(lines).strip()

    def build_prompt(self, query, search_results):
        context = self.build_context(search_results)
        return self.prompt_template.format(
            question=query, context=context
        )

    def llm(self, instructions, user_prompt, model="gemini-3.5-flash"):
        response = self.llm_client.interactions.create(
            model=model,
            system_instruction=instructions,
            input=user_prompt
        )
        return response.output_text

    def rag(self, query, model="gemini-3.5-flash"):
        search_results = self.search(query)
        prompt = self.build_prompt(query, search_results)
        answer = self.llm(self.instructions, prompt, model=model)
        return answer