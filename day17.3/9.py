# Polymorphic Notification System (Polymorphism, Abstraction) 
# Challenge: Design a system that can send notifications through various channels using a unified interface.
# Requirements:
# Create a base class Notifier.
# Define an abstract method send(message).
# Create subclasses EmailNotifier and SMSNotifier.
# Implement send(message) in both to print a formatted message specific to their channel (e.g., "Email sent to..." vs. "SMS sent to...").
# Create a function notify_users(message, notifiers_list) that takes a message and a list of notifier objects. Use a loop to call the send() method on every object in the list (Polymorphism).

from abc import ABC,abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self,message):
        pass
class EmailNotifier(Notifier):
    def send(self,message):
        print(f'Email sent to {message}')

class SMSNotifier(Notifier):
    def send(self,message):
        print(f'SMS sent to {message}')

def notify_users(message,notify_list):
    for i in notify_list:
        i.send(message)

mail=EmailNotifier()
sms=SMSNotifier()

obj=[mail,sms]
notify_users("the system is updated and messages are sent",obj)
    