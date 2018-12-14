def cleaning_text(text, choice=0):
    print("****************************** - Before Change - ******************************\n")
    print(text)
    puntuation = '''`~!@#$%^&*()_+-={[\|;'/.,:"?><"']}'''
    punct_list = list(puntuation)
    #     print(punct_list)
    str_s_flg = False
    new_para = ''
    cnt = 0
    # Without handling Punctuation
    if choice == 1:
        print("\n ***** Running program to remove \"s\" with handling punctuation ( for ex: large scales.[26] to large scale.[26]) *****\n")
        clean_word = ''
        for word in text.split():
            clean_word = [w for w in word if w not in punct_list and w.isalpha()]
            clean_word = ''.join(clean_word)

            # To handle words like 1996, where clean_word = ''
            if len(clean_word) == 0:
                word = word

            else:
                if clean_word[-1] == 's':
                    clean_word = clean_word[:-1]
                    str_s_flg = True
                    cnt = cnt + 1

                    # Stiching the string back after removing the "s"
                    if len(word[len(clean_word):]) > 1 and word[len(
                            clean_word):] != "'s":  # Handling apostrophe sign
                        word = word[:len(clean_word)] + word[len(clean_word) + 1:]

                    else:
                        word = word[:len(clean_word)]

                else:
                    str_s_flg = False

            clean_word = ''
            new_para = new_para + ' ' + word

        print("\n", new_para[1:], '\n')
        return cnt
    #         print("\n",new_para)

    # Without handling Punctuation
    elif choice == 0:
        print("\n ****************************** Running program to remove \"s\" without handling puntuation ******************************\n")

        for word in text.split():
            if word[-1] == 's':
                word = word[:-1]
                cnt = cnt + 1
            new_para = new_para + ' ' + word

        print("\n", new_para[1:], '\n')
        return cnt

    else:

        return "Invalid Choice"


#Main Body



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

print("""
\n Select the option for which you want to run the program:
\n Press 0 : For running program to remove "s" without handling puntuation 
\n Press 1 : For running program to remove "s" with handling punctuation ( for ex: large scales.[26] to large scale.[26])
""")

choice = input("\n Enter the your choice :")

print("### There were a total of {} words altered ###\n ".format(cleaning_text(paragraph, int(choice))))