# 2. Multi-Format Report Generator (Polymorphism, Inheritance, Abstraction) 📄
# Challenge: Design a system to output data in different formats (JSON and XML) using OOP pillars.
# Requirements:
# Inheritance: Create a base class ReportGenerator with a constructor taking a dictionary of data.
# Polymorphism & Abstraction: Define an abstract method placeholder generate_output() in the base class.
# Create two subclasses: JsonGenerator and XmlGenerator.
# Implement generate_output() in both:
# JsonGenerator returns a JSON-like string representation.
# XmlGenerator returns a simple XML-like tag representation.
# Create a public function render_report(generator_object) that takes any generator object and prints its output, providing Abstraction over the format details.

from abc import ABC,abstractmethod
class ReportGenerator(ABC):
    def __init__(self,data):
        self.data={}
    @abstractmethod
    def generate_output(self):
        pass
class JsonGenerator(ReportGenerator):
    def generate_output(self):
        return "JSON-like string representation."

class XmlGenerator(ReportGenerator):
    def generate_output(self):
        return "simple XML-like tag representation."
    
def render_report(generator_object):
    print(generator_object.generate_output())

data={"name":"vishu","age":27}
obj1=JsonGenerator(data)
obj2=XmlGenerator(data)

render_report(obj1)
render_report(obj2)

         
    

        