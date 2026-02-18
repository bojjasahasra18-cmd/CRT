def Reverse_String(s: str) -> str:
   c = ''
   for i in range(len(s)-1, -1, -1):
      c += s[i]
   return c
   



if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))
