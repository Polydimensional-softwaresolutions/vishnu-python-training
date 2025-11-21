# 3. Document Rendering Tool 
# Challenge: Create a system for rendering various document formats with common handling but hidden complexity.
# Requirements:
# Inheritance: Create a base class Document with a constructor that takes content.
# Polymorphism: Create subclasses PDFDocument and HTMLDocument. Both must implement a method render() that returns a string formatted according to their type (e.g., "PDF Output: ..." vs. "HTML Output: ...").
# Encapsulation: In the base class Document, strictly encapsulate the raw content attribute (self.__raw_content). Provide a public method get_content_length() to access the length of the content without exposing the data itself.
# Abstraction: Define a main function display_document(doc_object) that takes any Document object, calls its render() method, and prints the output, hiding the type-specific rendering logic.


class Document:
    def __init__(self, content):
        self.__raw_content = content  # strictly encapsulated

    def get_content_length(self):
        return len(self.__raw_content)

    # Protected helper to allow subclasses to access content indirectly
    def _get_raw_content(self):
        return self.__raw_content


# Subclass implementing polymorphism
class PDFDocument(Document):
    def render(self):
        content = self._get_raw_content()
        return f"PDF Output: {content}"


# Another subclass implementing polymorphism
class HTMLDocument(Document):
    def render(self):
        content = self._get_raw_content()
        return f"HTML Output: <p>{content}</p>"


# Abstraction: works with ANY Document object without knowing details
def display_document(doc_object):
    output = doc_object.render()
    print(output)


# Example usage:
obj1 = PDFDocument("This is a PDF document.")
obj2 = HTMLDocument("This is an HTML document.")

display_document(obj1)
display_document(obj2)


print("PDF content length:", obj1.get_content_length())
print("HTML content length:", obj2.get_content_length()) 