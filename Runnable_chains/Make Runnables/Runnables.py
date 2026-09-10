# now we see how to make standardize component code using Runnables and make chain

# make abstract class called runnables , now in that inherite both component classes so Every class now become runnable cause of inheritance , and in runnable every abstract method it have , we have to develope it into our component class. so every one hase common structure.

import random
from abc import ABC, abstractmethod

# Runnable is abstactclass that inherit from ABC
class Runnable(ABC):

    @abstractmethod
    def invoke(input_data):
        pass

# This class inherit fron Runnable, so it also be runnable
class Naklillm(Runnable):

    def __init__(self):
        print('LLM created')

    # So here we must have to create invoke method cause it is in abstarct class , otherwise when we run this class it through error like you not impiliment abstract method..
    def invoke(self, prompt):
        response_list = [
            'delhi is the capital of india',
            'IPL is a cricket league',
            'AI stands for artificial intelligence'
        ]
        return {'response':random.choice(response_list)}  
    # So here now whatever work do by pridict method now it done by invoke method.

    def predict(self, prompt):
        
        response_list = [
            'delhi is the capital of india',
            'IPL is a cricket league',
            'AI stands for artificial intelligence'
        ]
        return {'response':random.choice(response_list)}
    # So now what about this predict method , so we not have to delete it cause at past many AI Engineers use this , so here in return just type this code is deprecated..., so in output they get warning message and you have to call invoke method.



# 2nd component , Do same work like naklillm class

class Nakliprompttemplate(Runnable):

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variable = input_variables

    def invoke(self,input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)


# We add this class also , that just give only response of result
class naklistrOutputparse(Runnable):

    def __init__(self):
        pass

    def invoke(self,input_data):
        return input_data['response']


# Now we have to make class , so using this we can chaintogether 2 or more components.

class RunnableConnecter(Runnable):

        # Here we give list of components(Runnables) as input
        def __init__(self, runnable_list):
            self.runnable_list =runnable_list

        def invoke(self, input_data):

            # In this loop , suppose runnablelist is (prompt, llm), so first call invoke method of prompt and store result into input_data after again it run and call invoke method of llm and for llm input it get input_data..., so ouput of privious step is make input of next step.
            for runnable in self.runnable_list:
                input_data = runnable.invoke(input_data)

            return input_data



# Now make prompt, llm , chain and get output

template = Nakliprompttemplate(
    template='write a {length} poem about {topic}',
    input_variables=['length','topic']
)

llm = Naklillm()

parser = naklistrOutputparse()

chain = RunnableConnecter([template, llm, parser])

result = chain.invoke({'length':'long','topic':'india'})

print(result)



# Now make chain using 2 or more chain (4th priciple of runnable)

template1 = Nakliprompttemplate(
    template="Write joke about {topic}",
    input_variables=['topic']
)

template2 = Nakliprompttemplate(
    template="Write a summary about following joke {response}",
    input_variables=['response']
)

llm = Naklillm()

parser = naklistrOutputparse()

# Make chain 1 to get joke
chain1 = RunnableConnecter([template1,llm])

# make chain2 for summary of joke
chain2 = RunnableConnecter([template2, llm, parser])

finel_chain = RunnableConnecter([chain1, chain2])

result = finel_chain.invoke({'topic':'cricket'})
print(result)