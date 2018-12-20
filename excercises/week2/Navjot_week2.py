import pandas as pd


class Cleanup:

    def __init__(self):
        self.cleaned_list=[]
        self.count_dict = {}

    def word_frequency (self, text, val=3):

        for word in text.split():
            self.cleaned_list.append(self.remove_punct(word))

        df = pd.DataFrame(self.cleaned_list, columns = ['WORDS'])
        df['FREQUENCY']= df['WORDS'].value_counts()
        keys = df['WORDS'].value_counts().keys().tolist()
        values = df['WORDS'].value_counts().tolist()

        self.count_dict=dict(zip(keys, values))
        filtered_words = list(filter(lambda x: x[1] > val, self.count_dict.items()))

        return filtered_words

    @staticmethod
    def remove_punct(word):

        punctuation = '''`.~!@#$%^&*()_+-={[\|;'/.,:"?><"']}'''
        punct_list = list(punctuation)
        cnt = 0

        if word[:-1].isdigit():
            clean_word = [w for w in word if w not in punct_list]
            clean_word = ''.join(clean_word)
            word = clean_word
        else:
            clean_word = [w for w in word if w not in punct_list and w.isalpha()]
            clean_word = ''.join(clean_word)

            if clean_word[-1] == 's':
                clean_word = clean_word[:-1]
                cnt = cnt + 1
                word=clean_word
            else:
                word = clean_word
        return word.lower()


paragraph = """
Python is an interpreted, high-level programming language for general-purpose programming. Created by Guido van Rossum 
and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant 
whitespace. It provides constructs that enable clear programming on both small and large scales.[26] In July 2018, 
Van Rossum stepped down as the leader in the language community.[27][28]
Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, 
including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[29]
Python interpreters are available for many operating systems. CPython, the reference implementation of Python, 
is open source software[30] and has a community-based development model, as do nearly all of Python's other implementations. 
Python and CPython are managed by the non-profit Python Software Foundation.
"""

print("****************************** - Before Change - ******************************\n")
print(paragraph)

value = input("\n Enter the Frequency(integer) above which you want to see the word occurance in paragraph: ")

obj = Cleanup()
print("\n****************************** - Filtered List - ******************************\n",
      obj.word_frequency(paragraph, int(value)))

# print("### There were a total of {} words altered ###\n ".format(cleaning_text(paragraph, int(choice))))

