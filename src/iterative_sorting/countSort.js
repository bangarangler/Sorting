// COUNT SORT
testArr = [3, 0, 2, 5, 4, 1];

let countSort = (arr, min, max) => {
  let i = min,
    j = 0,
    len = arr.length,
    count = [];

  for (i; i <= max; i++) {
    count[i] = 0;
  }

  for (i = 0; i < len; i++) {
    count[arr[i]] += 1;
  }

  for (i = min; i <= max; i++) {
    while (count[i] > 0) {
      arr[j] = i;
      j++;
      count[i]--;
    }
  }
  return arr;
};
console.log(countSort(testArr, 0, 9));
