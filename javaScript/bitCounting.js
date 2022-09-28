// Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

// Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

// MI CODIGO
var CountBits = function(n) {
    return Math.abs(n).toString(2).split('1').length - 1;
}

//CODIGO CON MEJORES PRACTICAS
var countBits = function(n) {
    return n.toString(2).replace(/0/g,'').length;
  };

const countBits = n => n.toString(2)
  .split('')
  .filter(ele => ele == 1)
  .length

var countBits = function(n) {
  a = n.toString(2).match(/1/g);
  return a == null ? 0 : a.length;
};