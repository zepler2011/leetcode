#letters = 'abcdefghijklmnopqrstuvwxyz'
import string
letters = string.ascii_lowercase

def main():
   word = 'hit'
   for i in range(len(word)):
      print word[i]
      left = word[:i]
      right = word[i+1:]
      print left, right
      for l in letters:
         newWord = left + l + right
         #print newWord

if __name__ == "__main__":
   main()