// The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

// maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
// // should be 6: [4, -1, 2, 1]
// Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

// Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.


// MI CODIGO
var maxSequence = function(arr){
    let maxSum = 0;
    if(arr.every(num => num < 0)){
        return maxSum
    }

    for(i=0; i<arr.length; i++){
        let sequenceSize = 1;
        while(sequenceSize <= arr.length){
            if(arr.slice(i,sequenceSize).reduce((a, b) => a + b, 0) > maxSum){
                maxSum = arr.slice(i,sequenceSize).reduce((a, b) => a + b);
            }
            sequenceSize += 1;
        }
    }
    return(maxSum)
}

// CODIGO CON MEJORES PRACTICAS
var maxSequence = function(arr){
    var min = 0, ans = 0, i, sum = 0;
    for (i = 0; i < arr.length; ++i) {
      sum += arr[i];
      min = Math.min(sum, min);
      ans = Math.max(ans, sum - min);
    }
    return ans;
}

var maxSequence = function(arr){
    var currentSum = 0;
    return arr.reduce(function(maxSum, number){
        currentSum = Math.max(currentSum+number, 0);
        return Math.max(currentSum, maxSum);
    }, 0);
}

function maxSequence(arr) {
    var max = 0
    
    for (var i = 0; i < arr.length; i++) {
      for (var sum = 0, j = i; j < arr.length; j++) {
        sum += arr[j]
        if (sum > max) max = sum
      }
    }
    
    return max
  }