// Complete the solution so that the function will break up camel casing, using a space between words.

// Example
// "camelCasing"  =>  "camel Casing"
// "identifier"   =>  "identifier"
// ""             =>  ""

// MI CODIGO
function breackCamelCase(string) {
    console.log(string.split('').map( element => element.match(/[A-Z]/g) ? element + ' ' : element ).join(''))
    return string.split('').map( element => element.match(/[A-Z]/g) ? ' ' + element : element ).join('');
}

// CODIGO CON MEJORES PRACTICAS
function solution(string) {
    return(string.replace(/([A-Z])/g, ' $1'));
  
  }