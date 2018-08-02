# migrated from python 2.7
check_command = lambda p,a: ''.join(['1' if x.isalpha() else '0' for x in list(a.zfill(p.bit_length()))]) == '{:032b}'.format(p)[-len(a):]