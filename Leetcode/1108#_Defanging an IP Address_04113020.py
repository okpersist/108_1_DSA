class Solution:
    def defangIPaddr(self, address: str) -> str:
        input_ = address.find('.')
        print(input_)
        if input_ != -1: 
            address = address.replace('.', '[.]')
        return address