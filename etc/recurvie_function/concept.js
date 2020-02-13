// example code from yalpaks

function recursive (argument) {
    do the job
    if (condition) {
        return result
    } else {
        return recursive (worked argument)
    }
}


function answerByStory (question) {
    // find answer from the randomStory
    let answer = findFromRandomStory();

    // if the answer is not found
    if (answer == null) {
        return answerByStory(question);

    // if answer is there
    } else {
        return answer;
    }
}
