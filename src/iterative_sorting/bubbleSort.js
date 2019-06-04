//// BUBBLESORT
const array = [9, 1, 8, 5, 2, 5, 3, 4, 8];

//function swap(array, i, j) {
//let temp = array[i];
//array[i] = array[j];
//array[j] = temp;
//}

//function bubbleSort(array) {
//for (let i = 0; i < array.length; i++) {
//for (let j = 1; j < array.length; j++) {
//if (array[j - 1] > array[j]) {
//swap(array, j - 1, j);
//}
//}
//}
//return array;
//}
//console.log(bubbleSort(array.slice()));

function bubbleSort(array) {
  let swapped;
  do {
    swapped = false;
    for (let i = 0; i < array.length; i++) {
      if (array[i] && array[i + 1] && array[i] > array[i + 1]) {
        swap(array, i, i + 1);
        swapped = true;
      }
    }
  } while (swapped);
  return array;
}
console.log(bubbleSort(array));
