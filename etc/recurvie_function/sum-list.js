let numbers = [3, 1, 4, 1, 5, 9];

function recursive(acc, array) {
    if (array.length === 0) {
        console.log(`total sum is ${acc}`)
        return acc
    } else {
        try {
            console.log(`recursive(${acc} [${array}]) is "`)
            return recursive(acc + array[0], array.slice(1));
        } catch (e) {} finally {
            console.log('"is what they said.')
        }
    }
}

recursive(0, numbers)