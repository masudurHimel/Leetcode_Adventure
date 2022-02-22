class Solution:
    def interpret(self, command):
        _ = command.replace("()", "o")
        return _.replace("(al)", "al")