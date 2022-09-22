def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts =[100, 300, 500, 600, 900, 1000]
  low=medium=high=0
  for i in range(0,len(counts)):
    if counts[i]<410:
      low+=1
    elif counts[i]>410 and counts[i]<909:
      medium+=1
    else:
      high+=1
  print(low)
  print(medium)
  print(high)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
