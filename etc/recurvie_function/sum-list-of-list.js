// sum-list.js can be replaced by simple for loop
// but as the array is this complicated, using recursive function makes your code simpler.

let numberAndArrayHell = [3, [1, 4, [3, [6, 2], 5], 1, 3], 4, [8, 1, [2, 1, 9], 5], 5, 9];

function recursive_deep (acc, array) {
    if (array.length === 0) {
        console.log(`total sum is ${acc}.`)
        return acc;
    } else {
        return recursive_deep(acc + 
            (typeof array[0] === 'number' ?
                array[0] :
                recursive_deep(0, array[0])),
            array.slice(1));
    }
}

recursive_deep(0, numberAndArrayHell)