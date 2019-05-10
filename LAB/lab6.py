import ArrayStack

# problem 1

def reverse_string(input_str, low=0, high=None):
    if high is None:
        high = len(input_str)
    if low == high:
        return ''
    return reverse_string(input_str,low+1,high) + input_str[low]


print(reverse_string('how are you'))


# problem 2


def get_tag(text):
    for word in text.split():
        if word[0] == '<' and word[-1] == '>':
            yield word [1:-1]


def is_matched_html(text):
    tag_stack = ArrayStack.ArrayStack()
    html_list = text.split('\n')
    for line in html_list:
        for tag in get_tag(line):
            print(tag_stack._data)
            if tag[0] != '/':
                tag_stack.push(tag)
            elif tag_stack.is_empty() or tag[1:] != tag_stack.top():
                return False
            else:
                tag_stack.pop()
    if not tag_stack.is_empty():
        return False
    return True



if __name__ == '__main__':
    with open('html_file.html', 'r') as html_text:
        html = html_text.read()
        print(is_matched_html(html))