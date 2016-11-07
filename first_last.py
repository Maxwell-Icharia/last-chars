def both_ends(s):
    if len(s) >= 2:
      first = s[0] + s[1]
      last = s[-2] + s[-1]
      joint = first + last
      return joint
    else:
      return ''