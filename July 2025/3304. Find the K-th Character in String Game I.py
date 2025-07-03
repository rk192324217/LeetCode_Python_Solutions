class Solution:
    def kthCharacter(self, k: int) -> str:

        #Less Efficient
        """
        mapping={
            "a":"b","b":"c","c":"d","d":"e","e":"f","f":"g",
            "g":"h","h":"i","i":"j","j":"k","k":"l","l":"m",
            "m":"n","n":"o","o":"p","p":"q","q":"r","r":"s",
            "s":"t","t":"u","u":"v","v":"w","w":"x","x":"y",
            "y":"z","z":"a"
        }"""
        str_final="a"
        while len(str_final)<=k:
            new_str=""
            for i in str_final:
                if i=="z":
                    new_str+="a"
                else:
                    new_str+=chr(ord(i)+1)
            str_final+=new_str
        return str_final[k-1]
        