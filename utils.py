class utils:

    def reversed(self, n):
        """Returns integer n reversed

        Args:
            n (int): integer to be reverse
        """
        if type(n) is not int:
            try: n = int(n)
            except: return False

        if n < 0:
            return -int(str(n)[:0:-1])
        else:
            return int(str(n)[::-1])
    
    def formatter(self, n):
        """Returns integer n in binary and octal format

        Args:
            n (int): starting int
        """
        if type(n) is not int:
            try: n = int(n)
            except: return False

        return (bin(n), oct(n))