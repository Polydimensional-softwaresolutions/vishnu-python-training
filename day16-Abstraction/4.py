# 4. Abstraction Through Parameters (Hiding Configuration) 
# Challenge: Use method parameters to abstract complex configuration details, making the main task simple.
# Requirements:
# Create a class Printer.
# Define a public method print_document(pages, color_mode, paper_size) which takes three arguments representing configuration details.
# Inside print_document(), simply print the following three lines to show the configuration is being handled internally:
# "Configuring settings: Color=[color_mode], Size=[paper_size]"
# "Warming up print head..."
# "Printing [pages] pages..."
# Create a Printer object and call print_document(pages=10, color_mode="CMYK", paper_size="A4"). The method call itself is the simple action (printing), while the parameters abstract the technical setup.

class printer:
    def print_documents(self,pages,color_mode,paper_size):
        self.pages=pages
        self.color_mode=color_mode
        self.paper_size=paper_size
        print(f"Configuring settings: Color={self.color_mode}, Size={self.paper_size}")
        print("Warming up print head...")
        print(f"Printing {self.pages} pages...")
obj=printer()
obj.print_documents(50,"Red","A4")