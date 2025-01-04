def reverse_words_in_string(s):
    #write your code here
    for word in s.split(" "):
      print(word[::-1], end= " ")
    print()
