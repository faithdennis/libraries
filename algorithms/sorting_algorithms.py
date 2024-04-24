class SortingAlgorithms(object):
  def selectionsort(list):
    for i in range(len(list)):
      curr = min = list[i]
      min_index = i
      for j, num in enumerate(list):
        if num < min:
          min, min_index = num, j
      list[i], list[min_index] = min, curr
      return list
// TODO 
  def heapsort(list, bottom_up=True):
    heap = # heapify
    heap.size = len(list)
    for i in range(len):

// TODO
  def mergesort(list):

// TODO
  def quicksort(list):
// TODO
  def insertsort(list):
    for i in range(1, len(list)):
      j = i - 1
      while list[i] < list[j]:
        curr = list[i]
        list[i] = list[j]
        list[j] = curr
        i, j = j, j - 1
      return list
