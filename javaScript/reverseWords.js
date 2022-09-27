// Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

// Examples
// "This is an example!" ==> "sihT si na !elpmaxe"
// "double  spaces"      ==> "elbuod  secaps"

// MI CODIGO
function reverseWords(str) {
    // Go for it
    let words =  str.split(' ');
    let reverse = '';
    for(let i=0; i<words.length; i++){
        let word = words[i];
        for( let j=0; j<word.length; j++){
            reverse = reverse.concat(word[word.length-1-j]);
            console.log(word)
        }   
        if(i+1 != words.length){
            reverse = reverse.concat(' ');
        }
    }
    console.log(reverse);
}

// CODIGO CON MEJORES PRACTICAS
function reverseWordsBP(str) {
    return str.split(' ').map(function(word){
      return word.split('').reverse().join('');
    }).join(' ');
}