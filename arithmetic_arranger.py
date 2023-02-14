def arithmetic_arranger(problems, value=False):
  arranged_work = ""
  if len(problems) > 5:
    arranged_work = "Error, too many jobs"
    return arranged_work

  # to capture operators
  operations = list(map(lambda x: x.split()[1], problems))
  if set(operations) != {'+', '-'} and len(set(operations)) != 2:
    arranged_work = "Error, Operator must be '+' or '-'."
    return arranged_work

  #To capture operands
  operans = []
  for i in problems:
    x = i.split()
    operans.extend([x[0], x[2]])

  if not all(map(lambda x: x.isdigit(), operans)):
    arranged_work = "Error, Numbers must only contain digits."
    return arranged_work

  if not all(map(lambda x: len(x) < 5, operans)):
    arranged_work = "Error, Numbers cannot be more than four digits."
    return arranged_work

    top_row = ""
    dashes = ""
    values = list(map(lambda x: eval(x), problems))
    result = ""
    for i in range(0, len(operans), 2):
      space_width = max(len(operans[i]), len(operans[i + 1])) + 2
      top_row += operans[i].rjust(space_width)
      dashes += '-' * space_width
      result += str(values[i // 2]).rjust(space_width)
      if i != len(operans) - 2:
        top_row += ' ' * 4
        dashes += ' ' * 4
        result += ' ' * 4

    bottom_row = ''
    for i in range(1, len(operans), 2):
      space_width = max(len(operans[i - 1]), len(operans[i])) + 1
      bottom_row += operations[i // 2]
      bottom_row += operans[i].rjust(space_width)
      if i != len(operans) - 1:
        bottom_row += ' ' * 4

    if value:
      arranged_work = '\n'.join((top_row, bottom_row, dashes, result))
    else:
      arranged_work = '\n'.join((top_row, bottom_row, dashes))
    return arranged_work
