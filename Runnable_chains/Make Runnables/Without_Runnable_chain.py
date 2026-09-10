# first make LLM component that use in future by Users/Developers
import random

class Naklillm:

    def __init__(self):
        print('LLM created')

    def predict(self, prompt):

        response_list = [
            'delhi is the capital of india',
            'IPL is a cricket league',
            'AI stands for artificial intelligence'
        ]

        return {'response':random.choice(response_list)}

llm = Naklillm()
result = llm.predict('what is the capital of india')

# print(result)


# 2nd component 

class Nakliprompttemplate:

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variable = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)

template = Nakliprompttemplate(
    template='write a {length} poem about {topic}',
    input_variables=['length','topic']
)

result1 = template.format({'length':'short','topic':'india'})
# print(result1)


# Now think Ai engineear have this 2 components (llm and prompttemplate), now he make llm application that take input from user and it will print poem.

# First make prompt like above
template = Nakliprompttemplate(
    template='write a {length} poem about {topic}',
    input_variables=['length','topic']
)
prompt = template.format({'length':'short','topic':'india'})

# Nowmake LLM
llm = Naklillm()

finel_result = llm.predict(prompt)
# print(finel_result)



# Now build Chain , that connect prompttemplate and llm, so that engineers works become easy

class naklillmchain:

    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):

        finel_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(finel_prompt)

        return result['response']


# Now using this chain , will make naklillm application

template = Nakliprompttemplate(
    template='write a {length} poem about {topic}',
    input_variables=['length','topic']
)

llm = Naklillm()

chain = naklillmchain(llm, template)

resultt = chain.run({'length':'short','topic':'india'})
print(resultt)


# This is not flexible to create , because we cant use llm again in chain 'resultt = chain.run({'length':'short','topic':'india'})' , so team realize its not perfect way.

# Main thing is for interect with prompt class we have to use formate and for llm class we have to use pridict. s this is not standardize . so we have to stanardize it, then only we can make flexible chain.