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
