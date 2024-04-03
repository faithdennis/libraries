class SortingAlgorithms(object):
  def selection(list):
    for i in range(len(list)):
      curr = min = list[i]
      min_index = i
      for j, num in enumerate(list):
        if num < min:
          min, min_index = num, j
      list[i], list[min_index] = min, curr
      return list
