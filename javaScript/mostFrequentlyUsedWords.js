// Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

// Assumptions:
// A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
// Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
// Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
// Matches should be case-insensitive, and the words in the result should be lowercased.
// Ties may be broken arbitrarily.
// If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
// Examples:
// top_3_words("In a village of La Mancha, the name of which I have no desire to call to
// mind, there lived not long since one of those gentlemen that keep a lance
// in the lance-rack, an old buckler, a lean hack, and a greyhound for
// coursing. An olla of rather more beef than mutton, a salad on most
// nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
// on Sundays, made away with three-quarters of his income.")
// # => ["a", "of", "on"]

// top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
// # => ["e", "ddd", "aa"]

// top_3_words("  //wont won't won't")
// # => ["won't", "wont"]
// Bonus points (not really, but just for fun):
// Avoid creating an array whose memory footprint is roughly as big as the input text.
// Avoid sorting the entire array of unique words.

// MI CODIGO
function topThreeWords(text) {
    let frequently = [];
    let top = [];
    let wordsArray = text.toLowerCase().match(/'?([a-z])+'?([a-z])*/g) || [];
    let uniqueWords = wordsArray.filter((element, index, Array) => Array.indexOf(element) === index);
    for(let i=0; i<uniqueWords.length; i++){
        frequently.push(wordsArray.filter(element => element === uniqueWords[i]).length);
    }

    let length = frequently.length;
    for(let i=0; i<length; i++) {
        let maxNum = Math.max(...frequently);
        let index = frequently.indexOf(maxNum);
        top.push(uniqueWords[index]);
        frequently.splice(index,1,0);
    }

    return top.slice(0, 3)
}

// CODIGO CON MEJORES PRACTICAS
let topThreeWords = text => {
    let dict = new Map();
    text.replace(/[A-z']+(?=[ ]+|$)/g, match => {
        let word = match.toLowerCase();
        dict.set(word, dict.has(word) ? dict.get(word) + 1 : 1);
    });
    dict.delete("'");
    return [...dict].sort((a, b) => b[1] - a[1]).map(a => a[0]).slice(0, 3);
};

function topThreeWords(text) {
    let words = {}
    text.toLowerCase().replace(/([A-Za-z][A-Za-z']*)/g, match => {
      let c = words[match] || 0
      words[match] = ++c
    })
    return Object
            .keys(words)
            .sort(function(a,b){return words[b]-words[a]})
            .slice(0,3)
  }

  const topThreeWords = text => {
    let total = (text.toLowerCase().match(/\b[a-z']+\b/g)||[]).reduce((acc,cur) => (acc[cur] = (acc[cur]||0) + 1, acc), {});
    return Object.keys(total).sort((a,b) => total[b] - total[a]).slice(0,3);
  };