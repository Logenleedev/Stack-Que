from collections import deque


def hot_potato(names, num):
    queue = deque()
    for name in names:
        queue.appendleft(name)

    while len(queue) > 1:
        for _ in range(num):
            queue.appendleft(queue.pop())

        queue.pop()

    return queue.pop()


# print(hot_potato(('Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'), 9))
# => 'David'


for _ in range(10):
	print('running')


def balanced_check(s):

    if len(s)%2 != 0:
        return False

    opening = set('{[(')

    matches = set([('(',')'),('[',']'),('{','}')])

    stack =[]

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if(last_open,paren) not in matches:
                return False
    return len(stack)==0

# '{{([][])}()}'
