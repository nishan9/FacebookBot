from fbchat import Client, ThreadType
from PyDictionary import PyDictionary
from googletrans import Translator
from nltk.corpus import wordnet as wn

EMAIL = ""
PASSWORD = ""
dictionary = PyDictionary()
translator = Translator()


class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        friendlist = client.searchForUsers("", 2);thisi = friendlist[0]
        friendlist = client.searchForUsers("", 2);achira = friendlist[0]

        if thread_id == #.uid:
            print("Incoming Message: " + message_object.text + "From " + "Thisansa")
        if thread_id == #.uid:
            print("Incoming Message: " + message_object.text + "From " + "Achira")
        
        if thread_id == thisi.uid and author_id != self.uid:
            sendit = input("Y/N")
            if sendit == "Y":
                msg = input("Reply: ")
                self.sendMessage(msg, thread_id=thread_id)

        # Dictionary Lookup 
        input_string = message_object.text
        if "define" in input_string or "Define" in input_string:
            word = input_string[6:]
            text = dictionary.meaning(word)
            for key, value in text.items():
                s = ""
                for i in value[:3]:
                    s = s + i + ", "
                stree = key + ": " + s
                if thread_type == ThreadType.GROUP:
                    self.sendMessage(stree, thread_id=thread_id, thread_type=ThreadType.GROUP)
                self.sendMessage(stree, thread_id=thread_id)
        # Translation
        if input_string[:2] == "T ":  # Text is for translation
            totrans = input_string[2:-5:]
            if input_string[-2:] == "fr" and input_string[-5:-3] == "en":  # translate to fr from en
                ob = translator.translate(totrans, dest='fr', src='en')
            if input_string[-2:] == "en" and input_string[-5:-3] == "fr":  # translate to en from fr
                ob = translator.translate(totrans, dest='en', src='fr')
            if input_string[-2:] == "lk":
                totrans = input_string[2:-3:]
                ob = translator.translate(totrans, dest='si', src='en')
            translated = ob.text
            if thread_type == ThreadType.GROUP:
                self.sendMessage(translated, thread_id=thread_id, thread_type=ThreadType.GROUP)
            self.sendMessage(translated, thread_id=thread_id)
        
        # Test Bot for Feedback 
        if message_object.text == "Test":
            if thread_type == ThreadType.GROUP:
                self.sendMessage("I work. From Bot. ", thread_id=thread_id, thread_type=ThreadType.GROUP)
            self.sendMessage("I work but like the old way :(", thread_id=thread_id)

        #Find Synonyms 
        if input_string[:4] == "Syn ":
            word = input_string[4:]
            synslist = ""
            for i in wn.synsets(word):
                for i in i.lemma_names():
                    synslist = synslist + i + ", "
            if thread_type == ThreadType.GROUP:
                self.sendMessage("Synonyms are " + synslist, thread_id=thread_id, thread_type=ThreadType.GROUP)
            self.sendMessage("Synonyms are " + synslist, thread_id=thread_id)

        #Find Examples
        if input_string[:8] == "example ":
            word = input_string[8:]
            for idx, val in enumerate(wn.synsets(word)[0].examples(), start=1):
                examples = "Example " + str(idx) + ": " + str(val)
            if thread_type == ThreadType.GROUP:
                self.sendMessage(examples, thread_id=thread_id, thread_type=ThreadType.GROUP)
            self.sendMessage(examples, thread_id=thread_id)

client = EchoBot(EMAIL, PASSWORD)
client.listen()
