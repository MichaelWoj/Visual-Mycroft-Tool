from mycroft import MycroftSkill, intent_file_handler


class Demo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('demo.intent')
    def handle_test(self, message):
        self.speak_dialog('demo')


def create_skill():
    return Demo()
