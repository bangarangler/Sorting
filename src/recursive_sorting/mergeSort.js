// SPLIT ARRAY INTO HALVES AND MERGE THEM RECURSIVELY
function mergeSort(arr) {
  if (arr.length === 1) {
    // RETURN ONCE WE HIT AN ARRAY WITH SINGLE ITEM
    return arr;
  }

  const middle = Math.floor(arr.length / 2); // GET MIDDLE ITEM OF ARRAY ROUND DOWN
  const left = arr.slice(0, middle); // items on left side
  const right = arr.slice(middle); // items on right side

  return merge(mergeSort(left), mergeSort(right));
}

// COMPARE THE ARRAYS ITEM BY ITEM AND RETURN CONCATENATED RESULT
function merge(left, right) {
  let result = [];
  let indexLeft = 0;
  let indexRight = 0;

  while ((indexLeft, left.length && indexRight < right.length)) {
    if (left[indexLeft] < right[indexRight]) {
      result.push(left[indexLeft]);
      indexLeft++;
    } else {
      result.push(right[indexRight]);
      indexRight++;
    }
  }
  return result.concat(left.slice(indexLeft)).concat(right.slice(indexRight));
}

const list = [7, 5, 9, 4, 6, 0, 2, 8, 3];
console.log(mergeSort(list));
