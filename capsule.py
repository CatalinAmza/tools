def get_capsule(source, left_shell, right_shell, starting_position=0):               # returns (chunk, start, end) where
    if left_shell in right_shell or right_shell in left_shell:                       # $chunk is the first chunk of $source, after $starting_position,
        raise Exception('Your shells contain each other. Illegal use.')              # that's encapsulated between $left_shell and $right_shell
    else:                                                                            # (including the capsule) and $start is the index of the beginning of the core and $end its end.
        first_left_shell = source[starting_position:].find(left_shell)
        if first_left_shell == -1:                                                   # no left shells
            qprint('No left shells on your capsule.', color=YELLOW)
            return -1
        else:
            current = starting_position + first_left_shell + len(left_shell)
            count = 1                                                                # number of left shells unclosed
            while count > 0:
                current_left = source[current:].find(left_shell)                     # first left shell after the cursor
                current_right = source[current:].find(right_shell)
                if current_right == -1:
                    qprint('Capsule cracked - not enough right shells.', color=YELLOW)
                    return -1
                if current_left == -1:                                               # no more left shells to be closed
                    current_left = current_right + 1
                if current_left < current_right:                                     # new unclosed left shell
                    count += 1
                    current += current_left + len(left_shell)
                else:                                                                # closed existing left shell
                    count -= 1
                    current += current_right + len(right_shell)
            return [source[starting_position + first_left_shell: current], starting_position + first_left_shell + len(left_shell), current - len(right_shell)]


def get_core(source, left_shell, right_shell, starting_position=0):                  # returns the first chunk of $source, after $starting_position,
    res = get_capsule(source, left_shell, right_shell, starting_position)            # that's encapsulated between $left_shell and $right_shell (excluding the capsule)
    if res == -1:
        return -1
    else:
        return source[res[1]: res[2]]


def get_all_cores(source, left_shell, right_shell, starting_position=0):
    res = []
    item = get_capsule(source, left_shell, right_shell, starting_position)
    while item != -1:
        res.append(source[item[1]:item[2]])
        item = get_capsule(source, left_shell, right_shell, item[2] + len(right_shell))
    return res
