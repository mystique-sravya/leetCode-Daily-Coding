class Solution:
    def interpret(self, command: str) -> str:
        new = command.replace('()' , 'o').replace("(al)",'al')
        return new