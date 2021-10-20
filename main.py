def hiding_repeted_chars(lst):
    result= []
    for i in lst:
        if i not in result:
            result.append(i)
    print(result)

def find_the_str(string, lst):
    if any(string in word for word in lst):
        print("Yes")
    else:
        print("No")

def find_repeated_string(lst):
    frq = {}
    max_frq = 0
    max_str_frq = ""
    for string in lst:
        if string not in frq:
            frq[string] = 1
        else:
            if max_frq < frq[string]:
                max_frq = frq[string]
                max_str_frq = string
            frq[string] += 1
    print(max_str_frq)

def display_the_palindroms(lst):
    palindromes = []
    for word in lst:
        length = len(word) - 1
        index = 0
        is_palindrome = 0
        while index < length:
            if word[index] == word[length]:
                is_palindrome = 1
            else:
                is_palindrome = 0
            index+=1
            length-=1

        if is_palindrome:
            palindromes.append(word)
    print(palindromes)

def display_the_frq_array(lst):
    frq = {}
    max_char = ""
    max_frq_char = 0
    for word in lst:
        for char in word:
            if char not in frq:
                frq[char] = 1
            else:
                if frq[char] > max_frq_char:
                    max_char = char
                    max_frq_char = frq[char]
                frq[char] += 1
    for word in lst:
        if any(max_char in c for c in word):
            print(max_frq_char + 1)
        else:
            print(word)

def main():
    problem = input("Choose a problem: ")
    if problem == "1":
        n = int(input("Read the length: "))
        lst = []
        print("Read the array elements: ")
        for i in range(n):
            lst.append(input())
        hiding_repeted_chars(lst)
    elif problem == "2":
        string = input("Read a string: ")
        lst = ['aaa', 'bbb', 'cmtc', 'drd', 'aaa']
        find_the_str(string, lst)
    elif problem == "3":
        lst = ['aaa', 'bbb', 'cmtc', 'drd', 'aaa']
        find_repeated_string(lst)
    elif problem == "4":
        lst = ['ada', 'abc', 'cmtc', 'drd', 'aaa']
        display_the_palindroms(lst)
    elif problem == "5":
        lst = ['aaa', 'bbab', 'caamtc', 'drd', 'aaa']
        display_the_frq_array(lst)

if __name__ == '__main__':
    main()
