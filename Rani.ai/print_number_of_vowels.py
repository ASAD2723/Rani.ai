def vowel_count(str):

    count = 0
    vowels = set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowels:
            count = count + 1
      
    print("No. of vowels :", count)

str = "Hello Everyone"

vowel_count(str)