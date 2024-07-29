class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.combos = []

        def generate(digits):
            if len(digits) == n:
                self.combos.append(digits)
                return

            if digits[-1] != "0":
                generate(digits + "0")
            
            generate(digits + "1")

        generate("0")
        generate("1")
        return self.combos
            
