// ver2: Promise
searchStudentInfo("12345")
.then(function (studentInfo) {
    let studentPersonalId = studentInfo["personalId"];
    let highSchoolName = studentInfo["highSchoolName"];
    return searchHighSchoolDBAddress(studentPersonalId, highSchoolName)
})
.then(function (studentPersonalIdAndHighSchoolDBAddress) {
    let studentPersonalId = studentPersonalIdAndHighSchoolDBAddress[0];
    let highSchoolDBAddress = studentPersonalIdAndHighSchoolDBAddress[1];
    return searchLectureInHighSchool(highSchoolDBAddress, studentPersonalId)
})
.then(function (listOfLecture) {
    let lectureIdGo3Student = listOfLecture["Go3Math"];
    return searchLectureInfo(lectureIdGo3Student)
})
.then(function (lectureInfo) {
    console.log(`Teacher: ${lectureInfo["teacherName"]}`);
})


function searchStudentInfo(studentId) {
    return new Promise(function (resolve, reject) {
        ajax(baseUrl + "student-info/" + studentId,     // 1st arg: async task
        function (response) {                           // 2nd arg: callback function as getting the result from async task as input arg
            resolve(response);
        });
    });
}

// Here is different with func in callbackHell since it is difficult to pass argument over multiple functions in Promise
function searchHighSchoolDBAddress(studentPersonalId, highSchoolName) {
    return new Promise(function (resolve, reject) {
        ajax(baseUrl + "highschool-db/" + highSchoolName,
        function (response) {
            resolve(studentPersonalId, response);
        });
    });
}

function searchLectureInHighSchool(highSchoolDBAddress, studentPersonalId) {
    return new Promise(function (resolve, reject) {
        ajax(baseUrl + "classes/" + highSchoolDBAddress + "/" + studentPersonalId,
        function (response) {
            resolve(response);
        });
    });
}

function searchLectureInfo(lectureIdOfStudent) {
    return new Promise(function (resolve, reject) {
        ajax(baseUrl + "class-info/" + lectureIdOfStudent,
        function (response) {
            resolve(response);
        });
    });
}
